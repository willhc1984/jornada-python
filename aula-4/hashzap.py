# pip install flet - framework Python
# importar flet - criar função principal do app - rodar projeto

import flet as ft

def main(pagina):
    # criar elementos
    titulo = ft.Text("HashZap")
    botao_iniciar = ft.ElevatedButton("Iniciar Chat")
    #colocar elementos na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)
ft.app(main)

