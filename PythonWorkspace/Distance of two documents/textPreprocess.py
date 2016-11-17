# In this module we provided text pre-process functions which include:
# 1.Open & read files into dictionary structure with error catch.
# 2.Provide
#   -How many words in documents.
#   -Show all words which in documents by list in form.
#   -Give occurences of a specified word in dict(return zero if word not in dict).
#   -Provide the model of documents from the perspective of document vector.
import numpy as np


class Documents(object):
    def __init__(self, document):
        self.dict = {}
        self.vlist = []  # vlist is a list which contains only values of occurences of words in the document.
        self.model = 0
        self.spliteddoc = []
        self.document =document
        self.lines = ''
        try:    # Trying to get a list which contains all  words of given document.
            with open(self.document, 'r') as foo:
                # read whole files as a string which contained in list,
                # and split such string into another list contains dispersed words.
                for line in foo.readlines():
                    self.lines += line
                self.spliteddoc = self.lines.split()
        except IOError:
            print('Can not open file: ' + str(self.document))
        # Turn list of words into dictionary.
        # Each key-value pair contained in the dict must be self.dic['word'] = occurence of word
        for word in self.spliteddoc:
            self.dict[word] = self.dict.get(word, 0) + 1

    # Show all words in document
    def showallwords(self):
        print('File ' + str(self.document) + ' contains words: ' + str(self.dict.keys()))

    def occurence(self, word):
        print('Word ' + word + ' occured ' + str(self.dict.get(word, 0)) + ' times.')

    def returnmodel(self):
        self.vlist = np.array(self.dict.values())
        self.model = np.sqrt(self.vlist.dot(self.vlist))
        return self.model

    def getwords(self):
        return self.dict.keys()

    def getoccurence(self, word):
        return self.dict.get(word, 0)