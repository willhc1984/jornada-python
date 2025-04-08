import pyautogui
import time
import pandas

# Define delay entre comandos
pyautogui.PAUSE = 0.5

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

# Cadastra os produtos no arquivo csv
for linha in tabela.index:
    pyautogui.click(x=919, y=256)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))

    pyautogui.press("tab")
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))

    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))

    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]

    if obs != "NaN":
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)


# pyautogui -> cria automações com python