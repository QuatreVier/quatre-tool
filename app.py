import time
import os
import colorama
from colorama import *
import sys
import signal

"Funcion para poder reaccionar el ctr+c"
def ctrlc(signal, frame):
    limpiar()
    logo()
    print(Fore.RED+"Precionaste ctrl c, el proceso termino, saliendo...")
    time.sleep(2)
    salida()

signal.signal(signal.SIGINT, ctrlc)

def salida():
    limpiar()
    logo()
    print(f'{Fore.YELLOW} Gracias por usar la herramienta, saliendo...{Fore.RESET}')
    time.sleep(3)
    limpiar()
    sys.exit()

def limpiar():
    if sys.platform == "linux":
        os.system("clear")
    if sys.platform == "win32":
        os.system("cls")
    else: 
        os.system("cls || clear")

def terminado(funcion):
    termino = input(Fore.YELLOW+"El proceso termino que deseas hacer?"+ Fore.GREEN+"\n 1.- Volver al menu \n 2.- Repetir: \n 3.- Salir "+Fore.RESET)
    if termino == "1":
        print(Fore.GREEN+"Volviendo al menu..."+Fore.RESET)
        time.sleep(2)
        index()
    elif termino == "2":
        print(Fore.RED+"Reiniciando..."+Fore.RESET)
        time.sleep(2)
        limpiar()
        funcion()
    elif termino == "3":
        print(Fore.RED+"Saliendo..."+Fore.RESET)
        time.sleep(2)
        salida()    
    else:
        print(Fore.RED+"Eleccion no valida, volviendo al menu..."+Fore.RESET)
        time.sleep(2)    
        index()

def logo():
    print(f'''
  {Fore.RED}    ::::::::  {Fore.CYAN}    :::    :::  {Fore.MAGENTA}         :::  {Fore.GREEN}  :::::::::::{Fore.LIGHTCYAN_EX}       :::::::::       :::::::::: 
  {Fore.RED}  :+:    :+:  {Fore.CYAN}   :+:    :+:   {Fore.MAGENTA}      :+: :+: {Fore.GREEN}     :+:     {Fore.LIGHTCYAN_EX}      :+:    :+:      :+:         
  {Fore.RED} +:+    +:+   {Fore.CYAN}  +:+    +:+    {Fore.MAGENTA}    +:+   +:+ {Fore.GREEN}    +:+      {Fore.LIGHTCYAN_EX}     +:+    +:+      +:+          
  {Fore.RED}+#+    +:+    {Fore.CYAN} +#+    +:+     {Fore.MAGENTA}  +#++:++#++: {Fore.GREEN}   +#+       {Fore.LIGHTCYAN_EX}    +#++:++#:       +#++:++#      
 {Fore.RED}+#+    +#+     {Fore.CYAN}+#+    +#+      {Fore.MAGENTA} +#+     +#+  {Fore.GREEN}  +#+        {Fore.LIGHTCYAN_EX}   +#+    +#+      +#+            
{Fore.RED}#+#    #+#     {Fore.CYAN}#+#    #+#      {Fore.MAGENTA} #+#     #+#   {Fore.GREEN} #+#         {Fore.LIGHTCYAN_EX}  #+#    #+#      #+#             
{Fore.RED}###########    {Fore.CYAN}########       {Fore.MAGENTA} ###     ###   {Fore.GREEN} ###          {Fore.LIGHTCYAN_EX} ###    ###      ##########  
        ''') 
