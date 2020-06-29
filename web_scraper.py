#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import os
import webbrowser

source = requests.get('https://www.abola.pt/').content
soup = BeautifulSoup(source,'html.parser')

header_title = soup.find_all("div",'slice-header-title')
collection_title = soup.find_all("div",'collection_header')

ePicksCont = soup.find_all("div",'field-item')

path = "paginas"

exists = 0

try:
    os.mkdir(path)
except OSError:
    exists = 1
    print ("Directory %s already exists" % path)
else:
    exists = 0
    print ("Successfully created the directory %s" % path)

path2 = "artigos"

try:
    os.mkdir(path2)
except OSError:
    print ("Directory %s already exists" % path2)
else:
    print ("Successfully created the directory %s" % path2)

#HOMEPAGE

fhome = open("paginas/homepage.html",'w+')

fhome.write('<h1>Homepage</h1><br>')
fhome.write('<p><h4>Que deseja consultar?</h4></p>')
fhome.write('<p><a href="noticiasPrincipais.html"><h5>Notícias Principais</h5></a></p>')
fhome.write('<p><a href="noticiasEmDestaque.html"><h5>Notícias Em Destaque</h5></a></p>')
fhome.write('<p><a href="noticiasNacionais.html"><h5>Notícias a Nível Nacional</h5></a></p>')
fhome.write('<p><a href="noticiasInternacionais.html"><h5>Notícias a Nível Internacional</h5></a></p>')
fhome.write('<p><a href="noticiasModalidades.html"><h5>Notícias de Outras Modalidades</h5></a></p>')
fhome.write('<p><a href="noticiasEconomia.html"><h5>Notícias de Economia Futebolística</h5></a></p>')
fhome.write('<p><a href="noticiasMotores.html"><h5>Notícias Relativas a Desportos Motorizados</h5></a></p>')
fhome.write('<p><a href="noticiasABolaEMinha.html"><h5>Notícias da Secção A Bola É Minha</h5></a></p>')
fhome.write('<p><a href="noticiasNaoDesportivas.html"><h5>Notícias Não Desportivas</h5></a></p>')
fhome.write('<p><a href="seccaoDeJogos.html"><h5>Jogos Disponíveis No Website</h5></a></p>')
fhome.write('<p><a href="noticiasBrasileiras.html"><h5>Notícias Relativas Ao Futebol Brasileiro</h5></a></p>')
fhome.write('<p><a href="noticiasAfricanas.html"><h5>Notícias Relativas Ao Futebol Africano</h5></a></p>')
fhome.write('<p><a href="rubricasOnline.html"><h5>Rúbricas No Jornal Online</h5></a></p>')
fhome.write('<p><a href="noticiasCelebridades.html"><h5>Notícias De Celebridades</h5></a></p>')
fhome.write('<p><a href="noticiasAutomóveis.html"><h5>Notícias De Automóveis</h5></a></p>')

fhome.write('<p><h3>Notícias de clubes</h3></p>')

fhome.write('<p><a href="noticiasClubesPrimeiraLiga.html"><h5>Notícias de Clubes da Primeira Liga</h5></a></p>')

fhome.write('<p><a href="noticiasClubesSegundaLiga.html"><h5>Notícias de Clubes da Segunda Liga</h5></a></p>')

fhome.write('<p><a href="noticiasClubesLigaInglesa.html"><h5>Notícias de Clubes da Liga Inglesa</h5></a></p>')

fhome.write('<p><a href="noticiasClubesLigaEspanhola.html"><h5>Notícias de Clubes da Liga Espanhola</h5></a></p>')

fhome.write('<p><a href="noticiasClubesLigaItaliana.html"><h5>Notícias de Clubes da Liga Italiana</h5></a></p>')

fhome.write('<p><a href="noticiasClubesLigaAlema.html"><h5>Notícias de Clubes da Liga Alema</h5></a></p>')

fhome.write('<p><a href="noticiasClubesLigaFrancesa.html"><h5>Notícias de Clubes da Liga Francesa</h5></a></p>')

fhome.write('<p><a href="noticiasClubesLigaBrasileira.html"><h5>Notícias de Clubes da Liga Brasileira</h5></a></p>')

#CLUB SECTION GLOBAL VARIABLES

linkGeral = 'https://www.abola.pt/Clubes/1/'

soupClubesPrimeiraLiga = []
soupClubesSegundaLiga = []
soupClubesLigaInglesa = []
soupClubesLigaEspanhola = []
soupClubesLigaItaliana = []
soupClubesLigaAlema = []
soupClubesLigaFrancesa = []
soupClubesLigaBrasileira = []
primeiraLigaNums = [3,5,4,37,40,43,44,45,47,48,1523,1367,143,228,149,1225,152,1313]
segundaLigaNums = [41,1227,145,144,1524,148,36,1311,39,153,1315,1314,1309,162,1031,1834,1526,1830]
ligaInglesaNums = [1231,1232,1543,1228,1243,1763,1247,1229,1230,1240,1245,1237,1238,1244,1233]
ligaEspanholaNums = [1252,1261,1264,1249,1262,1267,1266,1248,1250,1258,1259,1253,1254,1255,1263,1260]
ligaItalianaNums = [1277,1278,1276,1268,1282,1280,1279,1269,1284,1270,1273,1286,1285,1283,1274,1275,1281]
ligaAlemaNums = [1288,1289,1332,1462,1325,1335]
ligaFrancesaNums = [1339,1338,1437,1292,1544]
ligaBrasileiraNums = [1751,1303,1740,1746,1744,1641,1745,1750,1749,1754,1739,1753,1742,1755,1752,1743]

