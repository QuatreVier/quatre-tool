import time
import os
import colorama
from colorama import *
import sys
import signal
import webbrowser
import platform
import psutil

# Funcion para detectar control + c
def ctrlc(signal, frame):
    limpiar()
    logo()
    print(Fore.RED+"Precionaste ctrl c, el proceso termino, saliendo...")
    time.sleep(2)
    salida()

signal.signal(signal.SIGINT, ctrlc)

# Funcion para salir de la aplicacion
def salida():
    limpiar()
    logo()
    print(f'{Fore.YELLOW} Gracias por usar la herramienta, saliendo...{Fore.RESET}')
    time.sleep(3)
    limpiar()
    sys.exit()

# Funcion para limpiar la consola
def limpiar():
    if sys.platform == "linux":
        os.system("clear")
    if sys.platform == "win32":
        os.system("cls")
    else: 
        os.system("cls || clear")

# Funcion para cuando termina un proceso
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

# Logos 
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
              ¶¶_¶¶  ¶¶ 
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
  ¶¶  ¶¶¶¶¶      ¶¶¶¶¶¶¶   ¶¶¶¶¶¶¶   ¶ 
   ¶  ¶¶¶          ¶¶¶¶   ¶¶¶¶¶¶¶¶¶   ¶ 
   ¶¶                    ¶¶¶¶¶¶¶¶¶¶   ¶¶¶ 
   ¶¶¶     ¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶¶¶   ¶¶¶¶ 
   ¶¶¶¶¶   ¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶ 
   ¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶ 
   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶ 
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶ 
    ¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶ 
  ¶¶¶¶¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶ 
  ¶¶¶¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶ 
   ¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶¶ 
                   ¶¶¶¶¶¶¶¶¶¶¶ 
                   ¶¶¶¶¶¶¶¶¶¶ 

    """) 
def logooso():
    print(f"""
              ██ █  ██ 
        ██ ██ ██ ██ ███ 
     █████            ███████ 
   █████               ███████ 
  █████                  █████ 
  ████                     ███
   ██                       ███ 
   █                         ████ 
  ██     ███      ██        ███████ 
  █     ████     █████      ██████ █ 
  █    █████    ████████    ██████  █ 
  ██  █████      ███████   ███████   █ 
   █  ███          ████   █████████   █ 
   ██                    ██████████   ███ 
   ███     ██████       ███████████   ████ 
   █████   ██████     █████████████  ██████ 
   ███████         ███████████████  ████████ 
   ████████  ███   ███████████████ █████████ 
    ████████████  ██████████████████████████ 
    █████████████████████████████ ██████████ 
    █████████ ███████ ███████████ ████████ 
  ███████████         ███████████ █████ 
  ██████████          ███████████ 
   ███████         ████████████ 
                   ███████████ 
                   ███████████ 

    """)

# Menu de electricidad 
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

# Funcion para poder aceptar solo numeros 
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
║ 1      ║ Informacion   ║ Muestra alguna informacion de sistema      ║
║ 2      ║ IP            ║ Algunas configuraciones de IP              ║
║ 3      ║ CPU           ║ Alguna informacion del sistema             ║
║ 4      ║ Salir         ║ Salir de esta herramienta                  ║
╚════════╩═══════════════╩════════════════════════════════════════════╝
{Fore.RESET}
''')
    eleccion = input(f'Selecciona una opcion: ')
    if eleccion == "1":
        print(f'En un momento cargara la opcion')
        time.sleep(2)
        informacion()
    elif eleccion == "2":
        print(F'En un momento cargara la opcion... ')
        time.sleep(2)
        ip()
    elif eleccion == "3":
        print("En un momento cargara la opcio....")

# Menu principal de la herramienta
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
def informacion():
    limpiar()
    print(f"""{Fore.GREEN}
╔════════╦═══════════════╦════════════════════════════════════════════╗
║ Numero ║ Opciones      ║ Descripción                                ║
╠════════╬═══════════════╬════════════════════════════════════════════╣
║ 1      ║ Informacion   ║ Muestra informacion basica de la maquina   ║
║ 2      ║ Memeoria      ║ Muestra la memoria total y disponible      ║
║ 3      ║ CPU           ║ Alguna informacion del sistema             ║
║ 4      ║ Salir         ║ Salir de esta herramienta                  ║
╚════════╩═══════════════╩════════════════════════════════════════════╝
          {Fore.RESET}
