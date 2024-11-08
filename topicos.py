from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time 
import pandas as pd
import pyautogui as pyag

print("\n===== Programa Criador de Textos Automático =====")

tema = (input("\nQual o tema central do texto?\n"))
quantidadeTopicos = int(input("\nQuantos tópicos terá esse texto?\n"))
temasTopicos = [tema]
finalizacaoCriada = False
adicionarTitulo = True

for i in range(quantidadeTopicos):
    temaTopico = (input(f"\nQual o tema do tópico {i + 1}?\n"))
    temasTopicos.append(temaTopico)
    
for i in range(len(temasTopicos)):
    pesquisa = ""
    
    if i == 0:
        pesquisa = f"Faca um pequeno texto de um parágrafo e sem titulo iniciando um documento sobre o tema: {tema}. Detalhe: nao formate o texto, deixe apenas texto normal."
    elif i == quantidadeTopicos + 1 and finalizacaoCriada == False:
        pesquisa = f"Faca um pequeno texto de um parágrafo e sem titulo finalizando e concluindo um documento sobre o tema: {tema}. Detalhe: nao formate o texto, deixe apenas texto normal."
        finalizacao = ""
        temasTopicos.append(finalizacao)
        finalizacaoCriada = True
    else:
        pesquisa = f"Faca um pequeno texto de um parágrafo e sem titulo sobre o tema: {tema}. Topico: {temasTopicos[i]}. Detalhe: nao formate o texto, deixe apenas texto normal."

    pyag.moveTo(x=558, y=750)
    pyag.click()
    pyag.moveTo(x=498, y=675)
    pyag.click()
    pyag.write(pesquisa)
    pyag.press('enter')
    time.sleep(5)
    pyag.moveTo(x=387, y=559)
    pyag.click()
    pyag.moveTo(x=704, y=750)
    pyag.click()
    
    if adicionarTitulo == True:
        pyag.moveTo(x=235, y=89)
        pyag.click()
        pyag.write("calibri light")
        pyag.press('enter')
        
        pyag.moveTo(x=302, y=88)
        pyag.click()
        pyag.write("16")
        pyag.press('enter')
        
        pyag.write(tema)
        pyag.hotkey('ctrl', 'e')
        pyag.press('enter')
        pyag.press('enter')
        
        adicionarTitulo = False
    
    pyag.moveTo(x=729, y=102)
    pyag.click()
    
    pyag.moveTo(x=235, y=89)
    pyag.click()
    pyag.write("arial")
    pyag.press('enter')
        
    pyag.moveTo(x=302, y=88)
    pyag.click()
    pyag.write("12")
    pyag.press('enter')
    
    pyag.hotkey('ctrl', 'v')
    pyag.hotkey('ctrl', 'j')
    pyag.press('enter')
    pyag.press('enter')