#mainPage(ficheiro para onde escreve,array de notícias,título da secção): função que vai buscar o conteúdo dos artigos que se encontram
#na página principal d'ABola e cria páginas para cada um deles
def mainPage(file,array,title):
    i = 1
    file.write(title)
    for inset in array:
        #LINK DESTE HEADLINE
        link_slide = 'https://www.abola.pt' + inset['href']
        #TÍTULO DESTE HEADLINE
        infos = inset.find_all('span')
        file.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
        n = 0
        for info in infos:
            file.write(info.text + " ")
            if n == 0 :
                file.write('</a></h3><p></p>')
            elif n == 2:
                break
            n+=1

        #ARTIGO
        sourceEstrelas = requests.get(link_slide).content
        soupEstrelas = BeautifulSoup(sourceEstrelas,'html.parser')
        art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
        if(soupEstrelas.find('h3','upper')):
            artigosTitulo = soupEstrelas.find('h3','upper').text
        elif(soupEstrelas.find('h1')):
            artigosTitulo = soupEstrelas.find('h1').text
        else:
            artigosTitulo = ""
        artigosImagens = inset.find('div',True)
        artigosTexto = soupEstrelas.find('div','corpo-noticia').find_all('p')
        art1.write("<h2>" + artigosTitulo + "</h2>")
        if (artigosImagens['data-img'][0] == 'h'):
            art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
        else:
            art1.write('<img src="https:' + artigosImagens['data-img'] + '"/>')
        for p in artigosTexto:
            art1.write('<p>' + p.text + '</p>')
        i+=1

