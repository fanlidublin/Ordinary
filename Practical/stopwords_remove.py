import nltk
from nltk.corpus import stopwords

stop = stopwords.words('english')
text = open('/Users/fan/Desktop/pra4.txt')
rawtext = text.read()
[i for i in rawtext.split() if i not in stop]


