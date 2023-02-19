
import PyPDF2
from textblob import Word

def punctuation_check(word):
    flag=0
    if (len(word)>1) and (word[-1].isalnum()):
        flag=0
    elif (len(word)>1):
        flag=1

    if flag==0:
        return ""
    else:
        return word[-1]

def correct_word_spelling(word):
    word = Word(word)
    result = word.spellcheck()
    if result[0][0] != word:
        return result[0][0]
        '''print("Did you mean",result[0][0],"?")'''
    else:
        return word

fileObj = open('/home/charumathi/Documents/blog/website/spell.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(fileObj,strict=False)
n = pdfReader.numPages
dataStr = ''
WordsL = []
tb = None

for eachPage in range(0, n):
    pageObj = pdfReader.getPage(eachPage)
    dataStr = pageObj.extractText()
    WordsL = dataStr.split(sep=' ')
    correctedWordsL = []
    for eachWord in WordsL:
        correctedWord = correct_word_spelling(eachWord)
        if (len(correctedWord)>0 and correctedWord[-1].isalnum==True):
            p = punctuation_check(eachWord)
            correctedWord=correctedWord+p
        correctedWordsL.append(correctedWord)
    correctedStr = ' '.join(correctedWordsL)
    print(correctedStr)