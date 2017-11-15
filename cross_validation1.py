from subprocess import check_output
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np
import nltk
import csv
import cross_validation2
from sklearn import cross_validation
from nltk.corpus import stopwords            # Import the stop word list

data=pd.read_csv("Book1_neg.csv")
skf1 = cross_validation.StratifiedKFold(data['star_rating'],3)
print(skf1);
mean_words_neg0=[]
mean_words_neg1=[]
mean_words_neg2=[]
print("\n NEGATIVE:");
n=0;
for train_index, test_index in skf1:
    n=n+1
    print ("TRAIN:", train_index, "TEST:", test_index)
    '''
    for i in train_index:
        if n==1:
            mean_words_neg0.append(cross_validation2.freqDpos(data['Text'][i],data['star_rating'][i]))
        elif n==2:
            mean_words_neg1.append(cross_validation2.freqDpos(data['Text'][i],data['star_rating'][i]))
        elif n==3:
            mean_words_neg2.append(cross_validation2.freqDpos(data['Text'][i],data['star_rating'][i]))
       '''
    '''
        elif n==4:
            mean_words_neg[3].append(cross_validation2.freqDpos(data['Text'][i],data['star_rating'][i]))
        elif n==5:
            mean_words_neg[4].append(cross_validation2.freqDpos(data['Text'][i],data['star_rating'][i]))
     '''
#print(mean_words_neg0);
#print(mean_words_neg1);
print("NEG DONE");      
        
mean_words_pos0=[]
mean_words_pos1=[]
mean_words_pos2=[]
mean_words_pos3=[]
mean_words_pos4=[]
data=pd.read_csv("Book1_pos.csv")
skf = cross_validation.StratifiedKFold(data['star_rating'],5)
print(skf);
mean_words_pos=[]
print("\n POSITIVE:");
n=0;
for train_index, test_index in skf:
    n=n+1
    print ("TRAIN:", train_index, "TEST:", test_index)
    '''
    for i in train_index:
        if n==1:
            mean_words_pos0.append(cross_validation2.freqDpos(data['Text'][i],data['star_rating'][i]))
        if n==2:
            mean_words_pos1.append(cross_validation2.freqDpos(data['Text'][i],data['star_rating'][i]))
        if n==3:
            mean_words_pos2.append(cross_validation2.freqDpos(data['Text'][i],data['star_rating'][i]))
        if n==4:
            mean_words_pos3.append(cross_validation2.freqDpos(data['Text'][i],data['star_rating'][i]))
        if n==5:
            mean_words_pos4.append(cross_validation2.freqDpos(data['Text'][i],data['star_rating'][i]))
    '''
#print("POS DONE");
#print(" neg0 :",mean_words_neg0);
#print(" pos0 :",mean_words_pos0);
#print(mean_words);

def get_words_in_rev(rev):
        all_words=[]
        for(words) in rev:
            all_words.extend(words)
        #print("rrrrrrrrrr");
        #print(all_words);
        return all_words
        
def get_word_features(wordlist):
      #  print("\n 222222");
      #  print(wordlist);
        #wordlist=nltk.FreqDist(wordlist)
        
    #print("\nFREQ DISTR :");
    wordfreq=[]
    for i in wordlist:
        wordfreq.append(wordlist.count(i))
        fieldnames = ['word', 'freq']
        #print("ffffffffffff");
        #print(wordlist);
    with open('freq_pos.csv', 'a') as csvfile:
        writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
            #for i in range(0,6500):
        i=0;
        print("Before for:::");
        for i in range(0,len(wordlist)):
            print(wordlist[i], wordfreq[i]);
            writer.writerow({'word':wordlist[i], 'freq':wordfreq[i]})
                
def get_word_features1(wordlist):
      #  print("\n 222222");
      #  print(wordlist);
        #wordlist=nltk.FreqDist(wordlist)
        
    #print("\nFREQ DISTR :");
    wordfreq=[]
    for i in wordlist:
        wordfreq.append(wordlist.count(i))
        fieldnames = ['word', 'freq']
        #print("ffffffffffff");
        #print(wordlist);
    with open('freq_neg.csv', 'a') as csvfile:
        writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
            #for i in range(0,6500):
        i=0;
        print("Before for:::");
        for i in range(0,len(wordlist)):
            print(wordlist[i], wordfreq[i]);
            writer.writerow({'word':wordlist[i], 'freq':wordfreq[i]})
print("1234");           
#get_word_features1(get_words_in_rev(mean_words_neg0))
print(" POS ");
#get_word_features(get_words_in_rev(mean_words_pos0))
print("4567");

        
    
    
#freqD.freqDpos(data)
'''
data1=pd.read_csv("Book1_neg.csv")
skf = cross_validation.StratifiedKFold(data1['star_rating'],5)
print(skf);
print("\n NEGATIVE:");
for train_index, test_index in skf:
    print ("TRAIN:", train_index, "TEST:", test_index)
#freqD.freqDneg(data1)
'''

  
 
        
    
