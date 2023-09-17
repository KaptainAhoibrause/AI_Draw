import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
import speech_recognition as sr
import sounddevice as sd
from pydub import AudioSegment

text = None

def get_text_from_speech():
    speech_engine = sr.Recognizer()

    def from_microphone():
        with sr.Microphone() as micro:
            print('''Recording...''')
            audio = speech_engine.record(micro, duration = 5)
            print(audio)
            print('''Recognition...''')
            text = speech_engine.recognize_google(audio, language = 'en')
        return text

    text = from_microphone()
    return text

def generate_and_save_img():
    url = "http://127.0.0.1:7860"


    payload = {
        'prompt': '{ftext}, svg, line art, white background'.format(ftext = text),
        'steps': 50,
        'batch size': 2
    }
    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

    r = response.json()

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save('draw {ftext}.png'.format(ftext = text), pnginfo=pnginfo)

text = get_text_from_speech()
print(text)
generate_and_save_img()