""")
    elecciones3(infobasica, memoria, cpu)

def infobasica():
    plataforma = platform.uname()
    limpiar()
    print(Fore.LIGHTGREEN_EX)
    print("<" + "=" * 40 + " Informacion Basica Del Sistema " + "=" * 40 + ">")
    print("#")
    print("# Sistema Operativo: ")
    print(f"# {plataforma.system}")
    print(f"#")
    print(f"# Nombre del nodo: ")
    print(f"# {plataforma.node}")
    print(f"#")
    print(f"# Libreria :")
    print(f"# {plataforma.release}")
    print(f"#")
    print(f"# Version")
    print(f"# {plataforma.version}")
    print(f"#")
    print(f"# Procesador")
    print(f"# {plataforma.processor}")
    print(f"#")
    print(f"# Maquina")
    print(f"# {plataforma.machine}")
    print(Fore.RESET)
    print("\n")
    time.sleep(2)
    terminado(infobasica)

def cpu():
    limpiar()
    infobasica()
    cpu = psutil.cpu_freq()
    print(Fore.LIGHTGREEN_EX)
    print("<" + "=" * 39 + " CPU Info " + "=" * 39 + ">")
    print("#")
    print(f"# Procesadores Logicos")
    print("#")
    print(f"# Nucleos Fisicos")
    print(f"# {psutil.cpu_count(logical= False)}")
    print(f"#")
    print(f"# Nucleos Totales")
    print(f"# {psutil.cpu_count(logical=True)}")
    print(f"#")
    print("# Maxima Frecuencia del CPU")
    print(f"# {cpu.max: .2f}Mhz")
    print("#")
    print("# Minima Frecuencia del CPU")
    print(f"# {cpu.min: .2f}Mhz")
    print("#")
    print("# Frecuencia Actual")
    print(f"# {cpu.current: .2f}Mhz")
    print("#")
    print(Fore.RESET)

def memoria():
    limpiar()
    memory = psutil.virtual_memory()
    disponible = memory.total
    print(f"{Fore.LIGHTGREEN_EX}")
    print("<" + "=" * 39 + " Memory Info " + "=" * 39 + ">")
    print("#")
    print("# Total ")
    print(f"# {memory.total :,}")
    print("# Disponible")
    print(f"# {disponible :,}")
    print("#")
    print("# ")
    terminado(memoria)

def ip():
    limpiar()
    logo()
    ip1 = input(Fore.YELLOW+"Introduce una ip: "+Fore.RESET)
    time.sleep(2)
    print(f'''
{Fore.GREEN} Estas son las opciones que tengo para ver la informacion de una ip
          {Fore.CYAN}
┌──────────────────────────────────┬───────────────────────┬───────────┐
│          1.-CheckHost            │   2.-Infobyip         │    3      │
├──────────────────────────────────┼───────────────────────┼───────────│
│  Muestra localización            │  Muestra localización │  Todas    │
│  proveedor, rango, código postal │       proveedor       │   las     │
│  organización y horario          │      código postal    │ anteriores│
└──────────────────────────────────┴───────────────────────┴───────────┘
          {Fore.RESET}''')
    x = input(Fore.RED+"Selecciona una opcion: "+Fore.RESET)
    if x == "1":
        print(Fore.GREEN+"En un momento se abrira en tu naegador la pagina"+Fore.RESET)
        webbrowser.open(f'https://check-host.net/ip-info?host={ip1}')
        time.sleep(3)
        terminado(ip)
    elif x == "2":
        print(Fore.GREEN+"En un momento se abrira en tu navegador la pagina"+Fore.RESET)
        webbrowser.open(f'https://es.infobyip.com/ip-{ip1}.html')
        time.sleep(3)
        terminado(ip)
    elif x == "3":
        print(Fore.GREEN+"En un momento se abriran en tu navegador las paginas"+Fore.RESET)
        webbrowser.open(f'https://check-host.net/ip-info?host={ip1}')   
        webbrowser.open(f'https://es.infobyip.com/ip-{ip1}.html')
        time.sleep(3)
        terminado(ip)

def elecciones3(f1, f2, f3):
    eleccion = input(f'Selecciona una opcion: ')
    if eleccion == "1":
        print(f'En un momento cargara la opcion')
        time.sleep(2)
        f1()
    elif eleccion == "2":
        print(F'En un momento cargara la opcion... ')
        time.sleep(2)
        f2()
    elif eleccion == "3":
        print("En un momento cargara la opcion....")
        time.sleep(2)
        f3()
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

def elecciones4(f1, f2, f3, f4):
    eleccion = input(f'Selecciona una opcion: ')
    if eleccion == "1":
        print(f'En un momento cargara la opcion')
        time.sleep(2)
        f1()
    elif eleccion == "2":
        print(F'En un momento cargara la opcion... ')
        time.sleep(2)
        f2()
    elif eleccion == "3":
        print("En un momento cargara la opcion....")
        time.sleep(2)
        f3()
    elif eleccion == "4":
        print("En un momento cargara la opcion....")
        time.sleep(2)
        f4()    
    elif eleccion == "5":
        print("Saliendo...")
        time.sleep(2)
        limpiar()
        salida()
    else:
        print("Opcion no valida, volviendo al menu...")
        time.sleep(2)
        limpiar()
        index()

# Iniciamos con el menu principal
index()
