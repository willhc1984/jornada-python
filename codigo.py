import pyautogui
import time

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
pyautogui.click(x=840, y=261)
pyautogui.write("1")
pyautogui.press("tab")
pyautogui.write("Samsung")
pyautogui.press("tab")
pyautogui.write("Celular")
pyautogui.press("tab")
pyautogui.write("Eletronico")
pyautogui.press("tab")
pyautogui.write("12,50")
pyautogui.press("tab")
pyautogui.write("10,50")
pyautogui.press("tab")
pyautogui.write("produto teste")
pyautogui.press("tab")
pyautogui.press("enter")

# pyautogui -> cria automações com python