def logo2():
    limpiar()
    print(f"""    
    ──{Fore.LIGHTBLUE_EX}▒▒▒▒▒▒{Fore.WHITE}───{Fore.LIGHTYELLOW_EX}▄████▄{Fore.WHITE}
    ─{Fore.LIGHTBLUE_EX}▒─▄▒─▄▒{Fore.WHITE}──{Fore.LIGHTYELLOW_EX}███▄█▀{Fore.WHITE}
    ─{Fore.LIGHTBLUE_EX}▒▒▒▒▒▒▒{Fore.WHITE}─{Fore.LIGHTYELLOW_EX}▐████{Fore.WHITE}──{Fore.LIGHTYELLOW_EX}█{Fore.WHITE}─{Fore.LIGHTYELLOW_EX}█{Fore.WHITE}
    ─{Fore.LIGHTBLUE_EX}▒▒▒▒▒▒▒{Fore.WHITE}──{Fore.LIGHTYELLOW_EX}█████▄{Fore.WHITE}
    ─{Fore.LIGHTBLUE_EX}▒─▒─▒─▒{Fore.WHITE}───{Fore.LIGHTYELLOW_EX}▀████▀{Fore.WHITE}
    {Fore.RESET}
              """)
def logo3():
    print(f"""
              ¶¶_¶¶  ¶¶ ¶¶
        ¶¶ ¶¶ ¶¶ ¶¶ ¶¶¶ 
     ¶¶¶¶¶            ¶¶¶¶¶¶¶ 
   ¶¶¶¶¶               ¶¶¶¶¶¶¶ 
  ¶¶¶¶¶                  ¶¶¶¶¶ 
  ¶¶¶¶                     ¶¶¶
   ¶¶                       ¶¶¶ 
   ¶                         ¶¶¶¶ 
  ¶¶     ¶¶¶      ¶¶        ¶¶¶¶¶¶¶ 
  ¶     ¶¶¶¶     ¶¶¶¶¶      ¶¶¶¶¶¶ ¶ 
  ¶    ¶¶¶¶¶    ¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶  ¶ 
  ¶¶  ¶¶¶¶¶______¶¶¶¶¶¶¶___¶¶¶¶¶¶¶   ¶ 
   ¶  ¶¶¶__________¶¶¶¶___¶¶¶¶¶¶¶¶¶   ¶ 
   ¶¶____________________¶¶¶¶¶¶¶¶¶¶   ¶¶¶ 
   ¶¶¶_____¶¶¶¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶   ¶¶¶¶ 
   ¶¶¶¶¶___¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶ 
   ¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶ 
   ¶¶¶¶¶¶¶¶  ¶¶¶   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶ 
____¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶ 
____¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶ 
__¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶ 
__¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶¶ 
___¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶ 
___________________¶¶¶¶¶¶¶¶¶¶¶ 
___________________¶¶¶¶¶¶¶¶¶¶ 

    """)
    



def electricidad():
    limpiar()
    logo2()
    print(f'''{Fore.BLUE}
Estas son las opciones de electricidad que tengo{Fore.GREEN}
╔════════╦════════════════╦════════════════════════════════════════════╗
║ Numero ║ Opciones       ║ Descripción                                ║
╠════════╬════════════════╬════════════════════════════════════════════╣
║ 1      ║ Resistencia    ║ Muestra el valor de la resistencia         ║
║ 2      ║ Intensidad     ║ Muestra el valor de la intensidad          ║
║ 3      ║ Voltaje        ║ Muestra el valor de la corriente           ║
║ 4      ║ Volver al menu ║ Volver al menu                             ║
║ 5      ║ Salir          ║ Salir de esta herramienta                  ║
╚════════╩════════════════╩════════════════════════════════════════════╝
         {Fore.RESET} ''')
    eleccion = input("Da una opcion: ")
    if eleccion == 1 or eleccion == "1":
        print("En un momento cargara la opcion...")
        time.sleep(2)
        limpiar()
        resistencia()
    elif eleccion == "2":
        print("En un momento cargara la opcion...")
        time.sleep(2)
        limpiar()
        intensidad()
    elif eleccion == "3":
        print("En un momento cargara la opcion...")
        time.sleep(2)
        limpiar()
        voltaje()
    elif eleccion == "4":
        print("Volviendo al menu...")
        time.sleep(2)
        limpiar()
        index()
    elif eleccion == "5":
        print("Saliendo...")
        time.sleep(2)
        limpiar()
        salida()
    else:
        print("Opcion no valida, selecciona otra")
        time.sleep(2)
        limpiar()
        electricidad()

