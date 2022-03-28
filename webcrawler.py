#########################################################
# Alessandro Miranda Gonçalves                          #
# Linkedin: www.linkedin.com/alessandromirandagoncalves #
# Março/2022                                            #
#########################################################
# Programa que lê páginas HTML e extrai informações mais relevantes

import requests
import operator
from bs4 import BeautifulSoup
from collections import Counter

def start(url):
    wordlist = []
    sourcecode=requests.get(url).text

    soup = BeautifulSoup(sourcecode,'html.parser')

    for each_text in soup.find_all('div', {'class':'entry-content'}):
        content = each_text.text
        words = content.lower().split()

    for each_word in words:
        wordlist.append(each_word)
    clean_wordlist(wordlist)

# Retira caracteres especiais das palavras
def clean_wordlist(wordlist):
    clean_list = []
    symbols = "!@#$%¨&*()_+{}?:><,.][=-|–"
    #Incluído por Alessandro Miranda
    #Palavras comuns da língua inglesa que devem ser ignoradas
    lista_exclusao = ['in','at','you','we','they','and','or','using','with','to','of','off','on','for','the','is','like',
                      'a','one','two','three','four','five','six','seven','eight','nine','ten',
                      'set','all','from','by','most','not','used']

    for word in wordlist:
        for i in range(len(symbols)):
            word = word.replace(symbols[i],'')

        # Alterado por Alessandro Miranda
        # Se existir algo e NÃO for das palavras da lista_exclusao, acrescenta à clean_list
        if len(word) > 0 and word not in lista_exclusao:
                clean_list.append(word)
    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count={}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(),
                             key = operator.itemgetter(1)):
        print("{} : {}".format(key,value))

    c = Counter(word_count)
    top = c.most_common(10)
    # Alterado por Alessandro Miranda para melhor legibilidade dos resultados
    print('Palavras mais usadas:\n')
    print('Palavra            Ocorrência(s)')
    print('________________________________')
    for i in top:
        palavra, ocorr = i
        print ("{:<30}{:<20}".format(palavra, ocorr))

#Execução principal
if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=left-bar")