"""
Created on Mon Nov  8 23:11:32 2021

@author: shubh
"""
import nltk
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
def txt_clean(word_list, stopwords_list, min_len):
    clean_words = []
    vocab = []
    for line in word_list:
        parts = line.strip().split()
        for word in parts:
            word_l = word.lower()
            if word_l not in stopwords_list:
                if word_l.isalpha():
                    if len(word_l) > min_len:
                        clean_words.append(word_l)
                        if word_l not in vocab:
                            vocab.append(word_l)
    return clean_words, vocab
txt_file1 = open('Pros.txt','r', encoding='utf8')
txt_file2 = open('Cons.txt','r', encoding='utf8')
stopwords_file = open('stopwords_en.txt','r', encoding='utf8')
stopwords = []
txt_words1 = []
txt_words2 = []
for word in stopwords_file:
    stopwords.append(word.strip())
    stopwords.extend(['tablets', 'teacher', 'print', 'better', 'compared', 'weight', 'lost', 'including',
                      'likely' 'text', 'device', 'names', 'textbook','.', '!', ',','?'])
for word in txt_file1:
    txt_words1.append(word.strip())
for word in txt_file2:
    txt_words2.append(word.strip())
min_word_len = 3
clean_words1, vocabulary1 = txt_clean(txt_words1,stopwords, min_word_len)
clean_words2, vocabulary2 = txt_clean(txt_words2,stopwords, min_word_len)
all_words_string1 = ' '.join(clean_words1)
all_words_string2 = ' '.join(clean_words2)
analyzer = SentimentIntensityAnalyzer()
clean_text_str1 = ' '.join(all_words_string1)
vad_sentiment = analyzer.polarity_scores(clean_text_str1)
pos = vad_sentiment ['pos']
neg = vad_sentiment ['neg']
neu = vad_sentiment ['neu']
print ('\nThe following is the distribution of the sentiment for the Pros -','\n',all_words_string1)
print ('\n It is positive for', '{:.1%}'.format(pos))
print ('\n It is negative for', '{:.1%}'.format(neg))
print ('\n It is neutral for', '{:.1%}'.format(neu), '\n')
clean_text_str2 = ' '.join(all_words_string2)
vad_sentiment = analyzer.polarity_scores(clean_text_str2)
pos = vad_sentiment ['pos']
neg = vad_sentiment ['neg']
neu = vad_sentiment ['neu']
print ('\nThe following is the distribution of the sentiment for the Cons :-','\n',all_words_string2)
print ('\n It is positive for', '{:.1%}'.format(pos))
print ('\n It is negative for', '{:.1%}'.format(neg))
print ('\n It is neutral for', '{:.1%}'.format(neu), '\n')
bigrammed1 = list(nltk.bigrams(clean_words1))
print ('The following are the bigrams extracted from the Pros:')
print()
print (bigrammed1)
print()
bigrammed2 = list(nltk.bigrams(clean_words2))
print ('The following are the bigrams extracted from the Cons:')
print()
print (bigrammed2)
wordcloud1 = WordCloud(max_font_size=61, max_words=1000, background_color="white").generate(all_words_string1)
plt.figure()
plt.imshow(wordcloud1, interpolation='bicubic')
plt.axis("off")
wordcloud2 = WordCloud(max_font_size=61, max_words=1000, background_color="white").generate(all_words_string2)
plt.figure()
plt.imshow(wordcloud2, interpolation='bicubic')
plt.axis("off")
plt.show()
