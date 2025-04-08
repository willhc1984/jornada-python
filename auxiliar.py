import pyautogui
import time
import pandas

time.sleep(5)
print(pyautogui.position())

# Importar a base de dados
tabela = pandas.read_csv("produtos.csv")

print(tabela)