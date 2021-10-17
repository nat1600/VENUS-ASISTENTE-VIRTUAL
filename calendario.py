
from datetime import datetime
from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE="/Users/knsmolina.28/Desktop/A/client_secret_710662099665-7njmppifvut78fkhn913frkv3vceicn5.apps.googleusercontent.com.json"
API_NAME="calendar"
API_VERSION="v3"
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service (CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

numeros=["1","2","3","4","5","6","7","8","9"]
num=""
meses={"enero":1,"febrero":2,"marzo":3,"abril":4,"mayo":5,"junio":6,"julio":7,"agosto":8,"septiembre":9,"octubre":10,"noviembre":11,"diciembre":12}
dias={"uno":1,"dos":2,"tres":3,"cuatro":4,"cinco":5,"seis":6,"siete":7,"ocho":8,"nueve":9,"diez":10,"once":11,"doce":12,"trece":13,"catorce":15}
horas={"una":1,"dos":2,"tres":3,"cuatro":4,"cinco":5,"seis":6,"siete":7,"ocho":8,"nueve":9}

def recordar():
    global datetime
    TITULO=input("titulo")
    descripcion=input("descripcion")
    anio=2021
    mes=int(input())
    dia1=int(input())
    horas1=int(input())
    minutos=int(input())
    


    event = {
    'summary': TITULO,
    'description': descripcion,
    'start': {
    'dateTime':convert_to_RFC_datetime (int(anio),int(mes),int(dia1),int(horas1),int(minutos)).isoformat() 

    }
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print ('Event created: %s') % (event.get('htmlLink'))

recordar()
