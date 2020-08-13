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

# 取得情報から降雨を判定
is_forecast_rain = False
rain_start_date = ''
for x in data:
    if x['Rainfall'] > 0:
        is_forecast_rain = True
        rain_start_date = x['Date'][8:12]
        break

# ファイルから直近に記録した状態を読み込み
is_past_rain = False
try:
    fin = open(state_file, 'rt')
    line = fin.read()
    fin.close()
    if line == 'True':
        is_past_rain = True
except FileNotFoundError:
    print('File not found.')
    fin = open(state_file, 'wt')
    fin.write('False')
    fin.close()

print(str(is_forecast_rain) + ' ' + str(is_past_rain))

# 書き込み・発話
if is_forecast_rain and (not is_past_rain):
    fout = open(state_file, 'wt')
    fout.write('True')
    fout.close()

    # 発話
    rain_start_hour = rain_start_date[0:2] if rain_start_date[0:1] == 0 else rain_start_date[1:2]
    rain_start_minutes = rain_start_date[2:4] if rain_start_date[2:3] == 0 else rain_start_date[3:4]

    speak_sentence = 'お天気を、お知らせします。' + \
                     rain_start_hour +\
                     '時' + \
                     rain_start_minutes +\
                     '分' + \
                     '頃より雨が降り出します。'
    speak_command = 'node /home/pi/homeautomation/notifier/speak.js ' + speak_sentence
    subprocess.call(speak_command, shell=True)

if (not is_forecast_rain) and is_past_rain:
    fout = open(state_file, 'wt')
    fout.write('False')
    fout.close()
