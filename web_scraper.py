#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import os

source = requests.get('https://www.abola.pt/').content
soup = BeautifulSoup(source,'html.parser')

header_title = soup.find_all("div",'slice-header-title')
collection_title = soup.find_all("div",'collection_header')

ePicksCont = soup.find_all("div",'field-item')

path = "paginas"

try:
    os.mkdir(path)
except OSError:
    print ("Directory %s already exists" % path)
else:
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
i = 1
f1.write('<h2>Lista de Notícias Principais</h2>')
for inset in dozeNoticias:
    #LINK DESTE HEADLINE
    link_slide = 'https://www.abola.pt' + inset['href']
    #TÍTULO DESTE HEADLINE
    infos = inset.find_all('span')
    f1.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
    n = 0
    for info in infos:
        f1.write(info.text + " ")
        if n == 0 :
            f1.write('</a></h3><p></p>')
        elif n == 2:
            break
        n+=1
    #ARTIGO
    sourcePrincipais = requests.get(link_slide).content
    soupPrincipais = BeautifulSoup(sourcePrincipais,'html.parser')
    art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
    if(soupPrincipais.find('h1',{'id':'body_Ver_lblTitulo'})):
        artigosTitulo = soupPrincipais.find('h1',{'id':'body_Ver_lblTitulo'}).text
    else:
        artigosTitulo = ""
    artigosImagens = inset.find('div',True)
    artigosTexto = soupPrincipais.find('div','corpo-noticia').find_all('p')
    art1.write("<h2>" + artigosTitulo + "</h2>")
    if (artigosImagens['data-img'][0] == 'h'):
        art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
    else:
        art1.write('<img src="https:' + artigosImagens['data-img'] + '"/>')
    for p in artigosTexto:
        art1.write('<p>' + p.text + '</p>')
    i+=1

#SECÇÃO EM DESTAQUE

f2 = open("paginas/noticiasEmDestaque.html", 'w+')

emDestaque = soup.find('section',{'id':'caixa90'}).find_all('a',href=True)
i = 1
f2.write('<h2>Lista de Notícias Em Destaque</h2>')
for inset in emDestaque:
    #LINK DESTE HEADLINE
    link_slide = 'https://www.abola.pt' + inset['href']
    #TÍTULO DESTE HEADLINE
    infos = inset.find_all('span')
    f2.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
    n = 0
    for info in infos:
        f2.write(info.text + " ")
        if n == 0 :
            f2.write('</a></h3><p></p>')
        elif n == 2:
            break
        n+=1
    #ARTIGO
    sourceDestaques = requests.get(link_slide).content
    soupDestaques = BeautifulSoup(sourceDestaques,'html.parser')
    art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
    if(soupDestaques.find('h1',{'id':'body_Ver_lblTitulo'})):
        artigosTitulo = soupDestaques.find('h1',{'id':'body_Ver_lblTitulo'}).text
    else:
        artigosTitulo = ""
    artigosImagens = inset.find('div',True)
    artigosTexto = soupDestaques.find('div','corpo-noticia').find_all('p')
    art1.write("<h2>" + artigosTitulo + "</h2>")
    if (artigosImagens['data-img'][0] == 'h'):
        art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
    else:
        art1.write('<img src="https:' + artigosImagens['data-img'] + '"/>')
    for p in artigosTexto:
        art1.write('<p>' + p.text + '</p>')
    i+=1

#SECÇÃO NACIONAL

f3 = open("paginas/noticiasNacionais.html", 'w+')

nacional = soup.find('div',{'id':'ctl00_body_nacional_divNoticiasNacional'}).find_all('a',href=True)
i = 1
f3.write('<h2>Lista de Notícias A Nível Nacional:</h2>')
for inset in nacional:
    #LINK DESTE HEADLINE
    link_slide = 'https://www.abola.pt' + inset['href']
    #TÍTULO DESTE HEADLINE
    infos = inset.find_all('span')
    f3.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
    n = 0
    for info in infos:
        f3.write(info.text + " ")
        if n == 0 :
            f3.write('</a></h3><p></p>')
        elif n == 2:
            break
        n+=1
    #ARTIGO
    sourceNacional = requests.get(link_slide).content
    soupNacional = BeautifulSoup(sourceNacional,'html.parser')
    art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
    if(soupNacional.find('h1',{'id':'body_Ver_lblTitulo'})):
        artigosTitulo = soupNacional.find('h1',{'id':'body_Ver_lblTitulo'}).text
    else:
        artigosTitulo = ""
    artigosImagens = inset.find('div',True)
    artigosTexto = soupNacional.find('div','corpo-noticia').find_all('p')
    art1.write("<h2>" + artigosTitulo + "</h2>")
    art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
    for p in artigosTexto:
        art1.write('<p>' + p.text + '</p>')
    i+=1