#sections: função que vai buscar o conteudo e cria as páginas relativas às secções da página principal d'ABola
def sections():
    #SECÇÃO DAS NOTÍCIAS PRINCIPAIS

    f1 = open("paginas/noticiasPrincipais.html", 'w+')

    dozeNoticias = soup.find('div','col-md-12 noticias clearfix').find('div','col-md-8 col-sm-6 col-xs-12 pad-r').find_all('a',href=True)
    dozeNoticias += soup.find('div','col-md-12 noticias clearfix').find('div',{'id':'ctl00_body_geral_rptGeralB1_ctl00_divteste'}).find_all('a',href=True)
    dozeNoticias += soup.find('div','col-md-12 noticias clearfix').find('div',{'id':'ctl00_body_geral_rptGeralB1_ctl01_divteste'}).find_all('a',href=True)
    dozeNoticias += soup.find('div','col-md-12 noticias clearfix').find('div',{'id':'divrptGeralC1'}).find_all('a',href=True)
    dozeNoticias += soup.find('div','col-md-12 noticias clearfix').find('div',{'id':'divrptGeralD1'}).find_all('a',href=True)
    dozeNoticias += soup.find('div','col-md-12 noticias clearfix').find('div',{'id':'divrptGeralD2'}).find_all('a',href=True)
    dozeNoticias += soup.find('div','col-md-12 noticias clearfix').find('div','content-box clearfix visible-lg visible-md').find_all('a',href=True)

    #allSuggestions = ePicksCont[1].find_all('div','inset_text')
    mainPage(f1,dozeNoticias,'<h2>Lista de Notícias Principais</h2>')

    #SECÇÃO EM DESTAQUE

    f2 = open("paginas/noticiasEmDestaque.html", 'w+')

    emDestaque = soup.find('section',{'id':'caixa90'}).find_all('a',href=True)

    mainPage(f2,emDestaque,'<h2>Lista de Notícias Em Destaque</h2>')

    #SECÇÃO NACIONAL

    f3 = open("paginas/noticiasNacionais.html", 'w+')

    nacional = soup.find('div',{'id':'ctl00_body_nacional_divNoticiasNacional'}).find_all('a',href=True)

    mainPage(f3,nacional,'<h2>Lista de Notícias A Nível Nacional:</h2>')

    #SECÇÃO INTERNACIONAL

    f4 = open("paginas/noticiasInternacionais.html", 'w+')

    internacional = soup.find('div',{'id':'ctl00_body_internacional_divNoticiasInternacional'}).find_all('a',href=True)

    mainPage(f4,internacional,'<h2>Lista de Notícias A Nível Internacional:</h2>')

    #SECÇÃO MODALIDADES

    f5 = open("paginas/noticiasModalidades.html", 'w+')

    modalidades = soup.find('div',{'id':'ctl00_body_modalidades_divNoticiasModalidades'}).find_all('a',href=True)

    mainPage(f5,modalidades,'<h2>Lista de Notícias Em Relações a Outras Modalidades:</h2>')

    #SECÇÃO ECONOMIA DA BOLA

    f6 = open("paginas/noticiasEconomia.html", 'w+')

    economia = soup.find('div',{'id':'ctl00_body_economico_divNoticiasEconomico'}).find_all('a',href=True)

    mainPage(f6,economia,'<h2>Lista de Notícias Em Relação à Economia Futebolistica:</h2>')

    #SECÇÃO MOTORES

    f7 = open("paginas/noticiasMotores.html", 'w+')

    motores = soup.find('div',{'id':'ctl00_body_motores_divNoticiasMotores'}).find_all('a',href=True)

    mainPage(f7,motores,'<h2>Lista de Notícias Em Relação a Desportos Motorizados:</h2>')

    #SECÇÃO A BOLA É MINHA

    f8 = open("paginas/noticiasABolaEMinha.html", 'w+')

    abolaeminha = soup.find('div',{'id':'ctl00_body_abolaeminha_divNoticiasABolaEMinha'}).find_all('a',href=True)

    mainPage(f8,abolaeminha,'<h2>Secção a bola é minha:</h2>')

    #SECÇÃO OUTROS MUNDOS

    f9 = open("paginas/noticiasNaoDesportivas.html", 'w+')

    outrosmundos = soup.find('div',{'id':'ctl00_body_mundos_divNoticiasOutrosMundos'}).find_all('a',href=True)

    mainPage(f9,outrosmundos,'<h2>Secção outros mundos:</h2>')

    #SECÇÃO JOGOS

    f10 = open("paginas/seccaoDeJogos.html", 'w+')

    jogos = soup.find('div',{'id':'ctl00_body_jogos_divNoticiasJogos'}).find_all('a',href=True)
    i = 1
    f10.write("<h2>Jogos d'A Bola:</h2>")
    for inset in jogos:
        #LINK DESTE HEADLINE
        if (inset['href'][0] == 'h'):
            link_slide = inset['href']
        else:
            link_slide = 'https:' + inset['href']
        
        #TÍTULO DESTE HEADLINE
        f10.write('<h3>Jogo ' + str(i) + ': <a href="' + link_slide + '">')
        infos = inset.find_all('span')
        n = 0
        for info in infos:
            f10.write(info.text + " ")
            if n == 0 :
                f10.write('</a></h3><p></p>')
            elif n == 2:
                break
            n+=1
        if i == 4:
            break
        i+=1
        

    #SECÇÃO RELATIVA AO BRASIL

    f11 = open("paginas/noticiasBrasileiras.html", 'w+')

    brasil = soup.find('div',{'id':'ctl00_body_brasil_divNoticiasBrasil'}).find_all('a',href=True)

    mainPage(f11,brasil,"<h2>Notícias relativas ao futebol brasileiro:</h2>")

    #SECÇÃO RELATIVA A ÁFRICA

    f12 = open("paginas/noticiasAfricanas.html", 'w+')

    africa = soup.find('div',{'id':'ctl00_body_africa_divNoticiasAfrica'}).find_all('a',href=True)

    mainPage(f12,africa,"<h2>Notícias relativas ao futebol africano:</h2>")

    #SECÇÃO RELATIVA A RÚBRICAS ONLINE

    f13 = open("paginas/rubricasOnline.html", 'w+')

    rubricas = soup.find('div',{'id':'ctl00_body_outras_divNoticiasOutras'}).find_all('a',href=True)

    mainPage(f13,rubricas,"<h2>Rúbricas online:</h2>")

    #SECÇÃO RELATIVA A ESTRELAS

    f14 = open("paginas/noticiasCelebridades.html", 'w+')

    estrelas = soup.find('div',{'id':'ctl00_body_estrelas_divNoticiasEstrelas'}).find_all('a',href=True)

    mainPage(f14,estrelas,"<h2>Notícias relativas a outras celebridades:</h2>")

    #SECÇÃO RELATIVA A AUTOMÓVEIS

    f15 = open("paginas/noticiasAutomóveis.html", 'w+')

    automoveis = soup.find('div',{'id':'ctl00_body_automoveis_divNoticiasAutomoveis'}).find_all('a',href=True)
    i = 1
    f15.write("<h2>Notícias relativas a automóveis:</h2>")
    for inset in automoveis:
        #LINK DESTE HEADLINE
        link_slide = inset['href']
        #TÍTULO DESTE HEADLINE
        infos = inset.find_all('span')
        f15.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
        n = 0
        for info in infos:
            f15.write(info.text + " ")
            if n == 0 :
                f15.write('</a></h3><p></p>')
            elif n == 2:
                break
            n+=1
        #ARTIGO
        sourceAutomoveis = requests.get(link_slide).content
        soupAutomoveis = BeautifulSoup(sourceAutomoveis,'html.parser')
        art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
        if(soupAutomoveis.find('h1',{'id':'body_Ver_lblTitulo'})):
            artigosTitulo = soupAutomoveis.find('h1',{'id':'body_Ver_lblTitulo'}).text
        else:
            artigosTitulo = ""
        artigosTexto = soupAutomoveis.find('span',{'id':'conteudo_corpoNoticia_lblCorpoNoticia'}).find_all('p')
        art1.write("<h2>" + artigosTitulo + "</h2>")
        for p in artigosTexto:
            art1.write('<p>' + p.text + '</p>')
        i+=1

