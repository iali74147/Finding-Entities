
#Removing Stop Words

tweet = """I’m amazed how often in practice, not only does a Acme Corp @huggingface NLP model solve your problem, but one of their public finetuned checkpoints,
 is good enough for the job. Both impressed, and a little disappointed how rarely I get to actually train a model that matters :("""

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
stop_words = stopwords.words('english')

stop_words = set(stop_words)
tweet = tweet.lower().split()

tweet_no_stopwords = [word for word in tweet if word not in stop_words]

print("With StopWords: ", tweet)
print("Without StopWords", tweet_no_stopwords)

#Stemming

stemmer = PorterStemmer()
stemmer_word = [stemmer.stem(word) for word in tweet_no_stopwords]
print("Stemmer: ", stemmer_word)

#Lemmatization

nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

lemmatizer = WordNetLemmatizer()
lema1 = [lemmatizer.lemmatize(word) for word in tweet_no_stopwords]
lema2 = [lemmatizer.lemmatize(word, wordnet.VERB) for word in tweet_no_stopwords]
print("Lemmatization: ", lema2)

