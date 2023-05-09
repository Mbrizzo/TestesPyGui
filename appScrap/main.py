import PySimpleGUI as sg # Interface Gráfica

def main():
    sg.theme('Reddit') # https://www.geeksforgeeks.org/themes-in-pysimplegui/

    layout = [[sg.Text('App Scraping', font='Arial')],
             [sg.Text('Digite o Site:'), sg.Input(key='', size=(45, 1))],
             [sg.Frame('Output', font='Arial', layout=[
             [sg.Output(size=(65, 15), font='Courier 10')]])],
            ]

    window = sg.Window('App Scraping', layout) # cria a janela

    while True: # loop para manter a janela aberta
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

    window.close() # fechar a janela quando o loop terminar
if __name__ == '__main__':
    main()
