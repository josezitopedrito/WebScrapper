import re
from tfidf import TfIdf
import os

def aplicarAlg ():
    filesP = os.listdir('paginas')
    filesA = os.listdir('artigos')
    table = TfIdf()

    for i in filesP:
        with open('paginas/{}'.format(i),'r') as content:
            table.add_document(i,re.sub(r'[\W]',' ',content.read()).split())

    for i in filesA:
        with open('artigos/{}'.format(i),'r') as content:
            table.add_document(i,re.sub(r'[\W]',' ',content.read()).split())

    print(table.similarities(['href','a']))

def main():
    aplicarAlg()

if __name__== "__main__":
   main()