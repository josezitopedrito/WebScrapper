#!/usr/bin/env python

import sys
import os

class TfIdf:
    def __init__(self):
        self.weighted = False
        self.documents = []
        self.corpus_dict = {}

    def add_document(self, doc_name, list_of_words):
        # building a dictionary
        doc_dict = {}
        for w in list_of_words:
            doc_dict[w] = doc_dict.get(w, 0.) + 1.0
            self.corpus_dict[w] = self.corpus_dict.get(w, 0.0) + 1.0

        # normalizing the dictionary
        length = float(len(list_of_words))
        for k in doc_dict:
            doc_dict[k] = doc_dict[k] / length

        # add the normalized document to the corpus
        self.documents.append([doc_name, doc_dict])

    def similarities(self, list_of_words):
        """Returns a list of all the [docname, similarity_score] pairs relative to a
list of words.
        """

        # building the query dictionary
        query_dict = {}
        for w in list_of_words:
            query_dict[w] = query_dict.get(w, 0.0) + 1.0

        # normalizing the query
        length = float(len(list_of_words))
        for k in query_dict:
            query_dict[k] = query_dict[k] / length

        # computing the list of similarities
        sims = []
        for doc in self.documents:
            score = 0.0
            doc_dict = doc[1]
            for k in query_dict:
                if k in doc_dict:
                    score += (query_dict[k] / self.corpus_dict[k]) + (
                        doc_dict[k] / self.corpus_dict[k])
            sims.append([doc[0], score])
        


        sims.sort(reverse=True,key=getValue)

        return sims

    def get_dic(self):
        dic = {}
        for i in range(len(self.documents)):
            lista = []
            for key, value in self.documents[i][1].items():
                temp = [key,value]
                lista.append(temp)
            dic[self.documents[i][0]] = lista
        for key in dic.keys():
            dic[key].sort(reverse=True,key=getValue)
        print(dic)

def getValue(e):
    return e[1]