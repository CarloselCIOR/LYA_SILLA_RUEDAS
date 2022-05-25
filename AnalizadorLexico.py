#Importaciones
from tkinter.scrolledtext import ScrolledText
import lex
import re
import codecs
import os
import sys
from tkinter import *

#Diccionario de palabras reservadas
reservadas =  [
    'IMPORT',
    'DEF',
    'CLASS',
    'IF',
    'ELSE',
    'FOR',
    'IN',
    'RANGE',
    'SELF',
    'WHILE',
    'TRY',
    'EXCEPT',
    'RETURN',
    'BREAK',
    'NEXT',

    'INPUT',
    'PRINT',
    'INT',
    'FLOAT',
    'BOOLEAN',
    'STRING',

    'POWER',
    'SQRT',
    'AND',
    'OR',
    'NOT',
    'BEGIN',
    'END'
]


#Lista de Tokens que usaran los metodos
        #Basicas
tokens = reservadas + ['ID', 'NUMERO','SUMA','ASIGNACION','RESTA','DIVISION','MULTIPLICACION',
         #Operadores 
          'IGUAL','DIFERENTE','MAYORQUE','MENORQUE','MAYORIGUALQUE','MENORIGUALQUE',
         #Separadores 
          'PUNTO','COMA','DOSPUNTOS','PUNTOCOMA','COMILLASIMPLE','COMILLADOBLE','PARENTESISABIERTO',
          'PARENTESISCERRADO','LLAVEABIERTO','LLAVECERRADO','CORCHETEABIERTO','CORCHETECERRADO','ESPACIO',
         #Pasos
          'INCREMENTO','DECREMENTO']
          

t_ignore = '\t'

#Operadores matematicos
t_SUMA = r'\+'
t_ASIGNACION = r'='
t_RESTA = r'\-'
t_DIVISION = r'/'
t_MULTIPLICACION = r'\*'

#Operadores
t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MAYORIGUALQUE = r'>='
t_MENORIGUALQUE = r'<='

t_PUNTO = r'\.'
t_COMA = r'\,'
t_DOSPUNTOS = r'\:'
t_PUNTOCOMA = r'\;'
t_COMILLASIMPLE = r'\''
t_COMILLADOBLE = r'\"'
t_PARENTESISABIERTO = r'\('
t_PARENTESISCERRADO = r'\)'
t_LLAVEABIERTO = r'\{'
t_LLAVECERRADO = r'\}'
t_CORCHETEABIERTO = r'\['
t_CORCHETECERRADO = r'\]'
t_ESPACIO = r'\s'

t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'\-\-'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SALTOLINEA(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_COMENTARIO(t):
    r'\#.*'
    pass

def t_error(t):
    t.lexer.skip(1)
    return "Caracter ilegal"

a = []

def analiza(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    a.clear
    while True:
        tok = analizador.token()
        if not tok : break
        a.append(str(tok))
    return a


def analizaar():
    concatena = ""
    cadena = ''
    cadena = txtBox1.get(1.0, "end-1c")
    analiza(cadena)
    for i in a:
        concatena += i + '\n'
    txtBox2.delete('1.0', END)
    txtBox2.insert(END, concatena)

def limpiar1 ():
    txtBox1.delete('1.0', END)
    txtBox1.insert(END, '')
    limpiar2

def limpiar2 ():
    txtBox2.delete('1.0', END)
    txtBox2.insert(END, '')

ventana = Tk()
ventana.geometry("1920x1080")
ventana.title("Analizador Lexico - Python")
ventana.state('zoomed')

menubar = Menu(ventana)
ventana.config(menu = menubar)

lbl1 = Label(ventana, text = "Cadena a Analizar: ")
lbl1.grid(row = 0, column = 0)
txtBox1 = ScrolledText()
txtBox1.grid(row = 2, column = 0)

lbl2 = Label(ventana, text = "Tokens: ")
lbl2.grid(row = 3, column = 0)
txtBox2 = ScrolledText()
txtBox2.grid(row = 4, column = 0)

btn = Button(ventana, text = "Analizar", command = analizaar)
btn.grid(column=1,row=2)


filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command = limpiar1)
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command = ventana.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

voicemenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Archivo .WAV")
editmenu.add_command(label="Grabacion")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu = filemenu)
menubar.add_cascade(label="Editar", menu = editmenu)
menubar.add_cascade(label="Voz", menu = voicemenu)
menubar.add_cascade(label="Ayuda", menu = helpmenu)

ventana.mainloop()
