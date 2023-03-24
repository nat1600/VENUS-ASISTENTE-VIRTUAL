# Importamos las librerías necesarias
import os
import pywhatkit
import time
import playsound
import speech_recognition as sr
import wikipedia
import pyaudio
from gtts import gTTS
import datetime 
import time
import webbrowser
import webview
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser
import pyautogui
from time import sleep

# Credenciales de Spotify
client_id = "69403b8fd7484b41b8d0715615dd9d76"
client_secret = "ad47b09605d64a67b3d5ddba1e15fdef"

nombre = ""  # Variable global que guardará el nombre del usuario


def nombreu():
    global nombre 
    voz("Hola soy Venus . ¿Cómo quieres que te llame?")
    nombre = texto()

def voz(text):
    """
    Convierte texto a voz utilizando la API de Google Text To Speech y la reproduce
    """
    global nombre
    tts = gTTS(text=text, lang='es', slow=False) 
    f= "voice.mp3" 
    tts.save(f)
    playsound.playsound(f)

def saludo():
    """
    Saluda al usuario dependiendo de la hora del día
    """
    global nombre
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        voz("¡Buenos dias " + nombre )
    elif hour >= 12 and hour < 19:
        voz("¡Buenas tardes "+nombre)  
    else:
        voz("¡Buenas noches "+nombre) 