#SECÇÃO INTERNACIONAL

f4 = open("paginas/noticiasInternacionais.html", 'w+')

internacional = soup.find('div',{'id':'ctl00_body_internacional_divNoticiasInternacional'}).find_all('a',href=True)
i = 1
f4.write('<h2>Lista de Notícias A Nível Internacional:</h2>')
for inset in internacional:
    #LINK DESTE HEADLINE
    link_slide = 'https://www.abola.pt' + inset['href']
    #TÍTULO DESTE HEADLINE
    infos = inset.find_all('span')
    f4.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
    n = 0
    for info in infos:
        f4.write(info.text + " ")
        if n == 0 :
            f4.write('</a></h3><p></p>')
        elif n == 2:
            break
        n+=1
    #ARTIGO
    sourceInternacional = requests.get(link_slide).content
    soupInternacional = BeautifulSoup(sourceInternacional,'html.parser')
    art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
    if(soupInternacional.find('h1',{'id':'body_Ver_lblTitulo'})):
        artigosTitulo = soupInternacional.find('h1',{'id':'body_Ver_lblTitulo'}).text
    else:
        artigosTitulo = ""
    artigosImagens = inset.find('div',True)
    artigosTexto = soupInternacional.find('div','corpo-noticia').find_all('p')
    art1.write("<h2>" + artigosTitulo + "</h2>")
    if (artigosImagens['data-img'][0] == 'h'):
        art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
    else:
        art1.write('<img src="https:' + artigosImagens['data-img'] + '"/>')
    for p in artigosTexto:
        art1.write('<p>' + p.text + '</p>')
    i+=1

#SECÇÃO MODALIDADES

f5 = open("paginas/noticiasModalidades.html", 'w+')

modalidades = soup.find('div',{'id':'ctl00_body_modalidades_divNoticiasModalidades'}).find_all('a',href=True)
i = 1
f5.write('<h2>Lista de Notícias Em Relações a Outras Modalidades:</h2>')
for inset in modalidades:
    #LINK DESTE HEADLINE
    link_slide = 'https://www.abola.pt' + inset['href']
    #TÍTULO DESTE HEADLINE
    infos = inset.find_all('span')
    f5.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
    n = 0
    for info in infos:
        f5.write(info.text + " ")
        if n == 0 :
            f5.write('</a></h3><p></p>')
        elif n == 2:
            break
        n+=1
    #ARTIGO
    sourceModalidades = requests.get(link_slide).content
    soupModalidades = BeautifulSoup(sourceModalidades,'html.parser')
    art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
    if(soupModalidades.find('h1',{'id':'body_Ver_lblTitulo'})):
        artigosTitulo = soupModalidades.find('h1',{'id':'body_Ver_lblTitulo'}).text
    else:
        artigosTitulo = ""
    artigosImagens = inset.find('div',True)
    artigosTexto = soupModalidades.find('div','corpo-noticia').find_all('p')
    art1.write("<h2>" + artigosTitulo + "</h2>")
    if (artigosImagens['data-img'][0] == 'h'):
        art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
    else:
        art1.write('<img src="https:' + artigosImagens['data-img'] + '"/>')
    for p in artigosTexto:
        art1.write('<p>' + p.text + '</p>')
    i+=1

#SECÇÃO ECONOMIA DA BOLA

f6 = open("paginas/noticiasEconomia.html", 'w+')

