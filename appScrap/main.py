import PySimpleGUI as sg # Interface Gráfica
import requests
from bs4 import BeautifulSoup

from functions import get_website_text


def main():
    sg.theme('Reddit') # https://www.geeksforgeeks.org/themes-in-pysimplegui/

    layout = [[sg.Text('App Scraping', font='Arial')],
             [sg.Text('Digite a URL:'), sg.Input(key='-URL-', size=(45, 1), default_text='www.example.com'),
               sg.Button('Run', bind_return_key=True)],
              [sg.Text('Buscar Palavra:'), sg.Input(key='-KEYWORD-', size=(20, 0.5), default_text=''),
              sg.Button('Filter', bind_return_key=True)], 
             [sg.Frame('Output', font='Arial', layout=[
             [sg.Output(size=(65, 15), font='Courier 10', key='-OUTPUT-')]])],
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
            texto_extraido = get_website_text(url)
            print(texto_extraido)

    window.close()

if __name__ == '__main__':
    main()