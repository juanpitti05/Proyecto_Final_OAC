from tkinter import *
from tkinter import messagebox

def crearBoton(valor, i):
    return Button(frame_botones, text=valor, width=5, height=1, font=("Helvetica", 15),
                  command=lambda: botonClick(i))

def mostrar_coordenadas(z, y, x):
    texto_x.config(text=f"X={x}", fg="green")
    texto_y.config(text=f"Y={y}", fg="green")
    texto_z.config(text=f"Z={z}", fg="green")

def limpiar_mensajes():
    texto_msg.config(text="")

def botonClick(i):
    global jugador, jugadas, X, Y, Z, g
    Z = int(i / 16)
    Y = int((i % 16) / 4)
    X = i % 4

    mostrar_coordenadas(Z, Y, X)
    limpiar_mensajes()
    if g:
        return
    if jugadas[Z][Y][X] != 0:
        texto_msg.config(text="Jugada Inválida", fg="red")
        return

    if jugador == 0:
        jugadas[Z][Y][X] = 1
        botones[i].config(text="X", font="arial 15", fg="blue", bg="white")
    else:
        jugadas[Z][Y][X] = -1
        botones[i].config(text="O", font="arial 15", fg="red", bg="white")

    lineas = [horizontal(), vertical(), profundidad(),
              diagonal_frontal_1(), diagonal_frontal_2(),
              diagonal_vertical_1(), diagonal_vertical_2(),
              diagonal_horizontal_1(), diagonal_horizontal_2(),
              diagonal_cruzada_1(), diagonal_cruzada_2(),
              diagonal_cruzada_3(), diagonal_cruzada_4()]
    for linea in lineas:
        if linea is not None:
            resaltar_ganadora(linea)
            ganador()
            return

    jugador = 1 - jugador
    texto_turno.config(text="Jugador " + str(jugador + 1), fg="green")

def resaltar_ganadora(coords):
    for (z, y, x) in coords:
        i = z*16 + y*4 + x
        botones[i].config(bg="red")

def ganador():
    global jugador, g
    texto_msg.config(text="Jugador " + str(jugador + 1) + " GANO", fg="blue")
    g = 1

