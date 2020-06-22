import re
from tfidf import TfIdf
import os
import fileinput
import webbrowser

def aplicarAlg ():
    # filesP = os.listdir('paginas')
    filesA = os.listdir('artigos')
    table = TfIdf()

    # for i in filesP:
    #     with open('paginas/{}'.format(i),'r') as content:
    #         table.add_document(i,re.sub(r'[\W]',' ',content.read()).split())

    for i in filesA:
        with open('artigos/{}'.format(i),'r') as content:
            table.add_document(i,re.sub(r'[\W]',' ',content.read()).split())

    word = 0
    nword = 0
    narray = []
    print('Indique quantas palavras quer comparar:')
    for line in fileinput.input():
        if(word == 0):
            if(line.replace("\n","").isnumeric() and int(line) > 1):
                nword = int(line)
                word += 1
            else:
                print('Digite um número maior que 1')
        elif(word < nword):
            narray.append(line.replace("\n",""))
            word += 1
        else:
            narray.append(line.replace("\n",""))
            print(narray)
            fTDIDF = open('output' + narray[0] + '.html','w+')
            fTDIDF.write('<h2>Resultados da aplicação do algoritmo:<h2>')
            for s in table.similarities(narray):
                fTDIDF.write('<p><h5>' + s[0] + ' -> ' + str(s[1]) + '</h5></p>')

            new = 2 # open in a new tab, if possible
            url = "file:///home/ze/SPLN/WebScraper/output" + narray[0] + "%0A.html"
            webbrowser.open(url,new=new)
            word = 0

def main():
    aplicarAlg()

if __name__== "__main__":
   main()