economia = soup.find('div',{'id':'ctl00_body_economico_divNoticiasEconomico'}).find_all('a',href=True)
i = 1
f6.write('<h2>Lista de Notícias Em Relação à Economia Futebolistica:</h2>')
for inset in economia:
    #LINK DESTE HEADLINE
    link_slide = 'https://www.abola.pt' + inset['href']
    #TÍTULO DESTE HEADLINE
    infos = inset.find_all('span')
    f6.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
    n = 0
    for info in infos:
        f6.write(info.text + " ")
        if n == 0 :
            f6.write('</a></h3><p></p>')
        elif n == 2:
            break
        n+=1
    #ARTIGO
    sourceEconomia = requests.get(link_slide).content
    soupEconomia = BeautifulSoup(sourceEconomia,'html.parser')
    art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
    if(soupEconomia.find('h1',{'id':'body_Ver_lblTitulo'})):
        artigosTitulo = soupEconomia.find('h1',{'id':'body_Ver_lblTitulo'}).text
    else:
        artigosTitulo = ""
    artigosImagens = inset.find('div',True)
    artigosTexto = soupEconomia.find('div','corpo-noticia').find_all('p')
    art1.write("<h2>" + artigosTitulo + "</h2>")
    if (artigosImagens['data-img'][0] == 'h'):
        art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
    else:
        art1.write('<img src="https:' + artigosImagens['data-img'] + '"/>')
    for p in artigosTexto:
        art1.write('<p>' + p.text + '</p>')
    i+=1

#SECÇÃO MOTORES

f7 = open("paginas/noticiasMotores.html", 'w+')

motores = soup.find('div',{'id':'ctl00_body_motores_divNoticiasMotores'}).find_all('a',href=True)
i = 1
f7.write('<h2>Lista de Notícias Em Relação a Desportos Motorizados:</h2>')
for inset in motores:
    #LINK DESTE HEADLINE
    link_slide = 'https://www.abola.pt' + inset['href']
    #TÍTULO DESTE HEADLINE
    infos = inset.find_all('span')
    f7.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
    n = 0
    for info in infos:
        f7.write(info.text + " ")
        if n == 0 :
            f7.write('</a></h3><p></p>')
        elif n == 2:
            break
        n+=1
    #ARTIGO
    sourceMotores = requests.get(link_slide).content
    soupMotores = BeautifulSoup(sourceMotores,'html.parser')
    art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
    if(soupMotores.find('h1',{'id':'body_Ver_lblTitulo'})):
        artigosTitulo = soupMotores.find('h1',{'id':'body_Ver_lblTitulo'}).text
    else:
        artigosTitulo = ""
    artigosImagens = inset.find('div',True)
    artigosTexto = soupMotores.find('div','corpo-noticia').find_all('p')
    art1.write("<h2>" + artigosTitulo + "</h2>")
    if (artigosImagens['data-img'][0] == 'h'):
        art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
    else:
        art1.write('<img src="https:' + artigosImagens['data-img'] + '"/>')
    for p in artigosTexto:
        art1.write('<p>' + p.text + '</p>')
    i+=1

#SECÇÃO A BOLA É MINHA

f8 = open("paginas/noticiasABolaEMinha.html", 'w+')

abolaeminha = soup.find('div',{'id':'ctl00_body_abolaeminha_divNoticiasABolaEMinha'}).find_all('a',href=True)
i = 1
f8.write('<h2>Secção a bola é minha:</h2>')
for inset in abolaeminha:
    #LINK DESTE HEADLINE
    link_slide = 'https://www.abola.pt' + inset['href']
    #TÍTULO DESTE HEADLINE
    infos = inset.find_all('span')
    f8.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
    n = 0
    for info in infos:
        f8.write(info.text + " ")
        if n == 0 :
            f8.write('</a></h3><p></p>')
        elif n == 2:
            break
        n+=1
    #ARTIGO
    sourceABola = requests.get(link_slide).content
    soupABola = BeautifulSoup(sourceABola,'html.parser')
    art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
    if(soupABola.find('h1',{'id':'body_Ver_lblTitulo'})):
        artigosTitulo = soupABola.find('h1',{'id':'body_Ver_lblTitulo'}).text
    else:
        artigosTitulo = ""
    artigosImagens = inset.find('div',True)
    artigosTexto = soupABola.find('div','corpo-noticia').find_all('p')
    art1.write("<h2>" + artigosTitulo + "</h2>")
    if (artigosImagens['data-img'][0] == 'h'):
        art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
    else:
        art1.write('<img src="https:' + artigosImagens['data-img'] + '"/>')
    for p in artigosTexto:
        art1.write('<p>' + p.text + '</p>')
    i+=1

