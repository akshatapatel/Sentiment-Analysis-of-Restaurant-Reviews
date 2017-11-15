import pandas as pd
import csv
from sklearn import cross_validation
'''
data=pd.read_csv("Book1_neg.csv")
words_test=[]
word_prob_arr=pd.read_csv("word_prob_arr_old.csv")
skf1 = cross_validation.StratifiedKFold(data['star_rating'],3)
print(skf1);
for train_index, test_index in skf1:
    print ("TRAIN:", train_index, "TEST:", test_index)
    fieldnames = ['Text','goodness','badness', 'actual_senti','found_senti']
    with open('find_acc.csv', 'a') as csvfile:
            writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            k=0
            for t in test_index:
                test=data["Text"][t]  
                actual_sent=data["star_rating"][t]
                #print(" text and senti at i :",test,actual_sent);
                lower_case = test.lower()
                tempwords = lower_case.split()
                words_test.append(tempwords)
                
                sum_good=0.0
                sum_bad=0.0
                flag=0
                #print(" words in t :",words_test[k]);
                #print(len(words_test[k]));
                i=0
                print("i len(k) :",i,len(words_test[k]));
                while i<len(words_test[k]):
                    j=0
                    while j<len(word_prob_arr):
                        if word_prob_arr['goodness'][j]!="goodness":
                            #print(" cdvd :",word_prob_arr['word'][j]);
                            #print("HEYY",words_test[0][i]," ",word_prob_arr['word'][j]);
                            if words_test[k][i]==word_prob_arr['word'][j]:
                                print(" IN ");
                                print(i," ",j," " ,words_test[k][i]," ",word_prob_arr['word'][j]);
                                flag=1;
                                sum_good=sum_good+float(word_prob_arr['goodness'][j])
                                sum_bad=sum_bad+float(word_prob_arr['badness'][j])
                                print(sum_good);
                                print(sum_bad);
                                break;
                        j=j+1
                    i=i+1
                k=k+1
                if sum_good>sum_bad:
                    found_sent="pos"
                elif sum_good<sum_bad:
                    found_sent="neg"
                else:
                    found_sent="neutral"
                print(" sent of rev :",found_sent);
                writer.writerow({'Text':data["Text"][i],'goodness':sum_good,'badness':sum_bad, 'actual_senti':actual_sent,'found_senti':found_sent})
                
    break

print(" NEG Test DOne ");
'''
data=pd.read_csv("Book1_pos.csv")
words_test=[]
word_prob_arr=pd.read_csv("word_prob_arr_old.csv")
skf1 = cross_validation.StratifiedKFold(data['star_rating'],5)
print(skf1);
for train_index, test_index in skf1:
    print ("TRAIN:", train_index, "TEST:", test_index)
    fieldnames = ['Text','goodness','badness', 'actual_senti','found_senti']
    with open('find_acc.csv', 'a') as csvfile:
            writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            k=0
            for t in test_index:
                test=data["Text"][t]  
                actual_sent=data["star_rating"][t]
                #print(" text and senti at i :",test,actual_sent);
                lower_case = test.lower()
                tempwords = lower_case.split()
                words_test.append(tempwords)
                
                sum_good=0.0
                sum_bad=0.0
                flag=0
                #print(" words in t :",words_test[k]);
                #print(len(words_test[k]));
                i=0
                print("i len(k) :",i,len(words_test[k]));
                while i<len(words_test[k]):
                    j=0
                    while j<len(word_prob_arr):
                        if word_prob_arr['goodness'][j]!="goodness":
                            #print(" cdvd :",word_prob_arr['word'][j]);
                            #print("HEYY",words_test[0][i]," ",word_prob_arr['word'][j]);
                            if words_test[k][i]==word_prob_arr['word'][j]:
                                print(" IN ");
                                print(i," ",j," " ,words_test[k][i]," ",word_prob_arr['word'][j]);
                                flag=1;
                                sum_good=sum_good+float(word_prob_arr['goodness'][j])
                                sum_bad=sum_bad+float(word_prob_arr['badness'][j])
                                print(sum_good);
                                print(sum_bad);
                                break;
                        j=j+1
                    i=i+1
                k=k+1
                if sum_good>sum_bad:
                    found_sent="pos"
                elif sum_good<sum_bad:
                    found_sent="neg"
                else:
                    found_sent="neutral"
                print(" sent of rev :",found_sent);
                writer.writerow({'Text':data["Text"][i],'goodness':sum_good,'badness':sum_bad, 'actual_senti':actual_sent,'found_senti':found_sent})
                
    break

print(" POS Test DOne ");


'''
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