#SECÇÃO DE CLUBES
#clubLinks: trata de interligar todas páginas relativas a clubes e ligas com a homepage
def clubLinks():
    fC = open("paginas/noticiasClubesPrimeiraLiga.html", 'w+')

    fC.write("<h2>Notícias relativas aos clubes da primeira liga:</h2>")

    fC.write('<p><a href="noticiasBENFICA.html"><h5>Notícias do Benfica</h5></a></p>')
    fC.write('<p><a href="noticiasFC PORTO.html"><h5>Notícias do Porto</h5></a></p>')
    fC.write('<p><a href="noticiasSPORTING.html"><h5>Notícias do Sporting</h5></a></p>')
    fC.write('<p><a href="noticiasBELENENSES.html"><h5>Notícias do Belenenses</h5></a></p>')
    fC.write('<p><a href="noticiasMARÍTIMO.html"><h5>Notícias do Maritimo</h5></a></p>')
    fC.write('<p><a href="noticiasPAÇOS DE FERREIRA.html"><h5>Notícias do Paços</h5></a></p>')
    fC.write('<p><a href="noticiasRIO AVE.html"><h5>Notícias do Rio Ave</h5></a></p>')
    fC.write('<p><a href="noticiasSC BRAGA.html"><h5>Notícias do Braga</h5></a></p>')
    fC.write('<p><a href="noticiasVITÓRIA DE GUIMARÃES.html"><h5>Notícias do Vitória Guimarães</h5></a></p>')
    fC.write('<p><a href="noticiasVITÓRIA DE SETÚBAL.html"><h5>Notícias do Vitória de Setúbal</h5></a></p>')
    fC.write('<p><a href="noticiasFAMALICÃO.html"><h5>Notícias do Famalicão</h5></a></p>')
    fC.write('<p><a href="noticiasBOAVISTA.html"><h5>Notícias do Boavista</h5></a></p>')
    fC.write('<p><a href="noticiasSANTA CLARA.html"><h5>Notícias do Santa Clara</h5></a></p>')
    fC.write('<p><a href="noticiasMOREIRENSE.html"><h5>Notícias do Moreirense</h5></a></p>')
    fC.write('<p><a href="noticiasGIL VICENTE.html"><h5>Notícias do Gil Vicente</h5></a></p>')
    fC.write('<p><a href="noticiasTONDELA.html"><h5>Notícias do Tondela</h5></a></p>')
    fC.write('<p><a href="noticiasPORTIMONENSE.html"><h5>Notícias do Portimonense</h5></a></p>')
    fC.write('<p><a href="noticiasAVES.html"><h5>Notícias do Despotivo das Aves</h5></a></p>')

    fC2 = open("paginas/noticiasClubesSegundaLiga.html", 'w+')

    fC2.write("<h2>Notícias relativas aos clubes da segunda liga:</h2>")

    fC2.write('<p><a href="noticiasACADÉMICA.html"><h5>Notícias da Académica</h5></a></p>')
    fC2.write('<p><a href="noticiasACADÉMICO.html"><h5>Notícias do Académico de Viseu</h5></a></p>')
    fC2.write('<p><a href="noticiasBENFICA B.html"><h5>Notícias do Benfica B</h5></a></p>')
    fC2.write('<p><a href="noticiasCASA PIA.html"><h5>Notícias do Casa Pia</h5></a></p>')
    fC2.write('<p><a href="noticiasCHAVES.html"><h5>Notícias do Despotivo de Chaves</h5></a></p>')
    fC2.write('<p><a href="noticiasCOVILHÃ.html"><h5>Notícias do Sporting da Covilhã</h5></a></p>')
    fC2.write('<p><a href="noticiasESTORIL.html"><h5>Notícias do Estoril</h5></a></p>')
    fC2.write('<p><a href="noticiasFARENSE.html"><h5>Notícias do Farense</h5></a></p>')
    fC2.write('<p><a href="noticiasPORTO B.html"><h5>Notícias do Porto B</h5></a></p>')
    fC2.write('<p><a href="noticiasFEIRENSE.html"><h5>Notícias do Feirense</h5></a></p>')
    fC2.write('<p><a href="noticiasLEIXÕES.html"><h5>Notícias do Leixões</h5></a></p>')
    fC2.write('<p><a href="noticiasMAFRA.html"><h5>Notícias do Mafra</h5></a></p>')
    fC2.write('<p><a href="noticiasNACIONAL.html"><h5>Notícias do Nacional</h5></a></p>')
    fC2.write('<p><a href="noticiasPENAFIEL.html"><h5>Notícias do Penafiel</h5></a></p>')
    fC2.write('<p><a href="noticiasVARZIM.html"><h5>Notícias do Varzim</h5></a></p>')
    fC2.write('<p><a href="noticiasVILAFRANQUENSE.html"><h5>Notícias do Vilafranquense</h5></a></p>')
    fC2.write('<p><a href="noticiasOLIVEIRENSE.html"><h5>Notícias do Oliveirense</h5></a></p>')
    fC2.write('<p><a href="noticiasCOVA DA PIEDADE.html"><h5>Notícias do Cova da Piedade</h5></a></p>')

    fC3 = open("paginas/noticiasClubesLigaInglesa.html", 'w+')

    fC3.write("<h2>Notícias relativas aos clubes da liga inglesa:</h2>")

    fC3.write('<p><a href="noticiasLIVERPOOL.html"><h5>Notícias do Liverpool</h5></a></p>')
    fC3.write('<p><a href="noticiasMANCHESTER CITY.html"><h5>Notícias do Manchester City</h5></a></p>')
    fC3.write('<p><a href="noticiasLEICESTER.html"><h5>Notícias do Leicester</h5></a></p>')
    fC3.write('<p><a href="noticiasCHELSEA.html"><h5>Notícias do Chelsea</h5></a></p>')
    fC3.write('<p><a href="noticiasMANCHESTER UNITED.html"><h5>Notícias do Manchester United</h5></a></p>')
    fC3.write('<p><h5>O jornal ABola não possui uma página dedicada ao Sheffield United</h5></p>')
    fC3.write('<p><a href="noticiasWOLVERHAMPTON.html"><h5>Notícias do Wolves</h5></a></p>')
    fC3.write('<p><a href="noticiasTOTTENHAM.html"><h5>Notícias do Tottenham</h5></a></p>')
    fC3.write('<p><a href="noticiasARSENAL.html"><h5>Notícias do Arsenal</h5></a></p>')
    fC3.write('<p><h5>O jornal ABola não possui uma página dedicada ao Burnley</h5></p>')
    fC3.write('<p><a href="noticiasCRYSTAL PALACE.html"><h5>Notícias do Crystal Palace</h5></a></p>')
    fC3.write('<p><a href="noticiasEVERTON.html"><h5>Notícias do Everton</h5></a></p>')
    fC3.write('<p><a href="noticiasSOUTHAMPTON.html"><h5>Notícias do Southampton</h5></a></p>')
    fC3.write('<p><a href="noticiasINGLATERRA.html"><h5>Notícias do Newcastle</h5></p>')
    fC3.write('<p><h5>O jornal ABola não possui uma página dedicada ao Brighton</h5></p>')
    fC3.write('<p><h5>O jornal ABola não possui uma página dedicada ao Watford</h5></p>')
    fC3.write('<p><a href="noticiasWEST HAM.html"><h5>Notícias do West Ham</h5></a></p>')
    fC3.write('<p><h5>O jornal ABola não possui uma página dedicada ao Bournemouth</h5></p>')
    fC3.write('<p><a href="noticiasASTON VILLA.html"><h5>Notícias do Aston Villa</h5></a></p>')
    fC3.write('<p><a href="noticiasNORWICH.html"><h5>Notícias do Norwich</h5></a></p>')

    fC4 = open("paginas/noticiasClubesLigaEspanhola.html", 'w+')

    fC4.write("<h2>Notícias relativas aos clubes da liga espanhola:</h2>")

    fC4.write('<p><a href="noticiasBARCELONA.html"><h5>Notícias do Barcelona</h5></a></p>')
    fC4.write('<p><a href="noticiasREAL MADRID.html"><h5>Notícias do Real Madrid</h5></a></p>')
    fC4.write('<p><a href="noticiasSEVILHA.html"><h5>Notícias do Sevilha</h5></a></p>')
    fC4.write('<p><a href="noticiasATLETICO MADRID.html"><h5>Notícias do Atlético Madrid</h5></a></p>')
    fC4.write('<p><a href="noticiasGETAFE.html"><h5>Notícias do Getafe</h5></a></p>')
    fC4.write('<p><a href="noticiasREAL SOCIEDAD.html"><h5>Notícias do Real Sociedad</h5></a></p>')
    fC4.write('<p><a href="noticiasVILLAREAL.html"><h5>Notícias do Villareal</h5></a></p>')
    fC4.write('<p><a href="noticiasVALÊNCIA.html"><h5>Notícias do Valência</h5></a></p>')
    fC4.write('<p><a href="noticiasGRANADA.html"><h5>Notícias do Granada</h5></a></p>')
    fC4.write('<p><a href="noticiasATHLETIC BILBAO.html"><h5>Notícias do Atlético de Bilbao</h5></a></p>')
    fC4.write('<p><a href="noticiasLEVANTE.html"><h5>Notícias do Levante</h5></a></p>')
    fC4.write('<p><h5>O jornal ABola não possui uma página dedicada ao Alavés</h5></p>')
    fC4.write('<p><a href="noticiasOSASUNA.html"><h5>Notícias do Osasuna</h5></a></p>')
    fC4.write('<p><a href="noticiasBÉTIS.html"><h5>Notícias do Bétis</h5></a></p>')
    fC4.write('<p><a href="noticiasVALLADOLID.html"><h5>Notícias do Valladolid</h5></a></p>')
    fC4.write('<p><h5>O jornal ABola não possui uma página dedicada ao Eibar</h5></p>')
    fC4.write('<p><a href="noticiasCELTA DE VIGO.html"><h5>Notícias do Celta de Vigo</h5></a></p>')
    fC4.write('<p><h5>O jornal ABola não possui uma página dedicada ao Maiorca</h5></p>')
    fC4.write('<p><h5>O jornal ABola não possui uma página dedicada ao Leganés</h5></p>')
    fC4.write('<p><a href="noticiasESPANHOL.html"><h5>Notícias do Espanhol</h5></a></p>')

    fC5 = open("paginas/noticiasClubesLigaItaliana.html", 'w+')

    fC5.write("<h2>Notícias relativas aos clubes da liga italiana:</h2>")

    fC5.write('<p><a href="noticiasJUVENTUS.html"><h5>Notícias do Juventus</h5></a></p>')
    fC5.write('<p><a href="noticiasLAZIO.html"><h5>Notícias da Lázio</h5></a></p>')
    fC5.write('<p><a href="noticiasINTER DE MILÃO.html"><h5>Notícias do Inter de Milão</h5></a></p>')
    fC5.write('<p><a href="noticiasATALANTA.html"><h5>Notícias do Atalanta</h5></a></p>')
    fC5.write('<p><a href="noticiasROMA.html"><h5>Notícias da Roma</h5></a></p>')
    fC5.write('<p><a href="noticiasNÁPOLES.html"><h5>Notícias do Nápoles</h5></a></p>')
    fC5.write('<p><a href="noticiasAC MILAN.html"><h5>Notícias do AC Milan</h5></a></p>')
    fC5.write('<p><a href="noticiasVERONA.html"><h5>Notícias do Verona</h5></a></p>')
    fC5.write('<p><a href="noticiasPARMA.html"><h5>Notícias do Parma</h5></a></p>')
    fC5.write('<p><a href="noticiasBOLONHA.html"><h5>Notícias do Bolonha</h5></a></p>')
    fC5.write('<p><a href="noticiasSASSUOLO.html"><h5>Notícias do Sassuolo</h5></a></p>')
    fC5.write('<p><a href="noticiasCAGLIARI.html"><h5>Notícias do Cagliari</h5></a></p>')
    fC5.write('<p><a href="noticiasFIORENTINA.html"><h5>Notícias do Fiorentina</h5></a></p>')
    fC5.write('<p><a href="noticiasUDINESE.html"><h5>Notícias do Udinese</h5></a></p>')
    fC5.write('<p><a href="noticiasTORINO.html"><h5>Notícias do Torino</h5></a></p>')
    fC5.write('<p><a href="noticiasSAMPDORIA.html"><h5>Notícias do Sampdoria</h5></a></p>')
    fC5.write('<p><a href="noticiasGÉNOVA.html"><h5>Notícias do Génova</h5></a></p>')
    fC5.write('<p><h5>O jornal ABola não possui uma página dedicada ao Lecce</h5></p>')
    fC5.write('<p><h5>O jornal ABola não possui uma página dedicada ao SPAL</h5></p>')
    fC5.write('<p><h5>O jornal ABola não possui uma página dedicada ao Brescia</h5></p>')

    fC6 = open("paginas/noticiasClubesLigaAlema.html", 'w+')

    fC6.write("<h2>Notícias relativas aos clubes da liga alemã:</h2>")

    fC6.write('<p><a href="noticiasBAYERN MUNIQUE.html"><h5>Notícias do Bayern Munique</h5></a></p>')
    fC6.write('<p><a href="noticiasBORUSSIA DORTMUND.html"><h5>Notícias do Dortmund</h5></a></p>')
    fC6.write('<p><h5>O jornal ABola não possui uma página dedicada ao Leipzig</h5></p>')
    fC6.write('<p><h5>O jornal ABola não possui uma página dedicada ao Borussia Monchengladbach</h5></p>')
    fC6.write('<p><a href="noticiasBAYER LEVERKUSEN.html"><h5>Notícias do Bayer Leverkusen</h5></a></p>')
    fC6.write('<p><a href="noticiasWOLFSBURGO.html"><h5>Notícias do Wolfsburgo</h5></a></p>')
    fC6.write('<p><h5>O jornal ABola não possui uma página dedicada ao Hoffenheim</h5></p>')
    fC6.write('<p><a href="noticiasFRIBURGO.html"><h5>Notícias do Friburgo</h5></a></p>')
    fC6.write('<p><h5>O jornal ABola não possui uma página dedicada ao Eintracht Frankfurt</h5></p>')
    fC6.write('<p><h5>O jornal ABola não possui uma página dedicada ao Hertha Berlin</h5></p>')
    fC6.write('<p><a href="noticiasSCHALKE 04.html"><h5>Notícias do Schalke 04</h5></a></p>')
    fC6.write('<p><h5>O jornal ABola não possui uma página dedicada ao Union Berlin</h5></p>')
    fC6.write('<p><h5>O jornal ABola não possui uma página dedicada ao Mainz</h5></p>')
    fC6.write('<p><h5>O jornal ABola não possui uma página dedicada ao Colónia</h5></p>')
    fC6.write('<p><h5>O jornal ABola não possui uma página dedicada ao Augsburgo</h5></p>')
    fC6.write('<p><h5>O jornal ABola não possui uma página dedicada ao Fortuna Dusseldorf</h5></p>')
    fC6.write('<p><h5>O jornal ABola não possui uma página dedicada ao Weder Bremen</h5></p>')
    fC6.write('<p><h5>O jornal ABola não possui uma página dedicada ao Padderborn</h5></p>')

    fC7 = open("paginas/noticiasClubesLigaFrancesa.html", 'w+')

    fC7.write("<h2>Notícias relativas aos clubes da liga frencesa:</h2>")

    fC7.write('<p><a href="noticiasPARIS SAINT-GERMAIN.html"><h5>Notícias do PSG</h5></a></p>')
    fC7.write('<p><a href="noticiasMARSELHA.html"><h5>Notícias do Marselha</h5></a></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Rennes</h5></p>')
    fC7.write('<p><a href="noticiasLILLE.html"><h5>Notícias do Lille</h5></a></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Reims</h5></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Nice</h5></p>')
    fC7.write('<p><a href="noticiasLYON.html"><h5>Notícias do Lyon</h5></a></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Montpellier</h5></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Mónaco</h5></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Angers</h5></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Estrasburgo</h5></p>')
    fC7.write('<p><a href="noticiasBORDÉUS.html"><h5>Notícias do Bordéus</h5></a></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Nantes</h5></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Brest</h5></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Metz</h5></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Dijon</h5></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Saint-Étienne</h5></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Nimes</h5></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Amiens</h5></p>')
    fC7.write('<p><h5>O jornal ABola não possui uma página dedicada ao Toulouse</h5></p>')

    fC8 = open("paginas/noticiasClubesLigaBrasileira.html", 'w+')

    fC8.write("<h2>Notícias relativas aos clubes da liga espanhola:</h2>")

    fC8.write('<p><a href="noticiasFLAMENGO.html"><h5>Notícias do Flamengo</h5></a></p>')
    fC8.write('<p><a href="noticiasSANTOS.html"><h5>Notícias do Santos</h5></a></p>')
    fC8.write('<p><a href="noticiasPALMEIRAS.html"><h5>Notícias do Palmeiras</h5></a></p>')
    fC8.write('<p><a href="noticiasGRÉMIO.html"><h5>Notícias do Grémio</h5></a></p>')
    fC8.write('<p><a href="noticiasAT. PARANAENSE.html"><h5>Notícias do Atlético Paranaense</h5></a></p>')
    fC8.write('<p><a href="noticiasSÃO PAULO.html"><h5>Notícias do São Paulo</h5></a></p>')
    fC8.write('<p><h5>O jornal ABola não possui uma página dedicada ao Internacional</h5></p>')
    fC8.write('<p><a href="noticiasCORINTHIANS.html"><h5>Notícias do Corinthians</h5></a></p>')
    fC8.write('<p><h5>O jornal ABola não possui uma página dedicada ao Fortaleza</h5></p>')
    fC8.write('<p><h5>O jornal ABola não possui uma página dedicada ao Goiás</h5></p>')
    fC8.write('<p><h5>O jornal ABola não possui uma página dedicada ao Bahia</h5></p>')
    fC8.write('<p><a href="noticiasVASCO GAMA.html"><h5>Notícias do Vasco da Gama</h5></a></p>')
    fC8.write('<p><a href="noticiasAT. MINEIRO.html"><h5>Notícias do Atlético Mineiro</h5></a></p>')
    fC8.write('<p><a href="noticiasFLUMINENSE.html"><h5>Notícias do Fluminense</h5></a></p>')
    fC8.write('<p><a href="noticiasBOTAFOGO.html"><h5>Notícias do Botafogo</h5></a></p>')
    fC8.write('<p><a href="noticiasCRUZEIRO.html"><h5>Notícias do Cruzeiro</h5></a></p>')
    fC8.write('<p><h5>O jornal ABola não possui uma página dedicada ao Alagoano</h5></p>')
    fC8.write('<p><a href="noticiasCHAPECOENSE.html"><h5>Notícias do Chapecoense</h5></a></p>')
    fC8.write('<p><h5>O jornal ABola não possui uma página dedicada ao Avaí</h5></p>')
    fC8.write('<p><h5>O jornal ABola não possui uma página dedicada ao Ceará</h5></p>')

