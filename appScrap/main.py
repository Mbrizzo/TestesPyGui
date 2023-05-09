import PySimpleGUI as sg # Interface Gráfica

def main():
    sg.theme('Reddit') # https://www.geeksforgeeks.org/themes-in-pysimplegui/

    layout = [[sg.Text('App Scraping', font='Arial')],
    ]

    window = sg.Window('App Scraping', layout) # cria a janela

    while True: # loop para manter a janela aberta
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

    window.close() # fechar a janela quando o loop terminar
if __name__ == '__main__':
    main()
