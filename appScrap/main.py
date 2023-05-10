import PySimpleGUI as sg # Interface Gráfica
import requests
from bs4 import BeautifulSoup

from scraping import run_program

def main():
    sg.theme('Reddit') # https://www.geeksforgeeks.org/themes-in-pysimplegui/

    layout = [[sg.Text('App Scraping', font='Arial')],
             [sg.Text('Digite a URL:'), sg.Input(key='-URL-', size=(45, 1), default_text='www.example.com'),
               sg.Button('Run', bind_return_key=True), sg.Button('advanced', button_color=('red'), disabled=False),
                 sg.Button('Clear', button_color=('green'), bind_return_key=True)],
              [sg.Text('Palavra Chave:'), sg.Input(key='-KEYWORD-', size=(20, 0.5), default_text='')],
             [sg.Frame('Output', font='Arial', layout=[
             [sg.Output(size=(65, 15), font='Courier 10', key='-OUTPUT-')]])],
             [[sg.Button('Salvar relatório')]],
            ]

    window = sg.Window('App Scraping', layout) # cria a janela

    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Run':
            url = values['-URL-']
            print(f'Scraping website at {url}')

            # Get URL
            texto_extraido = run_program(url, palavra_chave)
            print(texto_extraido)
        
         # Verifica se o botão de salvar foi clicado
        if event == 'Salvar relatório':
        
            # Abre a janela de diálogo de salvamento de arquivo
            filepath = sg.popup_get_file('Salvar relatório como', save_as=True)
        
            # Cria o arquivo de relatório com o conteúdo do scraping
            if filepath:
                with open(filepath, 'w') as f:
                    f.write(conteudo_do_relatorio)
                
            # Verifica se a janela foi fechada
            if event == sg.WIN_CLOSED:
                break

        # Se o usuário clicou no botão Run (Licença)
        if event == "advanced":
            window['advanced'].update(disabled=True)
            sg.popup("Você não possui permissão para usar essa função.")
        # Faz o scraping avançado

            window.close()

if __name__ == '__main__':
    main()