def getClubSoup():
    for num in primeiraLigaNums:
        sourceClube = requests.get(linkGeral + str(num)).content
        soupClube = BeautifulSoup(sourceClube,'html.parser')
        soupClubesPrimeiraLiga.append(soupClube)
    for num2 in segundaLigaNums:
        sourceClube = requests.get(linkGeral + str(num2)).content
        soupClube = BeautifulSoup(sourceClube,'html.parser')
        soupClubesPrimeiraLiga.append(soupClube)
    for num3 in ligaInglesaNums:
        sourceClube = requests.get(linkGeral + str(num3)).content
        soupClube = BeautifulSoup(sourceClube,'html.parser')
        soupClubesLigaInglesa.append(soupClube)
    for num4 in ligaEspanholaNums:
        sourceClube = requests.get(linkGeral + str(num4)).content
        soupClube = BeautifulSoup(sourceClube,'html.parser')
        soupClubesLigaEspanhola.append(soupClube)
    for num5 in ligaItalianaNums:
        sourceClube = requests.get(linkGeral + str(num5)).content
        soupClube = BeautifulSoup(sourceClube,'html.parser')
        soupClubesLigaItaliana.append(soupClube)
    for num6 in ligaAlemaNums:
        sourceClube = requests.get(linkGeral + str(num6)).content
        soupClube = BeautifulSoup(sourceClube,'html.parser')
        soupClubesLigaAlema.append(soupClube)
    for num7 in ligaFrancesaNums:
        sourceClube = requests.get(linkGeral + str(num7)).content
        soupClube = BeautifulSoup(sourceClube,'html.parser')
        soupClubesLigaFrancesa.append(soupClube)
    for num8 in ligaBrasileiraNums:
        sourceClube = requests.get(linkGeral + str(num8)).content
        soupClube = BeautifulSoup(sourceClube,'html.parser')
        soupClubesLigaBrasileira.append(soupClube)

