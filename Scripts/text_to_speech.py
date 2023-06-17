import json
import time
import requests
import playsound
from config import Key_EdenAI

def TextToSpeech(text='Бәріне салем!'):
    headers = {"Authorization": f"Bearer {Key_EdenAI}"}
    url = 'https://api.edenai.run/v2/audio/text_to_speech'

    payload = {
        'providers': 'microsoft',
        'language': 'kk-KZ',
        # 'option': 'MALE',
        # 'microsoft': 'kk-KZ-DauletNeural',
        'option': 'FEMALE',
        'lovoai': 'kk-KZ-AigulNeural',
        'text': f'{text}'
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    unx_time = int(time.time())

    # with open(f'{unx_time}.json', 'w') as file:
    #     json.dump(result, file, indent=4, ensure_ascii=False)

    audio_url = result.get('microsoft').get('audio_resource_url')
    r = requests.get(audio_url)

    with open('speech.mp3', 'wb') as file:
        file.write(r.content)
    playsound.playsound("speech.mp3")
    