#SECÇÃO OUTROS MUNDOS

f9 = open("paginas/noticiasNaoDesportivas.html", 'w+')

outrosmundos = soup.find('div',{'id':'ctl00_body_mundos_divNoticiasOutrosMundos'}).find_all('a',href=True)
i = 1
f9.write('<h2>Secção outros mundos:</h2>')
for inset in outrosmundos:
    #LINK DESTE HEADLINE
    link_slide = 'https://www.abola.pt' + inset['href']
    #TÍTULO DESTE HEADLINE
    infos = inset.find_all('span')
    f9.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
    n = 0
    for info in infos:
        f9.write(info.text + " ")
        if n == 0 :
            f9.write('</a></h3><p></p>')
        elif n == 2:
            break
        n+=1
    #ARTIGO
    sourceOutrosMundos = requests.get(link_slide).content
    soupOutrosMundos = BeautifulSoup(sourceOutrosMundos,'html.parser')
    art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
    if(soupOutrosMundos.find('h1',{'id':'body_Ver_lblTitulo'})):
        artigosTitulo = soupOutrosMundos.find('h1',{'id':'body_Ver_lblTitulo'}).text
    else:
        artigosTitulo = ""
    artigosImagens = inset.find('div',True)
    artigosTexto = soupOutrosMundos.find('div','corpo-noticia').find_all('p')
    art1.write("<h2>" + artigosTitulo + "</h2>")
    if (artigosImagens['data-img'][0] == 'h'):
        art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
    else:
        art1.write('<img src="https:' + artigosImagens['data-img'] + '"/>')
    for p in artigosTexto:
        art1.write('<p>' + p.text + '</p>')
    i+=1

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
i = 1
f11.write("<h2>Notícias relativas ao futebol brasileiro:</h2>")
for inset in brasil:
    #LINK DESTE HEADLINE
    link_slide = 'https://www.abola.pt' + inset['href']
    #TÍTULO DESTE HEADLINE
    infos = inset.find_all('span')
    f11.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
    n = 0
    for info in infos:
        f11.write(info.text + " ")
        if n == 0 :
            f11.write('</a></h3><p></p>')
        elif n == 2:
            break
        n+=1
    #ARTIGO
    sourceBrasil = requests.get(link_slide).content
    soupBrasil = BeautifulSoup(sourceBrasil,'html.parser')
    art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
    if(soupBrasil.find('h1',{'id':'body_Ver_lblTitulo'})):
        artigosTitulo = soupBrasil.find('h1',{'id':'body_Ver_lblTitulo'}).text
    else:
        artigosTitulo = ""
    artigosImagens = inset.find('div',True)
    artigosTexto = soupBrasil.find('div','corpo-noticia').find_all('p')
    art1.write("<h2>" + artigosTitulo + "</h2>")
    if (artigosImagens['data-img'][0] == 'h'):
        art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
    else:
        art1.write('<img src="https:' + artigosImagens['data-img'] + '"/>')
    for p in artigosTexto:
        art1.write('<p>' + p.text + '</p>')
    i+=1

#SECÇÃO RELATIVA A ÁFRICA

f12 = open("paginas/noticiasAfricanas.html", 'w+')

africa = soup.find('div',{'id':'ctl00_body_africa_divNoticiasAfrica'}).find_all('a',href=True)
i = 1
f12.write("<h2>Notícias relativas ao futebol africano:</h2>")
for inset in africa:
    #LINK DESTE HEADLINE
    link_slide = 'https://www.abola.pt' + inset['href']
    #TÍTULO DESTE HEADLINE
    infos = inset.find_all('span')
    f12.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
    n = 0
    for info in infos:
        f12.write(info.text + " ")
        if n == 0 :
            f12.write('</a></h3><p></p>')
        elif n == 2:
            break
        n+=1
    #ARTIGO
    sourceAfrica = requests.get(link_slide).content
    soupAfrica = BeautifulSoup(sourceAfrica,'html.parser')
    art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
    if(soupAfrica.find('h1',{'id':'body_Ver_lblTitulo'})):
        artigosTitulo = soupAfrica.find('h1',{'id':'body_Ver_lblTitulo'}).text
    else:
        artigosTitulo = ""
    artigosImagens = inset.find('div',True)
    artigosTexto = soupAfrica.find('div','corpo-noticia').find_all('p')
    art1.write("<h2>" + artigosTitulo + "</h2>")
    if (artigosImagens['data-img'][0] == 'h'):
        art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
    else:
        art1.write('<img src="https:' + artigosImagens['data-img'] + '"/>')
    for p in artigosTexto:
        art1.write('<p>' + p.text + '</p>')
    i+=1

