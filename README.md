# Sentiment Analysis

Sentiment Analysis is the way toward deciding the opinion or sentiment a bit of content.<br> It is the field of study that breaks down individuals' conclusions, assumptions, and feelings towards elements, for example, products, individuals, issues, occasions, themes, and their qualities.<br> It mainly focuses on opinions which express positive or negative sentiments.
Machine learning is implemented to automatically decide the sentiment of the text. It is an approach to assess written or spoken language to decide whether the expression is ideal, negative, or unbiased, and to what degree. It uncovers the client's feeling about subjects going from your items and administrations to your area, your ads, or even your rivals.

# Cleaning of the Reviews:
1) Reviews are extracted from the HTML or XML files using the BeautifulSoup library.
2) Punctuations are removed from the reviews using the string substitution operation
3) The entire review is split into an array consisting of its words as individual elements
4) Removing stopwords. Stopwords are unimportant words that do not affect the sentiment of the review such as prepositions(I,we,us,etc.).

# Training Of the Model:
Mean_words[ ] consists of the list of words in each review with its corresponding sentiment.
Now, we find the count of each word in positive and negative reviews.
			The count of a word is calculated by this python code:
              wordfreq.append(wordlist.count(i))
              
From both the datasets(freq_pos.csv,freq_neg.csv) ,now we calculate goodness and badness of each word.
      Goodness=freq of that word in freq_pos/total count of the word
      Badness=freq of that word in freq_neg/total count of the word
      
# Input to the network:
Word_prob_arr[] consists of:
      (word, goodness, badness)
      
# Testing
Each of the word is checked in the word_prob_arr.csv file and if it is found, its goodness is added to sum_good and its badness is added in sum_bad.
      sum_good=sum_good+float(word_prob_arr['goodness'][j])
			sum_bad=sum_bad+float(word_prob_arr['badness'][j])
      
Thus at the end, we get the sum_good and sum_bad of the entire review.
The one which is greater will become the sentiment of the review. If sum_good is greater, then the review is classified as positive. If sum_bad is greater, it is classified as negative. Otherwise, it is taken as neutral.
These results are stored in the file find_acc.csv
