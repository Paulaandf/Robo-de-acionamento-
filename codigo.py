#Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://www.smsolucoesdigital.com.br/index.html#/atendimentos/chat
# pip install pyautogui
import pyautogui
import time
pyautogui.PAUSE = 2

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
# abrir o navegador (chrome)

pyautogui.press ("win")
pyautogui.write ("edge")
pyautogui.press("enter")
link ="https://www.smsolucoesdigital.com.br/index.html#/atendimentos/chat"
pyautogui.write (link)
pyautogui.press("enter")
time.sleep(7)
# entrar no link 
import pandas

tabela = pandas.read_excel("base.xlsx")
# Passo 2: Fazer login
for linha in tabela.index:

    # Passo 2: Fazer login
    pyautogui.click (x=411, y=164)
    pyautogui.click (x=554, y=217)
    time.sleep(0.5)
    pyautogui.click (x=554, y=217)
    time.sleep(2)
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.click (x=556, y=364)
    pyautogui.write(str(tabela.loc[linha,"Número Celular"]))
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha,"Nome Candidato"])
    pyautogui.press("tab")
    pyautogui.click (x=638, y=503)
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press("tab")
    pyautogui.click (x=542, y=595)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.click (x=569, y=680)
    pyautogui.write("//")
    pyautogui.press("enter")
    pyautogui.click (x=590, y=596)
    pyautogui.press("space")
    pyautogui.write(str(tabela.loc[linha,"Nome Candidato"]))
    pyautogui.press("enter")
    time.sleep(1.5)

# escrever o seu email
# Passo 3: Importar a base de produtos pra cadastrarx=542, y=480

