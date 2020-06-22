import fileinput
from tfidf import TfIdf
import os
import re
import webbrowser

def menu():
    print("Que deseja fazer?")
    print("1 - Consultar a informação do site do jornal ABola")
    print("2 - Aplicar o algoritmo do TFIDF")
    print("3 - Sair")
    word = 0
    nword = 0
    narray = []
    for line in fileinput.input():
        if line.replace("\n","") == "1":
            os.system('python3 web_scraper.py')
            print("Que deseja fazer?")
            print("1 - Consultar a informação do site do jornal ABola")
            print("2 - Aplicar o algoritmo do TFIDF")
            print("3 - Sair")
        elif (line.replace("\n","") == "2") or (word > 0):
            if word == 0:
                if(os.path.isdir("artigos") == False):
                    print('Necessita de gerar primeiro o conteúdo. Escolha a opção 1')
                    print("Que deseja fazer?")
                    print("1 - Consultar a informação do site do jornal ABola")
                    print("2 - Aplicar o algoritmo do TFIDF")
                    print("3 - Sair")
                else:
                    filesA = os.listdir('artigos')
                    table = TfIdf()
                    for i in filesA:
                        with open('artigos/{}'.format(i),'r') as content:
                            table.add_document(i,re.sub(r'[\W]',' ',content.read()).split()) 
                    word += 1
                    print('Indique quantas palavras quer comparar:')
            elif(word == 1):
                if(line.replace("\n","").isnumeric() and int(line) > 1):
                    nword = int(line)
                    word += 1
                else:
                    print('Digite um número maior que 1')
            elif(word > 1) and (word <= nword):
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
                url = "file:///home/ze/SPLN/WebScraper/output" + narray[0] + ".html"
                webbrowser.open(url,new=new)
                word = 0
                nword = 0
                narray = []
                print("Que deseja fazer?")
                print("1 - Consultar a informação do site do jornal ABola")
                print("2 - Aplicar o algoritmo do TFIDF")
                print("3 - Sair")
        elif (line.replace("\n","") == "3") and (word == 0):
            print("Obrigado pela sua visita")
            fileinput.close()


def main():
    menu()

if __name__== "__main__":
   main()