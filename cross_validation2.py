from subprocess import check_output
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np
import nltk
import csv
from nltk.corpus import stopwords  
def freqDpos(Text,star_rating):
    sentiment=[]
    words=[]
    mean_words=[]
    lower_case=[]
   
    #for i in range(0,6500):
    sentiment.append(star_rating);
    #print(sentiment);
    
                                                #removing html tags
    #for i in range(0,6500):                                        
    example = BeautifulSoup(Text,"lxml")
    Text=example.get_text();
        #print (data["Text"][i])
        
    #print("\nAfter removing html tags...");
    #print(data["Text"][0]);        
                       
        
                                                 #removing punctuations
    #for i in range(0,6500):
    Text= re.sub("[^a-zA-Z]"," ",Text);     
       #print (data["Text"][i])
       
    #print ("\nAfter removing punctuation...");
    #print(data["Text"][0]);    
    
    
    #print("\nAll Words..");
    
    k=0;                                         #splitting into words
    #while k < 6501:
    lower_case = Text.lower()
    tempwords = lower_case.split()
    words.append(tempwords)
       # print(words[k])
    k+=1
        
    #print("11111");
    #print(words) 
                                                #removing stopwords
    #print("\nSTOPWORDS!");
    
    #print (stopwords.words("english")) 
    stop = set(stopwords.words("english"));
    #print(stop);
    stops=[]
    w="";
    for w in stop:
        stops.append(w);
    #print("22222");
    #print(stops);
    #print("\nOnly meaningful words with sentiment...");
    #for i in range(0,6500):
    i=0;
    meaningful_words=[]
    for i in words[0]:
        #print("tttttt");
        #print(i);
        fl=0
        for j in stops:
            if i==j:
                fl=1;
                break;
        if fl==0:
            meaningful_words.append(i)
       
        #meaningful_words = [w for w in words if w not in stops]
    #print("ggggggggg");
    #print(meaningful_words);    
    mean_words.append((meaningful_words,sentiment))
    #print("mmmmm");
    #print(mean_words);
    return meaningful_words;
    #for i in range(0,5):
      #  print (mean_words[i])
   
   
                
        #wordfeatures=wordlist.keys()
       # print("hello");
        #print(wordfeatures);
        #return wordfeatures
    #print("\n HIIIIIIIII");
    #print(word_features)
        
    
def freqDneg(data):
    sentiment=[]
    words=[]
    mean_words=[]
    lower_case=[]
    splitl=0
    
    for i in range(0,1400):
        sentiment.append(data["star_rating"][i]);
    #print(sentiment);
    
                                                #removing html tags
    for i in range(0,1400):                                        
        example = BeautifulSoup(data["Text"][i],"lxml")
        data["Text"][i]=example.get_text();
        #print (data["Text"][i])
        
    #print("\nAfter removing html tags...");
    #print(data["Text"][0]);        
                       
        
                                                 #removing punctuations
    for i in range(0,1400):              
       data["Text"][i]= re.sub("[^a-zA-Z]"," ",data["Text"][i]);     
       #print (data["Text"][i])
       
    #print ("\nAfter removing punctuation...");
    #print(data["Text"][0]);    
    
    
    #print("\nAll Words..");
    
    k=0;                                         #splitting into words
    while k < 1401:
        lower_case = data["Text"][k].lower()
        tempwords = lower_case.split()
        words.append(tempwords)
       # print(words[k])
        k+=1
        
    #print(words[0]) 
                                                #removing stopwords
    #print("\nSTOPWORDS!");
    w=0
    #print (stopwords.words("english")) 
    stops = set(stopwords.words("english"))
    clean_train_reviews=[]
    
    #print("\nOnly meaningful words with sentiment...");
    
    for i in range(0,1400):
        meaningful_words = [w for w in words[i] if w not in stops]
        mean_words.append((meaningful_words,sentiment[i]))
     
    #for i in range(0,5):
    #    print (mean_words[i])
    
    def get_words_in_rev(rev):
        all_words=[]
        for(words,sentiment) in rev:
            all_words.extend(words)
        return all_words
        
    def get_word_features(wordlist):
      #  print("\n 222222");
      #  print(wordlist);
        #wordlist=nltk.FreqDist(wordlist)
        
        print("\nFREQ DISTR :");
        wordfreq=[]
        for i in wordlist:
            wordfreq.append(wordlist.count(i))
        fieldnames = ['word', 'freq']
        
            
        with open('freq_neg.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(0,1400):
                print(wordlist[i], wordfreq[i]);
                writer.writerow({'word':wordlist[i], 'freq':wordfreq[i]})
        #wordfeatures=wordlist.keys()
       # print("hello");
        #print(wordfeatures);
        #return wordfeatures
    
    word_features=get_word_features(get_words_in_rev(mean_words))
    print("\n HIIIIIIIII");
    #print(word_features)    
  

