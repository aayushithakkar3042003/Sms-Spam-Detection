import re
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
import requests
from bs4 import BeautifulSoup
from fastpunct import FastPunct
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf

fastpunct = FastPunct()

from nltk import pos_tag
print("If you want to write your own paragraph press 1.")
print("if you want paragraph form for summarizing press 2 .")
que1 = int(input("enter a number: "))
if que1==1:
    text = input("Write the sentence for summarizzing : ")
    

    def summarize(text):
        words = word_tokenize(text)
        
        tg = pos_tag(words)
        print("Parts of speech\n")
        # for w in tg:
        #     print(w)

        
        stopwords1 = set(stopwords.words('english'))
        filtered_words = []
        for word in words:
            if word.lower() not in stopwords1:
                filtered_words.append(word)
        return " ".join(filtered_words)
    c= fastpunct.punct(text)
    summary = summarize(c)
    
    print("summary = ",summarize(c))
elif que1==2:
    
    url1 = input("please give me a link . ")
    def link(url1):
        
        response = requests.get(url1)
        if response.status_code==200:
            print("succesfully fetched the web page!")
            
        else:
            print(f"failed to fetch the web page .Staus code : ",response.status_code)
            return
        soup = BeautifulSoup(response.text,'html.parser')
        paragraphs = soup.find_all('p')
        
        filtered_words =[]
        for para in paragraphs:
            wr = word_tokenize(para.text)
            tg = pos_tag(wr)
            stopwords1 = set(stopwords.words('english'))
            
            for word in wr:
                if word.lower() not in stopwords1:
                    filtered_words.append(word)

            cleaned_text = re.sub(r'[^a-zA-Z\s]', '', ' '.join(filtered_words))
        return cleaned_text
    summary = link(url1)
    print("summary of web paragraphs : ",summary)
else:
    print("invalid input.")
    
        