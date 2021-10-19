import matplotlib.pyplot as plt
from os import system

x = []
y = []

def creacion_plano():
    print("Dibujemos un plano cartesiano (◠﹏◠)")
    puntox = int(input("Ingrese valor para X: "))
    puntoy = int(input("Ingrese valor para Y: "))

    plt.ion()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(puntox,puntoy,marker="o")

def creacion_grafica():
    x.clear()
    y.clear()
    consultar_numeros(4)
    plt.bar(x,y)

def consultar_numeros(i):
    if i<0:
        return 0
    else:
        valorx = int(input("Ingrese valor para X: "))
        valory = int(input("Ingrese valor para Y: "))
        x.append(valorx)
        y.append(valory)
        return consultar_numeros(i-1)

def run():
    system("clear")
    creacion_plano()
    menu = True
    while menu == True:
        try:
            print('''
                    (★´･д･)ﾉ***- Menú cool -***(｡>ωω<｡)
                    1.-       Crear gráfica (งツ)ว
                    2.- Eliminar contenido de la gráfica
                    3.-    Salir del programa ฅ^-ﻌ-^ฅ
                ''')
            r = int(input("Ingrese una opción: "))
            if r == 1:
                creacion_grafica()
                system("clear")
            elif r == 2:
                system("clear")
                plt.clf()
            elif r == 3:
                menu = False
                print("Adiós y vuelva pronto (⊃｡•́‿•̀｡)⊃")
            else:
                system("clear")
                print("Ingrese una opción válida")
        except:
            system("clear")
            print("Ingrese un caracter correcto")

if __name__=='__main__':
    run()

