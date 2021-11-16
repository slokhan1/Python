# import the libraries
import bs4 as bs
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Getting the content
body = requests.get('https://www.foxnews.com/')
soup = bs.BeautifulSoup(body.content,'html.parser')

# Get the heading/headlines
empty = []
words = []
print()
print("Following are the headlines:")
print()
print (soup.title.string, '\n')
for paragraph in soup.find_all('a'):
    empty.append(paragraph.text)
    print(paragraph.text, '\n')

# Tranforming heading/headlines into list
for i in range(0,len(empty)):
    line = empty[i].split()
    for j in range(0,len(line)):
        words.append(line[j])

# Cleaning a files for words
def txt_clean(word_list, stopwords_list):
    clean_words = []
    vocab = []
    for line in word_list:
        parts = line.strip().split() #stripping and splitting the text
        for word in parts:
            word_l = word.lower() #lowering the content of text file
            if word_l not in stopwords_list: #removing the words not in stopwords file
                if word_l.isalpha():
                        clean_words.append(word_l) #appending the list
                        if word_l not in vocab:
                            vocab.append(word_l)
    return clean_words, vocab

# Opening a stopwords file
stopwords_file = open('stopwords_en.txt','r', encoding='utf8')
stopwords = []

# Removing words from stopwords list
for word in stopwords_file:
    stopwords.append(word.strip())
clean_words, vocabulary = txt_clean(words,stopwords)
all_words_string = ' '.join(clean_words) #joining all the clean texts

# Printing the Sentiment
SID_obj = SentimentIntensityAnalyzer()
# Calculating a polarity score which gives us a sentiment dictionary
polarity_dict = SID_obj.polarity_scores(all_words_string)
print("Polarity of Headlines is as follows :")
print()
print("Polarity percentage of headlines is", polarity_dict['neg'] * 100, "% Negative")
print("polarity percentage of headlines is", polarity_dict['neu'] * 100, "% Neutral")
print("polarity percentage of headlines is", polarity_dict['pos'] * 100, "% Positive")
print()
print("Overall polarity percentage of sentence is", end=" : ")
# Calculating overall sentiment by compound score
if polarity_dict['compound'] >= 0.05:
    print("Positive")
elif polarity_dict['compound'] <= - 0.05:
    print("Negative")
else:
    print("Neutral")
print()

# To find most positive and negative sentiment
positive_counts = Counter()
negative_counts = Counter()
total_counts = Counter()

for i in range(len(clean_words)):
    for word in clean_words[i].lower().split(" "):
        positive_counts[word] += 1
        total_counts[word] += 1
print('The 3 most positive sentiments are:')
print(positive_counts.most_common()[0:3])
print()
for i in range(len(clean_words)):
    for word in clean_words[i].lower().split(" "):
        negative_counts[word] -= 1
        total_counts[word] -= 1
print('The 3 most negative sentiments are:')
print(negative_counts.most_common()[0:3])
print()

# Creating a Bigram
bigram = list(nltk.bigrams(clean_words))
print("Following are the Bigrams:")
print(bigram)
print()

# Bigrams of 2 words appearing together more than 2 times in the whole text
d = Counter(bigram)
new_list = list([item for item in d if d[item] > 2])
print("Bigram of words appearing for more than 2 times are:")
print()
print(new_list)
print()

# Printing Bigrams with underscore
new_words = ['_'.join(word) for word in new_list]
print("New Bigrams list is:")
print(new_words)
print()

# Merging the list of single words with the list of bigrams
merge = clean_words + new_words
print('New Merged list of single words with the list of bigrams is:')
print(merge)
print()

#Creating a Wordcloud
wc = " ".join(merge)
wordcloud = WordCloud(max_font_size=60, max_words=200, background_color="white").generate(wc)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
