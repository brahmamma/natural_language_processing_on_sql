# -*- coding: utf-8 -*
import importlib
import sys
import unicodedata

importlib.reload(sys)

class StopwordFilter:
    
    def __init__(self):
        self.list = []
    
    def add_stopword(self, word):
        self.list.append(word)

    def get_stopword_list(self):
        return self.list
    
    def filter(self, sentence):
        tmp_sentence = []
        for word in sentence:
            word = self.remove_accents(word).lower()
            if word not in self.list:
                tmp_sentence.append(word)
        return tmp_sentence

    def remove_accents(self, string):
        nkfd_form = unicodedata.normalize('NFKD', str(string,'utf-8'))
        return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

    def load(self, lang):
        with open('./stopwords/' + lang + '.txt') as f:
            lines = f.read().split('\n')
            for word in lines:
                stopword = self.remove_accents(word).lower()
                self.list.append(stopword)
