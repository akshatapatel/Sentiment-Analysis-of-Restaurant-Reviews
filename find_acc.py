import pandas as pd
print("HI");
data1=pd.read_csv("acc1.csv")
i=0
n=0
acc=0
tn=0
tp=0
t=0
for i in range(0,len(data1)):
    if data1['goodness'][i]!="goodness":
        #print("in");
        
        
        if str(data1['actual_senti'][i])!="nan":
            n=n+1
            #print(type(data1['actual_senti'][i]))
            #print(data1['actual_senti'][i],data1['found_senti'][i]);
            if data1['actual_senti'][i]=="1":
                if data1['found_senti'][i]=="1":
                    #print("hi");
                    tn=tn+1;
            elif data1['actual_senti'][i]=="2":
                if data1['found_senti'][i]=="2":
                    #print("hi");
                    tp=tp+1;
            elif data1['actual_senti'][i]=="0":
                if data1['found_senti'][i]=="0":
                    #print("hi");
                    t=t+1;
print " tn ",tn;
print " tp ",tp;
print " t ",t;
print " n ",n;
acc=float(float(tp+tn+t)/float(n));
print "Accuracy is :",(acc*100);
    