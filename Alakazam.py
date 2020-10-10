# -*- coding: utf-8 -*-
import pyttsx3 as ts
import speech_recognition as sp
from time import sleep
import Functions as ft
import keyboard

while True:
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('9'):
        # Starting voice system

        engine = ts.init()
        engine.setProperty('rate', 150)
        print('Iniciando Alakazam')
        engine.say("Iniciando Alakazam")
        engine.runAndWait()

        # Starting recognition system
        rec = sp.Recognizer()
        mic = sp.Microphone(1)

        # Starting program
        print('Estou te escutando')
        engine.say("Estou te escutando")
        engine.runAndWait()

        while True:

            # Voice recognition

            try:
                text = ft.Recognizing()

                # Activating action

                if 'AÇÃO' in text or 'AÇÕES' in text:
                    ft.Stock()

                # Turn off lights

                elif 'DESLIGAR' in text:
                    ft.LightOff()

                # Turn on lights

                elif 'LIGAR' in text:
                    ft.LightOn()

                # Show the weather

                elif 'TEMPERATURA' in text or 'TEMPO' in text:
                    ft.Weather()

                # Open Youtube

                elif 'YOUTUBE' in text:
                    ft.Youtube()

                # Search on Wikipédia

                elif 'WIKIPÉDIA' in text or 'WIKIPEDIA' in text:
                    ft.Wikipedia()

                # PRICES #

                # Dólar

                elif 'DOLAR' in text or 'DÓLAR' in text:
                    ft.Dolar()

                # EURO

                elif 'EURO' in text:
                    ft.Euro()

                # Google search

                elif 'GOOGLE' in text:
                    ft.GoogleSearch()

                # Disable system

                elif 'DESATIVAR' in text:
                    print('Desativando')
                    engine.say('desativando')
                    engine.runAndWait()
                    engine.stop()
                    break

                # Another text

                else:
                    print(f'Eu entendi {text}, tente novamente')
                    engine.say(f'Eu entendi {text}')
                    engine.runAndWait()
                    sleep(1)
            except:
                print('Não compreendi')
                engine.say(f'Não compreendi')
                engine.runAndWait()
