#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing libraries needed
import ipywidgets as widgets
from IPython.display import display
import time


# In[2]:


# Creating the function to store the questions and answers for the mini-quiz
def answer_check(question, question_input):
    if question_input == "Question-1":
        if question.value == "7":
            print("Correct Answer!")
            
        else:
            print("Incorrect Answer!")
            
    elif question_input == "Question-2":
        if question.value == "366":
            print("Correct Answer!")
            
        else:
            print("Incorrect Answer!")
def mini_quiz(question):
    if question == 'Question-1':
#         q1 = widgets.IntText(value=0, description='How many continents are there in the world?')
        q = widgets.RadioButtons(options=['4', '5', '6', '7'], description='How many continents are there in the world?:')
        display(q)
        
    elif question == 'Question-2':
        q = widgets.RadioButtons(options=['364', '365', '366', '367'], description='How many days are there in a leap year?:')
        display(q)
        
    return q


# In[3]:


#Giving user an option to pick from different types of questions
question = widgets.ToggleButtons(options=['Question-1', 'Question-2'], description='Quiz:')
display(question)


# In[4]:


#Storing value of the toggle button
question_input = question.value
question_input


# In[5]:


#Calling functions to compute the questions and answers 
question = mini_quiz(question_input)


# In[6]:


answer_check(question, question_input)


# In[7]:


question = mini_quiz(question_input)


# In[8]:


answer_check(question, question_input)


# In[9]:


question = mini_quiz(question_input)


# In[10]:


answer_check(question, question_input)


# In[11]:


question = mini_quiz(question_input)


# In[12]:


answer_check(question, question_input)


# In[ ]:




