import time
import requests
from obswebsocket import obsws, requests as obs_requests


host = "localhost"
port = 4444  
password = "" ## CONTRASEÑA DEL WEBSOCKET EN OBS


ws = obsws(host, port, password)
ws.connect()

# Configuración
main_scene = "Escena Principal"
clips_scene = "Escena de Clips"
check_interval = 10  
status_url = "" ## RTMP DE LA TRANSMISION 

def is_streaming():
    try:
        response = requests.get(status_url)
        return response.status_code == 200
    except requests.RequestException:
        return False

def switch_scene(scene_name):
    ws.call(obs_requests.SetCurrentScene(scene_name))

while True:
    if is_streaming():
        switch_scene(main_scene)
    else:
        switch_scene(clips_scene)
    time.sleep(check_interval)
