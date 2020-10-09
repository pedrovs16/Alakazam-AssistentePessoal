# -*- coding: utf-8 -*-
import pyttsx3 as ts
import speech_recognition as sp
from time import sleep
import Functions as ft
import keyboard

while True:
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('9'):
        # Iniciando sistema de voz

        engine = ts.init()
        engine.setProperty('rate', 150)
        print('Iniciando Alakazam')
        engine.say("Iniciando Alakazam")
        engine.runAndWait()

        # Iniciando sistema de reconhecimento
        rec = sp.Recognizer()
        mic = sp.Microphone(1)

        # Iniciando
        print('Estou te escutando')
        engine.say("Estou te escutando")
        engine.runAndWait()

        while True:

            # Reconhecendo voz

            try:
                text = ft.Reconhecendo()


                # DesligarLuz

                if 'DESLIGAR' in text:
                    ft.DesligarLuz()

                # Ligar luz

                elif 'LIGAR' in text:
                    ft.LigarLuz()

                # Ativar ação

                elif 'AÇÃO' in text or 'AÇÕES' in text:
                    ft.Acao()

                # Ver temperatura

                elif 'TEMPERATURA' in text or 'TEMPO' in text:
                    ft.Weather()

                # Abrir Youtube

                elif 'YOUTUBE' in text:
                    ft.Youtube()

                # Pesquisar no Wikipedia

                elif 'WIKIPÉDIA' in text or 'WIKIPEDIA' in text:
                    ft.Wikipedia()

                # COTAÇÕES #

                # Dólar

                elif 'DOLAR' in text or 'DÓLAR' in text:
                    ft.Dolar()

                # EURO

                elif 'EURO' in text:
                    ft.Euro()

                # Desativar sistema

                elif 'DESATIVAR' in text:
                    print('Desativando')
                    engine.say('desativando')
                    engine.runAndWait()
                    engine.stop()
                    break

                # Não entendeu a frase

                else:
                    print(f'Eu entendi {text}, tente novamente')
                    engine.say(f'Eu entendi {text}')
                    engine.runAndWait()
                    sleep(1)
            except:
                print('Não compreendi')
                engine.say(f'Não compreendi')
                engine.runAndWait()
