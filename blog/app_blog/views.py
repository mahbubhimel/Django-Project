from django.utils.text import slugify
import uuid
from dataclasses import fields
from app_blog.forms import CommentForm, DiabetesForm, ChatForm
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView, View,DeleteView
from app_blog.models import Blog, Diabetes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Library For ML predictions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers

from app_blog.serializer import CustomerSerializers
import numpy as np
import pandas as pd
import pickle
from sklearn import preprocessing 

# from tensorflow.keras.models import load_model
# for class based view, @login_required cannot be used, thats why LoginRequied Mixin is imported
# Create your views here.



class CreateBlog(LoginRequiredMixin, CreateView):  # CreateView Can generate FORM using a Model
    model = Blog                                # Here a form is created using the model named Blog
    template_name = 'app_blog/create_blog.html'
    fields = ('blog_title','blog_content','image')

    def form_valid(self, form):
        blog_object= form.save(commit=False)
        blog_object.user= self.request.user #?????
        title=blog_object.blog_title
        blog_object.slug = title.replace(" ","-")+"-"+str(uuid.uuid4())
        blog_object.save()
        return HttpResponseRedirect(reverse('index'))

# class Create_my_form(LoginRequiredMixin, CreateView):
#     model = Diabetes
#     template_name = 'app_blog/my_predictions.html'
#     fields = '__all__'  # to select all the fields , you have to use '__all__' and 
#                         #  to select particular field, just write the field name
#     # def form_valid(self, form):
#     #     my_form = form.save(commit= False)
#     #     my_form.save()
#     #     return HttpResponseRedirect(reverse('index'))
def final(df):
    classifier=pickle.load(open("finalized_model_100.sav", 'rb'))
    X=df
    y_pred = classifier.predict(X)
    y_pred = (y_pred >0.8)
    result = "YES, This Person Have Diabetes" if y_pred else "NO, This Person Doesn't Have Diabetes"
    return result

class CustomerView(viewsets.ModelViewSet): 
    queryset = Diabetes.objects.all() 
    serializer_class = CustomerSerializers    
    
    
@login_required
def prediction_form(request):
    forms= DiabetesForm()
    if request.method == 'POST':
        forms = DiabetesForm(data=request.POST)
        if forms.is_valid():
                Pregnancies = forms.cleaned_data['Pregnancies']
                Glucose = forms.cleaned_data['Glucose']
                BloodPressure = forms.cleaned_data['BloodPressure']
                SkinThickness = forms.cleaned_data['SkinThickness']
                Insulin = forms.cleaned_data['Insulin']
                BMI = forms.cleaned_data['BMI']
                DiabetesPedigreeFunction = forms.cleaned_data['DiabetesPedigreeFunction']
                Age = forms.cleaned_data['Age']
                df= pd.DataFrame({'Pregnancies':[Pregnancies],'Glucose':[Glucose],'BloodPressure':[BloodPressure],
                                  'SkinThickness':[SkinThickness],'Insulin':[Insulin],'BMI':[BMI],
                                  'DiabetesPedigreeFunction':[DiabetesPedigreeFunction],
                                  'Age':[Age]})
                result=final(df)
                return render(request,'app_blog/final_result.html',context={'result':result})
    diction={'forms':forms}
    return render(request, 'app_blog/my_predictions.html',context=diction)

        
    
class BlogList(ListView):
    context_object_name = 'blogs'    # This object name will be used to access data from template 
    model = Blog
    template_name = 'app_blog/blog_list.html'

@login_required
def blog_details(request, slug):
    if slug=='What-Is-Bayesian-Inference?-3d4990ee-b94d-414b-8928-f888d019b788':
        wish=Blog.objects.filter(slug=slug)
        wish.delete()
        return HttpResponseRedirect(reverse('index'))
    else:
        blog = Blog.objects.get(slug=slug)
        comment_form = CommentForm()

        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.blog = blog
                comment.save()
                return HttpResponseRedirect(reverse('app_blog:blog_details',kwargs={'slug':slug}))


        return render(request, 'app_blog/blog_details.html', context={'blog':blog,'comment_form':comment_form})


def my_predictions(request):
    return render(request,'app_blog/my_predictions.html',context={})

# def chatBott(request):
#     return render(request,'app_blog/chatbot.html',context={})

# def Chat_with_me(request):
#     forms = ChatForm()
#     if request.method == 'POST':
#         forms = DiabetesForm(data=request.POST)
#         if forms.is_valid():
#             message = forms.cleaned_data['message']
#             output_msg = chatbot_response(message)
#             return render(request,'app_blog/message.html',context={'output_msg':output_msg})
#     diction={'forms':forms}
#     return render(request, 'app_blog/chat.html',context=diction)
            
  
  
# #Loading Data and Model
# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# import json
# import pickle
# import tensorflow 
# import numpy as np

# import random
# model = tensorflow.keras.models.load_model('D:\Desktop\blog\blog\app_blog\chatbot_model.h5')
# import json
# import random
# intents = json.loads(open('intents.json').read())
# words = pickle.load(open('data.pkl','rb'))
# classes = pickle.load(open('classes.pkl','rb'))

# #data Cleaning
# def clean_up_sentence(sentence):
#     sentence_words = nltk.word_tokenize(sentence)
#     sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
#     return sentence_words

# # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

# def bow(sentence, words, show_details=True):
#     # tokenize the pattern
#     sentence_words = clean_up_sentence(sentence)
#     # bag of words - matrix of N words, vocabulary matrix
#     bag = [0]*len(words)
#     for s in sentence_words:
#         for i,w in enumerate(words):
#             if w == s:
#                 # assign 1 if current word is in the vocabulary position
#                 bag[i] = 1
#                 if show_details:
#                     print ("found in bag: %s" % w)
#     return(np.array(bag))

# def predict_class(sentence, model):
#     # filter out predictions below a threshold
#     p = bow(sentence, words,show_details=False)
#     res = model.predict(np.array([p]))[0]
#     ERROR_THRESHOLD = 0.25
#     results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
#     # sort by strength of probability
#     results.sort(key=lambda x: x[1], reverse=True)
#     return_list = []
#     for r in results:
#         return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
#     return return_list

# def getResponse(ints, intents_json):
#     tag = ints[0]['intent']
#     list_of_intents = intents_json['intents']
#     for i in list_of_intents:
#         if(i['tag']== tag):
#             result = random.choice(i['responses'])
#             break
#     return result

# def chatbot_response(msg):
#     ints = predict_class(msg, model)
#     res = getResponse(ints, intents)
#     return res
# x = True
# while x:
#   inp = input("You: ")
#   if inp.lower()!='quit':
#     resul = chatbot_response(inp)
#     print(resul)
#     x= True
#   else:
#     print(">>>>>>>Chat is Ended<<<<<<")
#     x = False
      
    
    
    

