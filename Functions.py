# -*- coding: utf-8 -*-
import pyttsx3 as ts
import speech_recognition as sp
# from pyfirmata import Arduino
from time import sleep
import webbrowser
import yfinance as yf
import wikipedia
import requests
import googlesearch

# Starting voice system

engine = ts.init()
engine.setProperty('rate', 150)
engine.runAndWait()

# Wikipedia language

wikipedia.set_lang("pt")

# Starting recognition system
rec = sp.Recognizer()
mic = sp.Microphone()

# Arduino config
# Uno = Arduino('COM3')


def Recognizing():
    with mic as fonte:
        rec.adjust_for_ambient_noise(fonte)
        audio = rec.listen(fonte)
        print('Processando')
        engine.say('Processando')
        engine.runAndWait()
        text1 = rec.recognize_google(audio, language='pt-BR')
        text = text1.upper()
        print(text)
    return text.upper()


def Stock():
    while True:
        print('Escolha uma ação')
        engine.say('Escolha uma ação')
        engine.runAndWait()
        try:
            text = Recognizing()
            if "SAIR" in text:
                print('Saindo de ações')
                engine.say('Saindo de ações')
                engine.runAndWait()
                break
            else:
                stock = yf.Ticker(f"{text.upper()}.SA")
                wallet = stock.info
                porcent = ((float(wallet["ask"])) / (float(wallet["previousClose"])) - 1) * 100
                print(
                    f'Ontem a ação da {wallet["shortName"]} foi, {wallet["previousClose"]} e agora está, '
                    f'{wallet["ask"]} variou, {round(porcent, 2)} por cento')
                engine.say(
                    f'Ontem a ação da {wallet["shortName"]} foi, {wallet["previousClose"]} e agora está, '
                    f'{wallet["ask"]} variou, {round(porcent, 2)} por cento')
                engine.runAndWait()
        except:
            engine.say('Não entendi qual ação')
            engine.runAndWait()


def LightOn():
    print('Ligando')
    engine.say('ligando')
    engine.runAndWait()
    #Uno.digital[13].write(1)
    sleep(1)


def LightOff():
    print('Desligando')
    engine.say('desligando')
    engine.runAndWait()
    #Uno.digital[13].write(0)
    sleep(1)


def Weather():
    try:
        r = requests.get('http://api.weatherapi.com/v1/current.json?key=c1580e90d5fa4f2184f230545200710&q='
                         'Florianópolis')
        weather = r.json()

        temp = weather['current']['temp_c']
        cloud = weather['current']['cloud']
        wind_dir1 = weather['current']['wind_dir']
        wind_dir = str
        wind_kph = weather['current']['wind_kph']

        if wind_dir1 == 'SE':
            wind_dir = 'Sudeste'
        elif wind_dir1 == 'S':
            wind_dir = 'Sul'
        elif wind_dir1 == 'SW':
            wind_dir = 'Sudoeste'
        elif wind_dir1 == 'NE':
            wind_dir = 'Nordeste'
        elif wind_dir1 == 'NW':
            wind_dir = 'Noroeste'
        elif wind_dir1 == 'W':
            wind_dir = 'Oeste'
        elif wind_dir1 == 'E':
            wind_dir = 'Leste'

        print(f'A temperatura atual é,{temp} graus.'
              f' Velocidade do vento é {wind_kph} km '
              f'para direção {wind_dir}.'
              f'E a densidade das nuvens é de {cloud}')
        engine.say(f'A temperatura atual é,{temp} graus.'
                   f' Velocidade do vento é {wind_kph} quilomêtros '
                   f'para direção {wind_dir} .'
                   f' E a densidade das nuvens é de {cloud} por cento')
        engine.runAndWait()
    except:
        print('Não consegui a informação')
        engine.say('Não consegui a informação')
        engine.runAndWait()


def Youtube():
    try:
        print('Abrindo')
        engine.say('Abrindo')
        engine.runAndWait()
        webbrowser.open_new("https://www.youtube.com/")
    except:
        print('Não conseguir abrir')
        engine.say('Não conseguir abrir')
        engine.runAndWait()


def Wikipedia():
    while True:
        print('O que você quer pesquisar')
        engine.say('O que você quer pesquisar')
        engine.runAndWait()
        try:
            text = Recognizing()
            if text == "SAIR":
                print('Saindo de pesquisa')
                engine.say('Saindo de pesquisa')
                engine.runAndWait()
                break
            else:
                search = wikipedia.search(text)
                search = wikipedia.summary(search[0], sentences=2)
                print(search)
                engine.say(search)
                engine.runAndWait()
        except:
            engine.say('Não encontrei nada')
            engine.runAndWait()


def Dolar():
    r = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    dic = r.json()
    print(f"O valor do dolár está em, {dic['USD']['ask']} reais")
    engine.say(f"O valor do dolár está em, {dic['USD']['ask']} reais")
    engine.runAndWait()


def Euro():
    r = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')
    dic = r.json()
    print(f"O valor do euro está em, {dic['EUR']['ask']} reais")
    engine.say(f"O valor do euro está em, {dic['EUR']['ask']} reais")
    engine.runAndWait()


def GoogleSearch():
    while True:
        print('O que você quer pesquisar')
        engine.say('O que você quer pesquisar')
        engine.runAndWait()
        search = Recognizing()
        try:
            if search == 'SAIR':
                print('Saindo do google')
                engine.say('Saindo de google')
                engine.runAndWait()
                break
            else:
                print(f'Pesquisando {search}')
                engine.say(f'Pesquisando {search}')
                engine.runAndWait()
                for url in googlesearch.search(search, stop=3, lang='pt'):
                    webbrowser.open_new(url)
        except:
            engine.say('Não entendi o que você quer')
            engine.runAndWait()
