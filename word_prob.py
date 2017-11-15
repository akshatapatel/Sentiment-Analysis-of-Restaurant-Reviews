import numpy as np
import pandas as pd
import csv
print("HI");
data_neg=pd.read_csv("freq_neg.csv")
#print(data_neg);
word_prob_arr=[]
data_pos=pd.read_csv("freq_pos.csv")
#for j in range(0,6400): 

fieldnames = ['word', 'goodness','badness'] 
with open('word_prob_arr.csv', 'a') as csvfile:
    writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for j in range(0,len(data_pos)):
        if data_pos["freq"][j]!="freq":
            comp_word=data_pos["word"][j]
            print(comp_word);
            print(" j :",j);
            for i in range(0,len(data_neg)):
                if data_neg["freq"][i]!="freq":
                    print(" i :",i);
                    print(data_neg["word"][i]);
                    if comp_word==data_neg["word"][i]:
                        add_freq=int(data_pos["freq"][j])+int(data_neg["freq"][i])
                        print(" data pos freq : ",data_pos["freq"][j])
                        print(" data neg freq : ",data_neg["freq"][i])
                        print(add_freq);
                        goodness=(int(data_pos["freq"][j]))/(add_freq)
                        badness=(int(data_neg["freq"][i]))/(add_freq)
                        word_prob_arr.append((comp_word,goodness,badness))
                        writer.writerow({'word':comp_word, 'goodness':goodness,'badness':badness})
                        break;
#print(word_prob_arr);
np.savetxt("word_prob_arr.txt",word_prob_arr,fmt="%s",delimiter="__");
print("Training Done");
            #training complete
            
'''            
words_test=[]
test1=pd.read_csv("Book1.csv")
for i in range(0,5):
    test=test1["Text"][i]  
    actual_sent=test1["star_rating"][i]                      
    #test="1 check-in Having first tried only the bread that was given to me on a food truck tour, I was so happy that I finally got around to coming here. Very limited indoor seating, especially since this was a very chilly, cloudy, yucky Saturday morning, and my friend and I ended up having to sit outside. It was difficult to decide among all of the beautiful options, but eventually we decided to split an almond macaroon, a raspberry pistachio pastry and a lemon blueberry scone. Everything was perfect and beautiful! The coffee, however, is where it fell flat for me. I ordered an almond milk latte, and while it got the job done, I would not go back for espresso beverages alone. However, I am completely smitten with this place. Raspberry pistachio pastry, almond macaroon, and a blueberry lemon scone"
    lower_case = test.lower()
    tempwords = lower_case.split()
    words_test.append(tempwords)
    #print(words_test);  
    i=0
    sum_good=0
    sum_bad=0
    flag=0;
    while i<len(words_test[0]):
        j=0
        while j<len(word_prob_arr):
            #print("HEYY",words_test[0][i]," ",word_prob_arr[j][0]);
            if words_test[0][i]==word_prob_arr[j][0]:
                #print(i," ",j," " ,words_test[0][i]," ",word_prob_arr[j][0]);
                flag=1;
                sum_good=sum_good+word_prob_arr[j][1]
                sum_bad=sum_bad+word_prob_arr[j][2] 
                break;
            j=j+1
        i=i+1
    print("The actual sentiment was ",actual_sent);
    print("The sum_good is ",sum_good);
    print("The sum_bad is ",sum_bad);
    if sum_good>sum_bad:
        print("The sentence is positive\n");
    elif sum_good<sum_bad:
        print("The sentence is negative\n");
    else:
        print("The sentence is neutral\n");
''' 