def clubeCont(cont):
    news = cont.find('section',{'id':'SeccaoA'}).find_all('a',href=True)
    i = 0
    k = 1
    for noticia in news:
        linkNoticia = 'https://www.abola.pt' + noticia['href']
        infos = noticia.find_all('span')
        if(i == 0):
            fClube = open("paginas/noticias{}.html".format(infos[1].text), 'w+')
        if(i == 1):
            fClube.write("<h2>Notícias do {}:</h2>".format(infos[1].text))
        fClube.write('<h3>Notícia ' + str(k) + ': <a href="../artigos/' + infos[0].text.replace("/"," ").replace(":"," ") + '.html">')
        n = 0
        for info in infos:
            fClube.write(info.text + " ")
            if n == 0 :
                fClube.write('</a></h3><p></p>')
            elif n == 2:
                break
            n+=1
        i = 1
        k += 1
        #ARTIGO
        sourceNoticia = requests.get(linkNoticia).content
        soupNoticia = BeautifulSoup(sourceNoticia,'html.parser')
        art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
        if(soupNoticia.find('h1',{'id':'body_Ver_lblTitulo'})):
            artigosTitulo = soupNoticia.find('h1',{'id':'body_Ver_lblTitulo'}).text
        else:
            artigosTitulo = ""
        artigosImagens = noticia.find('div',True)
        artigosTexto = soupNoticia.find('div','corpo-noticia').find_all('p')
        art1.write("<h2>" + artigosTitulo + "</h2>")
        if (artigosImagens['data-img'][0] == 'h'):
            art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
        else:
            art1.write('<img src="https:' + artigosImagens['data-img'] + '"/>')
        for p in artigosTexto:
            art1.write('<p>' + p.text + '</p>')
        i+=1

def clubAll():
    clubLinks()
    getClubSoup()

    for cont in soupClubesPrimeiraLiga:
        clubeCont(cont)

    for cont2 in soupClubesSegundaLiga:
        clubeCont(cont2)

    for cont3 in soupClubesLigaInglesa:
        clubeCont(cont3)

    for cont4 in soupClubesLigaEspanhola:
        clubeCont(cont4)

    for cont5 in soupClubesLigaItaliana:
        clubeCont(cont5)

    for cont6 in soupClubesLigaAlema:
        clubeCont(cont6)

    for cont7 in soupClubesLigaFrancesa:
        clubeCont(cont7)

    for cont8 in soupClubesLigaBrasileira:
        clubeCont(cont8)

def main():
    if (exists == 0):
        print('A realizar o web scraping')
        sections()
        clubAll()
    else:
        new = 2 # open in a new tab, if possible
        clubLinks()
        # open an HTML file on my own computer
        url = path + "/homepage.html"
        webbrowser.open(url,new=new)

if __name__ == "__main__":
    main()