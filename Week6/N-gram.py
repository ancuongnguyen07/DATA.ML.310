
import nltk
from collections import Counter


FILE_NAME = "TheStoryofAnHour-KateChopin.txt"
STOP_WORDS = "a an and as at for from in into of on or the to".split()
# print(STOP_WORDS)

contents = []
with open(FILE_NAME, mode='r', encoding='utf8') as fileObj:
    for word in nltk.wordpunct_tokenize(fileObj.read()):
        if (word not in STOP_WORDS and len(word) >= 2 and all(c.isalpha() 
            for c in word)):
            contents.append(word.lower())
    
ngrams = Counter(nltk.ngrams(contents, 2))


print(ngrams[('open', 'window')] / sum(ngrams.values()))