#SECÇÃO RELATIVA A RÚBRICAS ONLINE

f13 = open("paginas/rubricasOnline.html", 'w+')

rubricas = soup.find('div',{'id':'ctl00_body_outras_divNoticiasOutras'}).find_all('a',href=True)
i = 1
f13.write("<h2>Rúbricas online:</h2>")
for inset in rubricas:
    #LINK DESTE HEADLINE
    link_slide = 'https://www.abola.pt' + inset['href']
    #TÍTULO DESTE HEADLINE
    infos = inset.find_all('span')
    f13.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
    n = 0
    for info in infos:
        f13.write(info.text + " ")
        if n == 0 :
            f13.write('</a></h3><p></p>')
        elif n == 2:
            break
        n+=1
    #ARTIGO
    sourceRubricas = requests.get(link_slide).content
    soupRubricas = BeautifulSoup(sourceRubricas,'html.parser')
    art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
    if(soupRubricas.find('h1',{'id':'body_Ver_lblTitulo'})):
        artigosTitulo = soupRubricas.find('h1',{'id':'body_Ver_lblTitulo'}).text
    else:
        artigosTitulo = ""
    artigosImagens = inset.find('div',True)
    artigosTexto = soupRubricas.find('div','corpo-noticia').find_all('p')
    art1.write("<h2>" + artigosTitulo + "</h2>")
    if (artigosImagens['data-img'][0] == 'h'):
        art1.write('<img src="' + artigosImagens['data-img'] + '"/>')
    else:
        art1.write('<img src="https:' + artigosImagens['data-img'] + '"/>')
    for p in artigosTexto:
        art1.write('<p>' + p.text + '</p>')
    i+=1

#SECÇÃO RELATIVA A ESTRELAS

f14 = open("paginas/noticiasCelebridades.html", 'w+')

estrelas = soup.find('div',{'id':'ctl00_body_estrelas_divNoticiasEstrelas'}).find_all('a',href=True)
i = 1
f14.write("<h2>Notícias relativas a outras celebridades:</h2>")
for inset in estrelas:
    #LINK DESTE HEADLINE
    link_slide = 'https://www.abola.pt' + inset['href']
    #TÍTULO DESTE HEADLINE
    infos = inset.find_all('span')
    f14.write('<h3>Notícia ' + str(i) + ': <a href="../artigos/' + infos[0].text.replace("/"," ") + '.html">')
    n = 0
    for info in infos:
        f14.write(info.text + " ")
        if n == 0 :
            f14.write('</a></h3><p></p>')
        elif n == 2:
            break
        n+=1

    #ARTIGO
    sourceEstrelas = requests.get(link_slide).content
    soupEstrelas = BeautifulSoup(sourceEstrelas,'html.parser')
    art1 = open("artigos/" + infos[0].text.replace("/"," ") + ".html",'w+')
    if(soupEstrelas.find('h1',{'id':'body_Ver_lblTitulo'})):
        artigosTitulo = soupEstrelas.find('h1',{'id':'body_Ver_lblTitulo'}).text
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
    #artigosImagens = inset.find('div',True)
    artigosTexto = soupAutomoveis.find('span',{'id':'conteudo_corpoNoticia_lblCorpoNoticia'}).find_all('p')
    art1.write("<h2>" + artigosTitulo + "</h2>")
    #art1.write("<img src=" + artigosImagens['data-img'] + "/>")
    for p in artigosTexto:
        art1.write('<p>' + p.text + '</p>')
    i+=1