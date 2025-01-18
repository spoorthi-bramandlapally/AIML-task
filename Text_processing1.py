#!/usr/bin/env python
# coding: utf-8

# In[2]:


def remove_punc(input_text):
    punctuation_marks=['.',',','!','@',"#",'$','%','^','&','*','(',')','[',']','/','-','+','_','`','~','"']
    output_text=""
    for char in input_text:
        if char not in punctuation_marks:
            output_text += char
    return output_text


# In[ ]:





# In[6]:


def remove_stopwords(input_text):
    stop_words=['a','p','b','c','d','g','i','k','l','n','s','o','p','w','z','x']
    output_text=""
    for char in input_text:
        if char not in stop_words:
            output_text += char
    return output_text


# In[ ]:





# In[10]:


def remove_stopwords(input_text):
    stop_words=['and','an','the','it','is','in','on','out','for','if','up','down','of','off','at','am','with','was','were','have','has','my']
    words = input_text.split()
    filtered_words=[]
    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(word)
            output_text=' '.join(filtered_words)
    return output_text


# In[ ]:





# In[14]:


def remove_stopwords(input_text):
    stop_words=['and','an','the','it','is','in','on','out','for','if','up','down','of','off','at','am','with','was','were','have','has','my']
    filtered_words=[]
    for word in input_text.split():
        if word.lower() not in stop_words:
            filtered_words.append(word)
    output_text=' '.join(filtered_words)
    return output_text
remove_stopwords("the movie was good and it is a hit")

