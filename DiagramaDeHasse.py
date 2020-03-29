# -*- coding: UTF-8 -*-


from random import randrange
from Tkinter import *
import ttk
from sympy import FiniteSet
import tkMessageBox
import sys
import random

sys.setrecursionlimit(5000)

def Restart():
        lblResultadoSubconjunto.destroy()
        my_canvas.destroy()
        lblResultadoParesOrdenados.destroy()
        lblParesOrdenados.destroy()




def divisores(numeroNat):
    factores = []

    for i in range(1, numeroNat // 2 + 1):
        if numeroNat % i == 0:
            factores.append(i)
    factores.append(numeroNat)

    return factores

def ParesOrdenados(vector1):
    vectorResultado = ''

    for j in range(len(vector1)):
        for i in range(len(vector1)):
            vectorResultado += '(' + str(vector1[j]) + ',' + str(vector1[i]) + ')'

    return vectorResultado

def CheckRandomValuesisTrue():
    global divisoresDe


    if chkRandomValues.get():
        divisoresDe = randrange(2,40)
        txtBoxNumeroNatN.insert(0, divisoresDe)
        txtBoxNumeroNatN.config(state = 'disabled')
    else:
        txtBoxNumeroNatN.config(state = 'normal')
        txtBoxNumeroNatN.delete(first = 0, last = 50)

def ChangeToDarkMode():
    frame.config(background = backgroundColorDark[0])
    my_canvas.config(background = backgroundColorDark[0])
    Window.config( background=backgroundColorDark[1])
    lblResultadoSubconjunto.config(background=backgroundColorDark[0])
    chk.config(background=backgroundColorDark[1])
    style.configure('TLabel',
                background = backgroundColorDark[0],
                )
    lblNumeronaturalN.config(background=backgroundColorDark[1])

def ChangeToWhiteMode():
    frame.config(background = backgroundColorWhite[0])
    my_canvas.config(background = backgroundColorWhite[0])
    Window.config( background=backgroundColorWhite[1])
    lblResultadoSubconjunto.config(background=backgroundColorWhite[0])
    chk.config(background=backgroundColorWhite[1])
    style.configure('TLabel',
                background = backgroundColorWhite[0],
                )
    lblNumeronaturalN.config(background=backgroundColorWhite[1])

def ImprimirParesOrdenados(paresOrdenados):

    a = paresOrdenados[0:74]
    a2 = paresOrdenados[74:148]
    a3 = paresOrdenados[148:233]
    a4 = paresOrdenados[233:310]
    a5 = paresOrdenados[310:381]
    a6 = paresOrdenados[381:1000]

    return a + '\n' + a2+ '\n' + a3 + '\n' + a4 + '\n' + a5 + '\n' + a6

def ordenar(a):
    n=len(a)
    flag=False
    i=0
    while i<n or flag==False:
        i+=1
        flag = True
        for j in range(n-i):
            if a[j]>a[j+1]:
                flag=False
                aux=a[j+1]
                a[j+1]=a[j]
                a[j]=aux
    return a

def Graphic(event = None):
    def GraficarDiagramaHASSE(number, SubconjuntoGenerado):

        def CreateLineCanvas(canvas, x1, y1, x2, y2):
            colorLine = '#000'
            return canvas.create_line(x1, y1, x2, y2, fill = colorLine, width = 3)

        def create_circle(x, y, canvasName): #center coordinates, radius
            r = 4
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r
            return canvasName.create_oval(x0, y0, x1, y1, fill="#000")

        def create_text(x, y, canvasName, text):
            colorText = '#fff'
            return canvasName.create_text(x, y, text = text, fill = colorText, font=("Arial Bold", 12))

        def GenGraphicType(sub,canvasName, type):
            
            if type == 1:
                ## Circles
                create_circle(120, 6, canvasName)   # Punto alto
                create_circle(120, 82, canvasName)  # Punto medio
                create_circle(120, 175, canvasName) # Punto bajo
                ## Line
                CreateLineCanvas(canvasName, 120, 180, 120, 2)
                ## Text
                create_text(110, 8, canvasName, sub[2])   # Texto alto
                create_text(110, 84, canvasName, sub[1])  # Texto medio
                create_text(110, 179, canvasName, sub[0]) # Texto bajo


            elif type == 2:
                create_text(120, 200, canvasName, sub[0])
                create_text(35, 115, canvasName, sub[1])
                CreateLineCanvas(canvasName, 120, 220, 40, 135)
                create_circle(120, 217, canvasName)
                create_circle(40, 135, canvasName)
                create_text(217, 115, canvasName, sub[2])
                CreateLineCanvas(canvasName, 120, 220, 210, 135)
                create_circle(210, 135, canvasName)
                CreateLineCanvas(canvasName, 210, 135, 120, 40)
                create_circle(120, 40, canvasName)
                CreateLineCanvas(canvasName, 40, 135, 120, 40)
                create_text(120, 25, canvasName, sub[3])


        global my_canvas

        my_canvas = Canvas(Window, width = 230, height = 230, background=backgroundColorWhite, highlightthickness=0, relief='ridge')

        my_canvas.place(x = lblResultado_X + 210, y = 330)

        if ((2** (number - 1)) % number) == 1 or number == 2:
            CreateLineCanvas(my_canvas, 120, 180, 120, 60)
            create_circle(120, 175, my_canvas)
            create_text(120, 188, my_canvas, SubconjuntoGenerado[0])
            create_text(120, 46, my_canvas, SubconjuntoGenerado[1])
            create_circle(120, 58, my_canvas)
        else:
            if number == 4 or number == 9 or number == 25:
                GenGraphicType(SubconjuntoGenerado, my_canvas, 1)
            elif number == 6 or number == 10 or number == 14 or number == 15 or number == 21 or number == 22 or number == 26 or number == 33 or number == 34 or number == 35 or number == 38 or number == 39:
                GenGraphicType(SubconjuntoGenerado, my_canvas, 2)
            elif number == 8:
                create_circle(120, 4, my_canvas)
                create_circle(120, 63, my_canvas)
                create_circle(120, 115, my_canvas)
                create_circle(120, 175, my_canvas)
                CreateLineCanvas(my_canvas, 120, 180, 120, 2)
                create_text(110, 7, my_canvas, SubconjuntoGenerado[3])
                create_text(110, 63, my_canvas, SubconjuntoGenerado[2])
                create_text(110, 115, my_canvas, SubconjuntoGenerado[1])
                create_text(110, 175, my_canvas, SubconjuntoGenerado[0])
            elif number == 12:
                CreateLineCanvas(my_canvas, 120,190,65,145)
                create_circle(120, 190, my_canvas)
                create_text(120, 175, my_canvas, SubconjuntoGenerado[0])
                create_circle(65, 145, my_canvas)
                create_text(50, 145, my_canvas, SubconjuntoGenerado[1])
                CreateLineCanvas(my_canvas, 120,190,175,145)
                create_text(190, 145, my_canvas, SubconjuntoGenerado[3])
                create_circle(175, 145, my_canvas)
                CreateLineCanvas(my_canvas, 65,145,65,50)
                create_text(50, 50, my_canvas, SubconjuntoGenerado[2])
                CreateLineCanvas(my_canvas, 175, 50, 65, 145)
                create_circle(65, 50, my_canvas)
                CreateLineCanvas(my_canvas, 175,145,175,50)
                create_text(190, 50, my_canvas, SubconjuntoGenerado[4])
                create_circle(175, 50, my_canvas)
                CreateLineCanvas(my_canvas, 175,50,120,4)
                create_text(120, 21, my_canvas, SubconjuntoGenerado[5])
                create_circle(120, 4, my_canvas)
                CreateLineCanvas(my_canvas, 120,4,65,50)

            elif number == 16:
                CreateLineCanvas(my_canvas, 120, 220, 120, 5)
                create_circle(120, 220, my_canvas)
                create_circle(120, 165, my_canvas)
                create_circle(120, 110, my_canvas)
                create_circle(120, 55, my_canvas)
                create_circle(120, 5, my_canvas)
                create_text(110, 220, my_canvas, SubconjuntoGenerado[0])
                create_text(110, 165, my_canvas, SubconjuntoGenerado[1])
                create_text(110, 110, my_canvas, SubconjuntoGenerado[2])
                create_text(110, 55, my_canvas, SubconjuntoGenerado[3])
                create_text(110, 7, my_canvas, SubconjuntoGenerado[4])
            elif number == 18:
                CreateLineCanvas(my_canvas, 120,190,65,145)
                create_circle(120, 190, my_canvas)
                create_text(120, 175, my_canvas, SubconjuntoGenerado[0])
                create_circle(65, 145, my_canvas)
                create_text(50, 145, my_canvas, SubconjuntoGenerado[1])
                CreateLineCanvas(my_canvas, 120,190,175,145)
                create_text(190, 145, my_canvas, SubconjuntoGenerado[2])
                create_circle(175, 145, my_canvas)
                CreateLineCanvas(my_canvas, 65,145,65,50)

                create_text(50, 50, my_canvas, SubconjuntoGenerado[3])
                CreateLineCanvas(my_canvas, 65, 50, 175, 145)
                create_circle(65, 50, my_canvas)
                CreateLineCanvas(my_canvas, 175,145,175,50)
                create_text(190, 50, my_canvas, SubconjuntoGenerado[4])
                create_circle(175, 50, my_canvas)
                CreateLineCanvas(my_canvas, 175,50,120,4)
                create_text(120, 21, my_canvas, SubconjuntoGenerado[5])
                create_circle(120, 4, my_canvas)
                CreateLineCanvas(my_canvas, 120,4,65,50)
            elif number == 20:
                CreateLineCanvas(my_canvas, 120,190,65,145)
                create_circle(120, 190, my_canvas)
                create_text(120, 175, my_canvas, SubconjuntoGenerado[0])
                create_circle(65, 145, my_canvas)
                create_text(50, 145, my_canvas, SubconjuntoGenerado[1])
                CreateLineCanvas(my_canvas, 120,190,175,145)
                create_text(190, 145, my_canvas, SubconjuntoGenerado[3])
                create_circle(175, 145, my_canvas)
                CreateLineCanvas(my_canvas, 65,145,65,50)
                create_text(50, 50, my_canvas, SubconjuntoGenerado[2])
                CreateLineCanvas(my_canvas, 175, 50, 65, 145)
                create_circle(65, 50, my_canvas)
                CreateLineCanvas(my_canvas, 175,145,175,50)
                create_text(190, 50, my_canvas, SubconjuntoGenerado[4])
                create_circle(175, 50, my_canvas)
                CreateLineCanvas(my_canvas, 175,50,120,4)
                create_text(120, 21, my_canvas, SubconjuntoGenerado[5])
                create_circle(120, 4, my_canvas)
                CreateLineCanvas(my_canvas, 120,4,65,50)

            elif number == 24:
                CreateLineCanvas(my_canvas, 120, 220, 70, 190)
                CreateLineCanvas(my_canvas, 70, 190, 170, 140)
                create_circle(120, 220, my_canvas)
                create_circle(70, 190, my_canvas)
                CreateLineCanvas(my_canvas, 120, 220, 170, 190)
                CreateLineCanvas(my_canvas, 70, 140, 170, 90)
                CreateLineCanvas(my_canvas, 70, 190, 170, 140)
                create_circle(170, 190, my_canvas)
                CreateLineCanvas(my_canvas, 170, 190, 170, 140)
                CreateLineCanvas(my_canvas, 70, 190, 70, 140)
                create_circle(170, 140, my_canvas)
                create_circle(70, 140, my_canvas)
                CreateLineCanvas(my_canvas, 170, 140, 170, 90)
                CreateLineCanvas(my_canvas, 70, 140, 70, 90)
                create_circle(170, 90, my_canvas)
                create_circle(70, 90, my_canvas)
                CreateLineCanvas(my_canvas, 70, 90, 120, 60)
                CreateLineCanvas(my_canvas, 170, 90, 120, 60)
                create_circle(120, 60, my_canvas)
                create_text(120, 205, my_canvas, SubconjuntoGenerado[0])
                create_text(60, 190, my_canvas, SubconjuntoGenerado[1])
                create_text(180, 190, my_canvas, SubconjuntoGenerado[2])
                create_text(60, 140, my_canvas, SubconjuntoGenerado[3])
                create_text(180, 140, my_canvas, SubconjuntoGenerado[4])
                create_text(60, 90, my_canvas, SubconjuntoGenerado[5])
                create_text(185, 90, my_canvas, SubconjuntoGenerado[6])
                create_text(120, 75, my_canvas, SubconjuntoGenerado[7])

            elif number == 27:
                create_circle(120, 4, my_canvas)
                create_circle(120, 63, my_canvas)
                create_circle(120, 115, my_canvas)
                create_circle(120, 175, my_canvas)
                CreateLineCanvas(my_canvas, 120, 180, 120, 2)
                create_text(110, 7, my_canvas, SubconjuntoGenerado[3])
                create_text(110, 63, my_canvas, SubconjuntoGenerado[2])
                create_text(110, 115, my_canvas, SubconjuntoGenerado[1])
                create_text(110, 175, my_canvas, SubconjuntoGenerado[0])
            elif number == 28:
                CreateLineCanvas(my_canvas, 120,190,65,145)
                create_circle(120, 190, my_canvas)
                create_text(120, 175, my_canvas, SubconjuntoGenerado[0])
                create_circle(65, 145, my_canvas)
                create_text(50, 145, my_canvas, SubconjuntoGenerado[1])
                CreateLineCanvas(my_canvas, 120,190,175,145)
                create_text(190, 145, my_canvas, SubconjuntoGenerado[3])
                create_circle(175, 145, my_canvas)
                CreateLineCanvas(my_canvas, 65,145,65,50)
                create_text(50, 50, my_canvas, SubconjuntoGenerado[2])
                CreateLineCanvas(my_canvas, 175, 50, 65, 145)
                create_circle(65, 50, my_canvas)
                CreateLineCanvas(my_canvas, 175,145,175,50)
                create_text(190, 50, my_canvas, SubconjuntoGenerado[4])
                create_circle(175, 50, my_canvas)
                CreateLineCanvas(my_canvas, 175,50,120,4)
                create_text(120, 21, my_canvas, SubconjuntoGenerado[5])
                create_circle(120, 4, my_canvas)
                CreateLineCanvas(my_canvas, 120,4,65,50)
            elif number == 30:
                CreateLineCanvas(my_canvas, 80, 220, 180, 130)
                CreateLineCanvas(my_canvas, 80, 220, 20, 160)
                CreateLineCanvas(my_canvas, 80, 220, 80, 160)
                CreateLineCanvas(my_canvas, 20, 160, 25, 80)
                CreateLineCanvas(my_canvas, 25, 80, 80, 160)
                CreateLineCanvas(my_canvas, 180, 130, 145, 70)
                CreateLineCanvas(my_canvas, 180, 130, 190, 70)
                CreateLineCanvas(my_canvas, 190, 70, 145, 4)
                CreateLineCanvas(my_canvas, 145, 70, 145, 4)
                CreateLineCanvas(my_canvas, 25, 80, 145, 4)
                CreateLineCanvas(my_canvas, 20, 160, 145, 70)
                create_circle(80, 220, my_canvas)
                create_circle(180, 130, my_canvas)
                create_circle(80, 160, my_canvas)
                create_circle(20, 160, my_canvas)
                create_circle(25, 80, my_canvas)
                create_circle(145, 70, my_canvas)
                create_circle(190, 70, my_canvas)
                create_circle(145, 4, my_canvas)
                create_circle(145, 70, my_canvas)
                create_circle(20, 160, my_canvas)
                create_text(70, 220, my_canvas, SubconjuntoGenerado[0])
                create_text(10, 160, my_canvas, SubconjuntoGenerado[1])
                create_text(90, 160, my_canvas, SubconjuntoGenerado[2])
                create_text(190, 130, my_canvas, SubconjuntoGenerado[3])
                create_text(25, 67, my_canvas, SubconjuntoGenerado[4])
                create_text(135, 65, my_canvas, SubconjuntoGenerado[5])
                create_text(204, 70, my_canvas, SubconjuntoGenerado[6])
                create_text(160, 7, my_canvas, SubconjuntoGenerado[7])

            elif number == 32:
                CreateLineCanvas(my_canvas, 120, 220, 120, 5)
                create_circle(120, 220, my_canvas)
                create_circle(120, 176, my_canvas)
                create_circle(120, 132, my_canvas)
                create_circle(120, 88, my_canvas)
                create_circle(120, 44, my_canvas)
                create_circle(120, 5, my_canvas)
                create_text(110, 220, my_canvas, SubconjuntoGenerado[0])
                create_text(110, 176, my_canvas, SubconjuntoGenerado[1])
                create_text(110, 132, my_canvas, SubconjuntoGenerado[2])
                create_text(110, 88, my_canvas, SubconjuntoGenerado[3])
                create_text(105, 44, my_canvas, SubconjuntoGenerado[4])
                create_text(105, 7, my_canvas, SubconjuntoGenerado[5])

            elif number == 36:
                create_text(120, 200, my_canvas, SubconjuntoGenerado[0])
                create_text(40, 115, my_canvas, SubconjuntoGenerado[3])
                CreateLineCanvas(my_canvas, 120, 220, 30, 115)
                create_circle(120, 217, my_canvas)
                create_circle(30, 115, my_canvas)

                create_text(192, 115, my_canvas, SubconjuntoGenerado[5])
                CreateLineCanvas(my_canvas, 120, 220, 200, 115)
                create_circle(120, 115, my_canvas)
                create_circle(200, 115, my_canvas)


                create_text(120, 129, my_canvas,SubconjuntoGenerado[4])
                create_text(70, 174, my_canvas,SubconjuntoGenerado[1])
                CreateLineCanvas(my_canvas, 75, 166, 120, 115)
                create_circle(75, 166, my_canvas)

                create_text(166, 170, my_canvas, SubconjuntoGenerado[2])
                CreateLineCanvas(my_canvas, 160, 166, 120, 115)
                create_circle(160, 166, my_canvas)

                create_text(120, 9, my_canvas,SubconjuntoGenerado[8])
                CreateLineCanvas(my_canvas, 30, 115, 120, 15)
                create_circle(120, 19, my_canvas)

                CreateLineCanvas(my_canvas, 120, 15, 200, 115)

                create_text(169, 66, my_canvas,SubconjuntoGenerado[7])
                CreateLineCanvas(my_canvas, 120, 115, 160, 65)
                create_circle(160, 65, my_canvas)

                create_text(67, 58, my_canvas, SubconjuntoGenerado[6])
                CreateLineCanvas(my_canvas, 120, 115, 75, 65)
                create_circle(75, 65, my_canvas)

            elif number == 40:
                CreateLineCanvas(my_canvas, 120, 220, 70, 190)
                CreateLineCanvas(my_canvas, 70, 190, 170, 140)
                create_circle(120, 220, my_canvas)
                create_circle(70, 190, my_canvas)
                CreateLineCanvas(my_canvas, 120, 220, 170, 190)
                CreateLineCanvas(my_canvas, 70, 140, 170, 90)
                CreateLineCanvas(my_canvas, 70, 190, 170, 140)
                create_circle(170, 190, my_canvas)
                CreateLineCanvas(my_canvas, 170, 190, 170, 140)
                CreateLineCanvas(my_canvas, 70, 190, 70, 140)
                create_circle(170, 140, my_canvas)
                create_circle(70, 140, my_canvas)
                CreateLineCanvas(my_canvas, 170, 140, 170, 90)
                CreateLineCanvas(my_canvas, 70, 140, 70, 90)
                create_circle(170, 90, my_canvas)
                create_circle(70, 90, my_canvas)
                CreateLineCanvas(my_canvas, 70, 90, 120, 60)
                CreateLineCanvas(my_canvas, 170, 90, 120, 60)
                create_circle(120, 60, my_canvas)
                create_text(120, 205, my_canvas, SubconjuntoGenerado[0])
                create_text(60, 190, my_canvas, SubconjuntoGenerado[1])
                create_text(180, 190, my_canvas, SubconjuntoGenerado[3])
                create_text(60, 140, my_canvas, SubconjuntoGenerado[2])
                create_text(180, 140, my_canvas, SubconjuntoGenerado[5])
                create_text(60, 90, my_canvas, SubconjuntoGenerado[4])
                create_text(185, 90, my_canvas, SubconjuntoGenerado[6])
                create_text(120, 75, my_canvas, SubconjuntoGenerado[7])


    global divisoresDe, SubconjuntoGenerado, lblResultadoSubconjunto
    global lblParesOrdenados, lblResultadoParesOrdenados, lblNumeronaturalN


    if chkRandomValues.get():
        pass
    else:
        divisoresDe = int(txtBoxNumeroNatN.get())

    if int(txtBoxNumeroNatN.get()) < 2:
        tkMessageBox.showerror("Error de entrada", "Coloque un numero mayor o igual que 2.")
    elif int(txtBoxNumeroNatN.get()) > 40:
        tkMessageBox.showerror("Error de entrada", "Coloque un numero menor o igual que 40.")
    else:
        SubconjuntoGeneradoSinOrdenar = divisores(divisoresDe)
        SubconjuntoGenerado = ordenar(SubconjuntoGeneradoSinOrdenar)
        SubconjuntoDFormatedTemp = str(SubconjuntoGenerado).replace('[', '').replace(']', '')
        SubconjuntoDFormated = str(FiniteSet(SubconjuntoDFormatedTemp)).replace('(', '').replace(')', '')

        _ParesOrdenados = ParesOrdenados(SubconjuntoGenerado)
        lblResultado_X = 10


        lblResultadoSubconjunto = ttk.Label(Window, text='Sub. D(' + str(divisoresDe) + ') = ' + SubconjuntoDFormated, style='TLabel')
        lblResultadoSubconjunto.place(x = lblResultado_X, y =  130)

        lblParesOrdenados = ttk.Label(Window, text='Pares Ordenados: ', style='TLabel')
        lblParesOrdenados.place(x = lblResultado_X, y =  165)

        lblResultadoParesOrdenados = ttk.Label(Window, text=ImprimirParesOrdenados(_ParesOrdenados), style='TLabel')
        lblResultadoParesOrdenados.place(x = lblResultado_X, y =  190)

        GraficarDiagramaHASSE(divisoresDe, SubconjuntoGenerado)

###################### GUI CONFIG ######################

anchoVentana = 700
altoVentana = 600

Window = Tk()

Window.title("Diagrama de hasse | App")
Window.resizable(0,0)
Window.geometry(str(anchoVentana)+'x'+str(altoVentana)) #Tamano de la ventana
Window.iconbitmap('dist/images/Icon.ico')
Window.config(background='#5791D2')

backgroundColorWhite, backgroundColorDark  = ['#456185', '#0A77AC'], ['#3C444D','#6E6E6E']

frame = Frame(Window)
frame.config(bg=backgroundColorWhite)
frame.config(width=anchoVentana, height=500) #Altura frame
frame.place(x = 0, y = 120)

MenuBar = Menu(Window)

ConfiguracionMenu = Menu(MenuBar, tearoff=0)
ConfiguracionMenu.add_command(label="Cambiar a modo oscuro", command= ChangeToDarkMode)
ConfiguracionMenu.add_command(label="Cambiar a modo claro", command= ChangeToWhiteMode)
MenuBar.add_cascade(label="Apariencia", menu=ConfiguracionMenu)

Window.config(menu=MenuBar)


lblNumeronaturalN= Label(Window, text="Ingrese el Numero Natural N: ", font=("Arial Bold", 12), background='#5791D2')
lblNumeronaturalN.place(x = 10, y = 12)

txtBoxNumeroNatN = Entry(Window,width=3)
txtBoxNumeroNatN.place(x = 228, y = 14)

style = ttk.Style()

style.configure('TButton',
                font = ('calibri', 12, 'bold'),
                borderwidth = '2',
                background='black',
                fg = '#D46308',
                color = '#D46308'
                )

style.configure('TLabel',
                font= ('Arial Bold', 14),
                borderwidth = '0',
                background=backgroundColorWhite[0],
                fill = '#ffffff',
                )

btnCoordX = 450
btnCoordY = 10

btnGraficar = Button(Window, text="Graficar", command=Graphic, bg='#DAD5D5',fg='#474747',  relief='ridge', font = ('calibri', 12, 'bold'), width = 24)
btnGraficar.place(x = btnCoordX, y = btnCoordY)

Window.bind('<Return>', Graphic) #Funcion enter




btnReiniciar = Button(Window, text="Reiniciar", command=Restart, bg='#DAD5D5',fg='#474747',  relief='ridge', font = ('calibri', 12, 'bold'), width = 24)
btnReiniciar.place(x = btnCoordX, y = btnCoordY + 40)


lblResultadoSubconjunto = Label(Window)
my_canvas = Canvas(Window)


chkRandomValues = BooleanVar()
chkRandomValues.set(False)
chk = Checkbutton(Window, background='#5791D2', text='Valores aleatorios', var=chkRandomValues, command = CheckRandomValuesisTrue)
chk.place(x = 8, y = 51)

################## END GUI CONFIG #######################

if __name__ == "__main__":
    CheckRandomValuesisTrue()
    Window.mainloop()