def resistencia():
    try:
        corriente, intensidad = valores("corriente", "intensidad")
        resis = corriente/intensidad
        print(f'El valor de la resistencia es de {round(resis, 4)} Ω')
        time.sleep(2)
        terminado(resistencia)

    except ValueError:
        print(f'Error al sacar el valor de la resistencia, volviendo... ')
        time.sleep(2)
        limpiar()
        resistencia()

def intensidad():
    try:
        voltaje, resistencia = valores("voltaje", "resistencia")
        inten = voltaje/resistencia
        print(f'El valor de la intensidad es de {round(inten, 4)}A')
        time.sleep(2)
        terminado(intensidad)
    except ValueError:
        print(f'Error al sacar el valor de la intensidad, volviendo...')
        time.sleep(2)
        terminado(intensidad)

def voltaje():
    try:
        intensidad, resistencia = valores("intensidad", "resistencia")
        volt = intensidad * resistencia
        print(f'El valor de la intensidad es de {round(volt, 4)}v')
        time.sleep(2)
    except ValueError:
        print(f'Error al sacar el valor de la intensidad, volviendo...')
        time.sleep(2)
        terminado(voltaje)
 
def valores(cosa1, cosa2):
    while True:
        try:
            valor1 = float(input(f'Ingresa un valor para {cosa1}: '))
            valor2 = float(input(f'Ingresa un valor para {cosa2}: '))
            return valor1, valor2
        except ValueError:
            print(f'Error: Ingresa solo valores numericos') 

def sistema():
    limpiar()
    logo3()
    print(f'''{Fore.BLUE}
Estas son las opciones que tengo{Fore.GREEN}
╔════════╦═══════════════╦════════════════════════════════════════════╗
║ Numero ║ Opciones      ║ Descripción                                ║
╠════════╬══════════════ ╬════════════════════════════════════════════╣
║ 1      ║ Sistema       ║ Muestra algunas configuraciones de sistema ║
║ 2      ║ IP            ║ Algunas configuraciones de IP              ║
║ 3      ║ CPU           ║ Alguna informacion del sistema             ║
║ 4      ║ Salir         ║ Salir de esta herramienta                  ║
╚════════╩═══════════════╩════════════════════════════════════════════╝
{Fore.RESET}
''')

def index():
        limpiar()
        logo()
        print(f'''{Fore.BLUE}
Estas son las opciones que tengo{Fore.GREEN}
╔════════╦═══════════════╦════════════════════════════════════════════╗
║ Numero ║ Opciones      ║ Descripción                                ║
╠════════╬══════════════ ╬════════════════════════════════════════════╣
║ 1      ║ Sistema       ║ Algunos datos de tu computadora            ║
║ 2      ║ Electricidad  ║ Algunas operaciones de electricidad        ║
║ 3      ║ Utilidad      ║ Algunas funciones utiles                   ║
║ 4      ║ Salir         ║ Salir de esta herramienta                  ║
╚════════╩═══════════════╩════════════════════════════════════════════╝
         {Fore.RESET} ''')
        eleccion = input("Da una opcion: ")
        if eleccion == 1 or eleccion == "1":
            print("En un momento cargara la opcion...")
            time.sleep(2)
            limpiar()
            sistema()
        elif eleccion == "2":
            print("En un momento cargara la opcion...")
            time.sleep(2)
            limpiar()
            electricidad()
        elif eleccion == "3":
            print("En un momento cargara la opcion...")
            time.sleep(2)
            limpiar()
            voltaje()
        elif eleccion == "4":
            print("Saliendo...")
            time.sleep(2)
            limpiar()
            salida()
        else:
            print("Opcion no valida, volviendo al menu...")
            time.sleep(2)
            limpiar()
            index()
index()
