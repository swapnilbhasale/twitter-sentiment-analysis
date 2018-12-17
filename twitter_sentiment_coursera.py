punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
#print(positive_words)

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def strip_punctuation(word):
    for p in punctuation_chars:
        if p in word:
            word = word.replace(p, '') #replace return a copy of the string
    return word
def get_neg(sentence):
    nWords = 0
    words = sentence.split()
    for w in words:
        tmp = strip_punctuation(w)
        words.remove(w)
        words.append(tmp)
    for w in negative_words:
        if w in words:
            nWords += 1
    return nWords
def get_pos(sentence):
    pWords = 0
    words = sentence.split()
    for w in words:
        tmp = strip_punctuation(w)
        words.remove(w)
        words.append(tmp)
    for w in positive_words:
        if w in words:
            pWords += 1
    return pWords

result = []
with open('project_twitter_data.csv', 'r') as fileobj:
    
    sentences = fileobj.readlines()
    
    for s in sentences[1:]:
        pWords,nWords = 0,0
        parts = s.split(',')
        pWords += get_pos(parts[0])
        nWords += get_neg(parts[0])
        #print(s)
        
        result.append("{},{},{},{},{}".format(parts[1].strip(),parts[2].strip(),pWords,nWords,pWords-nWords))

with open('resulting_data.csv', 'w') as fileobj:
    fileobj.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    fileobj.write('\n')
    for r in result:
        fileobj.write(r)
        fileobj.write('\n')
 
