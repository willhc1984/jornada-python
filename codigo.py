import pyautogui
import time
import pandas

# Define delay entre comandos
pyautogui.PAUSE = 1.5

# Abrir Chrome e acessar login do site
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Aguardar 3 seg.
time.sleep(3)

# Fazer login
pyautogui.click(x=426, y=376)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.click(x=441, y=470)
pyautogui.write("123")
pyautogui.press("enter")

time.sleep(3)

# Importar a base de dados
tabela = pandas.read_csv("produtos.csv")

pyautogui.click(x=919, y=256)

codigo = "MOLO000251"
pyautogui.write(codigo)

pyautogui.press("tab")
marca = "Logitech"
pyautogui.write(marca)

pyautogui.press("tab")
tipo = "Mouse"
pyautogui.write(tipo)

pyautogui.press("tab")
categoria = "1"
pyautogui.write(categoria)

pyautogui.press("tab")
preco_unitario = "25.95"
pyautogui.write(preco_unitario)

pyautogui.press("tab")
custo = "6.5"
pyautogui.write(custo)

pyautogui.press("tab")
obs = "NaN"
pyautogui.write(obs)

pyautogui.press("tab")
pyautogui.press("enter")

# pyautogui -> cria automações com python