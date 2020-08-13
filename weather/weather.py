import requests
import json
import subprocess
import os

location = "139.728605,35.704896"
app_id = "dj00aiZpPW96NExRczNOcU1VQiZzPWNvbnN1bWVyc2VjcmV0Jng9NDY-"
url = "https://map.yahooapis.jp/weather/V1/place"

state_file = os.path.join(os.getcwd(), "rain_state.conf")

payload = {'coordinates': location, 'appid': app_id, 'output': 'json', 'interval': '5'}
r = requests.get(url, params=payload)
data = json.loads(r.text)
data = data['Feature'][0]['Property']['WeatherList']['Weather']

print(data)
rain = False
for x in data:
    if x['Rainfall'] > 0:
        rain = True
pastRainState = False
try:
    fin = open(state_file, 'rt')
    line = fin.read()
    print(line)
    fin.close()
    if line == 'True':
        pastRainState = True
except FileNotFoundError:
    print('File not found.')
    fin = open(state_file, 'wt')
    fin.write('False')
    fin.close()
print(str(rain) + ' ' + str(pastRainState))
if rain and (not pastRainState):
    fout = open(state_file, 'wt')
    fout.write('True')
    fout.close()
    speak_command = 'node /home/pi/homeautomation/notifier/speak.js 新宿区えのきちょうのお天気を、お知らせします。まもなく雨が降り出します。'
    subprocess.call(speak_command, shell=True)

if (not rain) and pastRainState:
    fout = open(state_file, 'wt')
    fout.write('False')
    fout.close()
