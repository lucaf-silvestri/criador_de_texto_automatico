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
finalizacao = "Faca um pequeno texto de um parágrafo e sem titulo finalizando e concluindo um documento sobre o tema: {tema}. Detalhe: nao formate o texto, deixe apenas texto normal."
finalizacao = "Faca um pequeno texto de um parágrafo e sem titulo finalizando e concluindo um documento sobre o tema: {tema}. Detalhe: nao formate o texto, deixe apenas texto normal."

def usarChatGPT(pesquisa, titulo):
    pyag.moveTo(x=704, y=1057)
    pyag.click()
    
    if titulo == True:
        pyag.moveTo(x=242, y=129)
        pyag.click()
        pyag.write("calibri light")
        pyag.press('enter')
        
        pyag.moveTo(x=319, y=129)
        pyag.click()
        pyag.write("16")
        pyag.press('enter')
        
        pyag.moveTo(x=639, y=1059)
        pyag.click()
        pyag.moveTo(x=691, y=960)
        pyag.click()
        pyag.write(f"faca um título bom para um texto sobre o tema: {tema}. Retorne apenas o título, sem formatacoes ou aspas.")
        pyag.press('enter')
        time.sleep(10)
        pyag.moveTo(x=592, y=815)
        pyag.click()
        pyag.moveTo(x=704, y=1057)
        pyag.click()
        pyag.hotkey('ctrl', 'v')
        
        pyag.hotkey('ctrl', 'e')
        pyag.press('enter')
        pyag.press('enter')
        
        return False
    
    pyag.moveTo(x=639, y=1059)
    pyag.click()
    pyag.moveTo(x=691, y=960)
    pyag.click()
    pyag.write(pesquisa)
    pyag.press('enter')
    time.sleep(10)
    pyag.moveTo(x=592, y=815)
    pyag.click()
    
    pyag.moveTo(x=951, y=143)
    pyag.click()
    
    pyag.moveTo(x=242, y=129)
    pyag.click()
    pyag.write("arial")
    pyag.press('enter')
        
    pyag.moveTo(x=319, y=129)
    pyag.click()
    pyag.write("12")
    pyag.press('enter')
    
    pyag.hotkey('ctrl', 'v')
    pyag.hotkey('ctrl', 'j')
    pyag.press('enter')
    pyag.press('enter')
    return False

for i in range(quantidadeTopicos):
    temaTopico = (input(f"\nQual o tema do tópico {i + 1}?\n"))
    temasTopicos.append(temaTopico)
    
for i in range(len(temasTopicos)):
    pesquisa = ""
    
    if i == 0:
        pesquisa = f"Faca um pequeno texto de um parágrafo e sem titulo iniciando um documento sobre o tema: {tema}. Detalhe: nao formate o texto, deixe apenas texto normal."
    else:
        pesquisa = f"Faca um pequeno texto de um parágrafo e sem titulo sobre o tema: {tema}. Topico: {temasTopicos[i]}. Detalhe: nao formate o texto, deixe apenas texto normal."

    adicionarTitulo = usarChatGPT(pesquisa, adicionarTitulo)

usarChatGPT(finalizacao, adicionarTitulo)