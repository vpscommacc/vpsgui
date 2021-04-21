from tkinter import *
from random import *

window = Tk()
window.title('Game Of Life')
window.minsize(width=500, height=530)
width = 500
height = 500
canvas = Canvas(window, background='white', width=width, height=height)


def create_grid(window):
    for line in range(0, width, 10):  # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

    for line in range(0, height, 10):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')

    canvas.grid(row=0, column=0)


# def dras():
#     nwindo = Toplevel()
#     nwindo.title('Рисовка')
#     x1 = Entry(nwindo, width=5)
#     y1 = Entry(nwindo, width=5)
#     x2 = Entry(nwindo, width=5)
#     y2 = Entry(nwindo, width=5)
#     Label(nwindo, text='x1').place(relx=.1.real, rely=0)
#     x1.place(relx=.2, rely=.0)
#     Label(nwindo, text='y1').place(relx=.5.real, rely=.0)
#     y1.place(relx=.6, rely=.0)
#     Label(nwindo, text='x2').place(relx=.1.real, rely=.1)
#     x2.place(relx=.2, rely=.1)
#     Label(nwindo, text='y2').place(relx=.5.real, rely=.1)
#     y2.place(relx=.6, rely=.1)
#     nwindo.minsize(width=200, height=200)
#     Button(nwindo, text="Нарисовать", width=20).pack(side="bottom")

canvas.create_rectangle(
    100, 100, 200, 300,
    outline="black", fill="white", width=4
)


def xs():
    canvas.create_rectangle(
        100, 240, 160, 300,
        outline="black", fill="red", width=4
    )

def ls():
    canvas.create_rectangle(
        200, 210, 160, 300,
        outline="black", fill="yellow", width=4
    )
    canvas.create_rectangle(
        140, 210, 160, 240,
        outline="black", fill="yellow", width=4
    )

def ks1():
    canvas.create_rectangle(
        100, 170, 140, 240,
        outline="black", fill="blue", width=4
    )
    canvas.create_rectangle(
        100, 170, 140, 240,
        outline="black", fill="blue", width=4
    )

def clear():
    canvas.create_rectangle(
        100, 100, 200, 300,
        outline="black", fill="white", width=4
    )


create_grid(window)
Button(window, text="Квадрат", command=xs).place(relx=.0.real, rely=.943)
Button(window, text="L наоборот", command=ls).place(relx=.172.real, rely=.943)
Button(window, text="1-ый уголок", command=ks1).place(relx=.378.real, rely=.943)
Button(window, text="2-ой уголок", command=ls).place(relx=.606.real, rely=.943)
Button(window, text="Очистка", command=clear).place(relx=.828.real, rely=.943)
window.mainloop()
