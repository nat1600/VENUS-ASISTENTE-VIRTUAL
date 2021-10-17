from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser 
import pyautogui
from time import sleep


client_id="69403b8fd7484b41b8d0715615dd9d76"
client_secret="ad47b09605d64a67b3d5ddba1e15fdef"
sin_autor = 0
artista = input('')
cancion = input("")

if len(artista) > 0:
   
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    resultado = sp.search(artista)

    for i in range(0, len(resultado["tracks"]["items"])):

        nombre_cancion = resultado["tracks"]["items"][i]["name"].upper()

        if cancion in nombre_cancion:
            sin_autor = 1
            webbrowser.open(resultado["tracks"]["items"][i]["uri"])
            sleep(5)
            pyautogui.press("enter")
            break

if sin_autor == 0:
    cancion = cancion.replace(" ", "%20")
    webbrowser.open(f'spotify:search:{cancion}')
    sleep(5)
    for i in range(27):
        pyautogui.press("tab")

    for i in range(2):
        pyautogui.press("enter")
        sleep(1)