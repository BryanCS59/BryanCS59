# importamos la libreria para el reconocimiento de voz
import speech_recognition as sr
import pyttsx3  # importamos la libreria para la voz del sistema
import pywhatkit  # importamos la libreria para buscar musica
import datetime  # importamos la libreria para sacar la fecha y hora del sistema
import sys
import requests
from lxml import html

name = 'chicobestia'
listener = sr.Recognizer()  # definimos variable para el reconocimeinto de voz
engine = pyttsx3.init()  # definimos e inicializamos variables para la voz del sistema

voices = engine.getProperty('voices')  # variable para modificar la voz
# asignamos prpiedades a la voz de acuerdo al id de la libreria
engine.setProperty('voices', voices[1].id)


def talk(text):  # metodo para devolver lo que el usuario diga
    engine.say(text)  # El sistema guardara en memoria lo que el usuario diga.
    engine.runAndWait()


# desde aqui se empieza a programar el asistente de voz
def listen():  # Definimos el método para el reconocimiento de voz
    try:  # Haremos que escuche lo que estamos diciendo
        with sr.Microphone() as source:  # desde la libreria, usaremos el metodo 'Microphone' para que haga uso del microfono del equipo
            print("Escuchando...")
            # creamos una variable voice y llamamos al reconocimiento de voz y con el método 'listen'
            voice = listener.listen(source)
            # hara que escuche lo que estamos diciendo
            # Creamos la variable rec para que guarde lo que acabamos de decir, mandamos a llamar el reconocimiento de voz y con el método de
            # 'recognize_google' haremos que busque las palabras desde un repositorio de google
            # con el parametro de 'language'
            rec = listener.recognize_google(voice, language='es-ES')
            # asignamos el idioma que deberá trabajar el asistente de voz
            rec = rec.lower()
            if name in rec:  # haremos que el sistema nos responda siempre y cuando se diga el nombre del sistema
                rec = rec.replace(name, '')
                print(rec)  # Haremos que nos regrese lo que acabamos de decir.
    except:
        pass
    return rec


def run():  # definimos un método para las instrucciones 
    rec = listen()  # mandamos a llamar el métod listen que creamos
    if 'reproduce' in rec:  # haremos que el sistema reproduzca la canción siempre y cuando la instrucción sea 'reproduce'
        music = rec.replace('reproduce', '')
        talk('Reproduciendo...' + music)  # el sistema nos contestará
        # utilizamos la libreria y con el método 'playonty' buscará la cancion desde YouTube y la reproducirá
        pywhatkit.playonyt(music)

    elif 'hora' in rec:  # Haremos que el sistema funciones siempre y cuando la instrucción tenga la palabra 'hora'
        # declaramos la variable hora y le asignamos los valores de 'datetime' que se
        hora = datetime.datetime.now().strftime('%I:%M %p')
        # importaran de la librea 'datetime'
        talk("Son las " + hora)  # nos contestará con la hora del SO.
        
    #elif 'clima' in rec:
    #    tiempo = 


run()