def texto():
    """
    Convierte voz en texto utilizando la API de reconocimiento de voz de Google
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        d = ""
        try:
            d = r.recognize_google(audio)
            print(d)
        except Exception as e:
            voz("No pude entenderte, por favor repite de nuevo. "+ str(e))
    return d 

def abrir_cosas(web):
    """
    Abre aplicaciones o realiza búsquedas en base a la entrada del usuario
    """
    if "youtube" in web:
        voz("¿Qué quieres buscar en youtube?")
        cancion = texto()
        pywhatkit.playonyt(cancion)
        voz("Reproduciendo.. "+cancion)

    elif "google" in web:
        voz("¿Qué quieres buscar?")
        busqueda = texto()
        pywhatkit.search(busqueda)
        voz("Buscando en google "+busqueda)

    elif "que hora es" in web or "que horas son" in web:
        hora = datetime.datetime.now().strftime("%I: %M %p")
        voz("La hora es "+hora)

    elif "wikipedia" in web:
        wikipedia.set_lang("es")
        voz("¿Qué quieres buscar dentro de wikipedia?")
        busqueda_en_wikipedia = texto()
        resultado_busqueda = wikipedia.summary(busqueda_en_wikipedia, sentences=1)
        voz(resultado_busqueda)
        texto()
    
    elif "recordar" in web or "recorder" in web or "breaker" in web or "go to bed" in web or "remember" in web or "calendario" in web:
         # Código para manipular eventos del calendario de
        # Importar librerías necesarias
        from pprint import pprint
        from Google import Create_Service, convert_to_RFC_datetime
        import spotipy
        from spotipy.oauth2 import SpotifyClientCredentials
        import webbrowser
        import pyautogui
        import webview

        # Variables necesarias para acceder a Google Calendar y Spotify
        CLIENT_SECRET_FILE = "/Users/knsmolina.28/Desktop/VENUS/client_secret_710662099665-7njmppifvut78fkhn913frkv3vceicn5.apps.googleusercontent.com.json"
        API_NAME = "calendar"
        API_VERSION = "v3"
        SCOPES = ['https://www.googleapis.com/auth/calendar']
        client_id = "client_id"
        client_secret = "client_secret"

        # Función para crear evento en Google Calendar
        def create_calendar_event():
            # Crear servicio para acceder a Google Calendar
            service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

            # Diccionarios con información para convertir texto a números
            meses = {"enero":1,"febrero":2,"marzo":3,"abril":4,"mayo":5,"junio":6,"julio":7,"agosto":8,"alkosto":8,"august":8,"septiembre":9,"octubre":10,"noviembre":11,"diciembre":12}
            dias = {"uno":1, "1":1 ,"dos":2,"tres":3,"cuatro":4,"cinco":5,"seis":6,"siete":7,"ocho":8,"nueve":9,"diez":10,"ds":10,"once":11,"doce":12,"trece":13,"catorce":14,"quince":15,"dieciséis":16,"diecisiete":17,"dieschiocho":18,"diecinueve":19,"veinte":20,"veintiuno":21,"veintidos":22,"veintitres":23,"veinticuatro":24,"veinticinco":25,"veintiseis":26,"veintisiete":27,"veintisiete":28,"veintiocho":28,"veintinueve":29,"treinta":30}
            horas = {"una":1,"dos":2,"tres":3,"cuatro":4,"cinco":5,"seis":6,"siete":7,"ocho":8,"nueve":9}

            # Obtener mes y día del evento
            voz("¿en qué mes?")
            mes = texto().lower()
            if mes in meses:
                mes_1 = meses[mes]
            else:
                return

            voz("¿en qué día?")
            dia = texto().lower()
            if dia in dias:
                dia_1 = dias[dia]
            else:
                return

            # Obtener título y descripción del evento
            voz("¿Qué quieres recordar?")
            titulo_recordatorio = texto()

            voz("¿Qué descripción quieres usar?")
            descripcion = texto()

            # Crear evento en Google Calendar
            hour_adjusment = +2 # Ajuste horario para Colombia
        horas=12
        minutos=2
        titulo_recordatorio=texto()
        voz("¿Qué descripción quieres usar?")
        descripcion=texto()
        event = {

            'summary': titulo_recordatorio,
            'description': descripcion,
            'start': {
                'dateTime':convert_to_RFC_datetime (int(anio),int(mes_1),int(dia_1),int(horas)+hour_adjusment,int(minutos)),
                "timeZone":"America/Los_Angeles"
                },
                'end': {
                'dateTime':convert_to_RFC_datetime (int(anio),int(mes_1),int(dia_1),int(horas)+hour_adjusment,int(minutos)),
                "timeZone":"America/Los_Angeles"
                    } 
                    }

        event = service.events().insert(calendarId='primary', body=event).execute()
        voz ('Evento creado:'+ titulo_recordatorio) 
        (event.get('htmlLink'))

    elif "reproducir" in web or "spotify" in web:

        voz("¿qué canción deseas oír?")
        cancion=texto()
        voz("¿de qué artista?")
        artista=texto()
        sin_autor = 0
        if len(artista) > 0:
            # Si se proporciona el nombre del artista, se busca la canción en Spotify
            sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
            resultado = sp.search(artista)
            for i in range(0, len(resultado["tracks"]["items"])):
                nombre_cancion = resultado["tracks"]["items"][i]["name"].upper()

            if cancion in nombre_cancion:
                sin_autor = 1
                webbrowser.open(resultado["tracks"]["items"][i]["uri"])
                sleep(5)
                pyautogui.press("enter")
                

    if sin_autor == 0:
         # Si no se proporciona el nombre del artista, se busca la canción por su nombre
        cancion = cancion.replace(" ", " ")
        webbrowser.open(f'spotify:search:{cancion}')
        sleep(5)
        for i in range(26):
            pyautogui.press("tab")

        for i in range(2):
            pyautogui.press("enter")
            voz("reproduciendo" + cancion)
            sleep(1)

"""
Interfaz gráfica y ejecución de comandos de voz
"""
if __name__ == "__main__":
    # Crear ventana de interfaz gráfica
    webview.create_window('', '/Users/knsmolina.28/Desktop/GUI VENUS/y.HTML')
    # Iniciar la interfaz gráfica
    webview.start()
    
    # Obtener nombre del usuario
    nombreu()
    # Dar un saludo inicial
    saludo()
    
    while True:
        # Preguntar al usuario "¿En qué te puedo ayudar"+nombre"
        voz("¿En qué te puedo ayudar" + nombre)
        # Obtener texto del usuario en minúsculas
        texto1 = texto().lower()
        
        # Abrir diferentes cosas dependiendo del texto recibido
        abrir_cosas(texto1)
        
        # Verificar si el texto contiene alguna palabra clave de despedida
        if "adios" in texto1 or "salir" in texto1 or "chao" in texto1 or "hasta la proxima" in texto1 or "uno" in texto1 or "hasta pronto" in texto1:
            # Decir "Hasta la próxima,cuídate "+ nombre
            voz("Hasta la próxima,cuídate " + nombre)
            break
    