def reiniciar():
    global jugadas, jugador, g, X, Y, Z
    jugadas = [[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
               [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
               [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
               [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
    jugador = 0
    g = 0
    X = Y = Z = 0
    for b in range(64):
        botones[b].config(text=" ", fg="black", bg="SystemButtonFace")
    texto_turno.config(text="Jugador 1", fg="green")
    texto_msg.config(text="")
    mostrar_coordenadas(0, 0, 0)

def salir():
    if messagebox.askyesno("FINALIZAR", "¿Quieres continuar?"):
        reiniciar()
    else:
        tablero.destroy()

# ——— Funciones de línea que devuelven coords o None ———
def horizontal():
    for z in range(4):
        for y in range(4):
            s, coords = 0, []
            for x in range(4):
                s += jugadas[z][y][x]
                coords.append((z, y, x))
            if abs(s) == 4:
                return coords
    return None

def vertical():
    for z in range(4):
        for x in range(4):
            s, coords = 0, []
            for y in range(4):
                s += jugadas[z][y][x]
                coords.append((z, y, x))
            if abs(s) == 4:
                return coords
    return None

def profundidad():
    for y in range(4):
        for x in range(4):
            s, coords = 0, []
            for z in range(4):
                s += jugadas[z][y][x]
                coords.append((z, y, x))
            if abs(s) == 4:
                return coords
    return None

def diagonal_frontal_1():
    for z in range(4):
        s, coords = 0, []
        for i in range(4):
            s += jugadas[z][i][i]
            coords.append((z, i, i))
        if abs(s) == 4:
            return coords
    return None

def diagonal_frontal_2():
    for z in range(4):
        s, coords = 0, []
        for i in range(4):
            s += jugadas[z][i][3 - i]
            coords.append((z, i, 3 - i))
        if abs(s) == 4:
            return coords
    return None

def diagonal_vertical_1():
    for x in range(4):
        s, coords = 0, []
        for i in range(4):
            s += jugadas[i][i][x]
            coords.append((i, i, x))
        if abs(s) == 4:
            return coords
    return None

def diagonal_vertical_2():
    for x in range(4):
        s, coords = 0, []
        for i in range(4):
            s += jugadas[3 - i][i][x]
            coords.append((3 - i, i, x))
        if abs(s) == 4:
            return coords
    return None

def diagonal_horizontal_1():
    for y in range(4):
        s, coords = 0, []
        for i in range(4):
            s += jugadas[i][y][i]
            coords.append((i, y, i))
        if abs(s) == 4:
            return coords
    return None

def diagonal_horizontal_2():
    for y in range(4):
        s, coords = 0, []
        for i in range(4):
            s += jugadas[3 - i][y][i]
            coords.append((3 - i, y, i))
        if abs(s) == 4:
            return coords
    return None

def diagonal_cruzada_1():
    s, coords = 0, []
    for i in range(4):
        s += jugadas[3 - i][i][i]
        coords.append((3 - i, i, i))
    if abs(s) == 4:
        return coords
    return None

def diagonal_cruzada_2():
    s, coords = 0, []
    for i in range(4):
        s += jugadas[i][3 - i][i]
        coords.append((i, 3 - i, i))
    if abs(s) == 4:
        return coords
    return None

def diagonal_cruzada_3():
    s, coords = 0, []
    for i in range(4):
        s += jugadas[i][i][3 - i]
        coords.append((i, i, 3 - i))
    if abs(s) == 4:
        return coords
    return None

def diagonal_cruzada_4():
    s, coords = 0, []
    for i in range(4):
        s += jugadas[i][i][i]
        coords.append((i, i, i))
    if abs(s) == 4:
        return coords
    return None

# —— INICIALIZACIÓN TABLERO ——
jugadas = [[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
           [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
           [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
           [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
X = Y = Z = 0
jugador = 0
g = 0

tablero = Tk()
tablero.title('Tic Tac Toe 3D')
tablero.geometry("1040x720+100+5")
tablero.resizable(0, 0)

canvas = Canvas(tablero, width=1040, height=680)
canvas.pack()

# Frame para los botones del cubo 3D
frame_botones = Frame(tablero)
frame_botones.place(x=0, y=0, width=1040, height=640)

for z in range(4):
    for y in range(4):
        for x in range(4):
            canvas.create_rectangle((3-z)*260 + x*65 + 1,
                                   z*160 + y*40 + 1,
                                   (3-z)*260 + (x+1)*65,
                                   z*160 + (y+1)*40,
                                   outline="#0000ff", width=3)

# SIN línea roja aquí
#canvas.create_rectangle(1, 643, 1040, 680, outline="#ff0000", width=3)

# Texto de turno
texto_turno = Label(tablero, text="Jugador 1", font="arial, 20", fg="green")
texto_turno.place(x=480, y=680)

# Etiquetas de coordenadas SIEMPRE visibles
texto_x = Label(tablero, text="X=0", font="arial, 18", fg="green")
texto_x.place(x=10, y=40)
texto_y = Label(tablero, text="Y=0", font="arial, 18", fg="green")
texto_y.place(x=10, y=70)
texto_z = Label(tablero, text="Z=0", font="arial, 18", fg="green")
texto_z.place(x=10, y=100)
texto_msg = Label(tablero, text="", font="arial, 20")
texto_msg.place(x=320, y=10)

# Botones del cubo 3D (en frame_botones, usando grid)
botones = []
for b in range(64):
    botones.append(crearBoton(' ', b))

contador = 0
for z in range(4):
    for y in range(4):
        for x in range(4):
            botones[contador].grid(row=y + z*4, column=x + (3-z)*4)
            contador += 1

# Botón RESET
btn_reset = Button(tablero, text="Reset", width=7, font=("Helvetica", 13), command=reiniciar)
btn_reset.place(x=800, y=15)

# Botón EXIT
btn_exit = Button(tablero, text="Exit", width=7, font=("Helvetica", 13), command=salir)
btn_exit.place(x=900, y=15)

# Al inicio muestra coordenadas
mostrar_coordenadas(0,0,0)

tablero.mainloop()
