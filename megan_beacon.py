import dweepy
import json
import time
import os

from gtts import gTTS
tts = gTTS('pay attention to me')
tts.save('sound.mp3')

while True:
    try:
        with open('need_token.txt', 'r') as myfile:
            file_data = myfile.read()
        dweet = dweepy.get_latest_dweet_for('The_megan_beacon')
        value = str(dweet[0]["content"]["value"])
        if file_data == value:
            print("yep")
            time.sleep(10)
        else:
            print("nope")
            # play audio file
            # write new number to token file
            print(value)
            os.system("afplay sound.mp3")
            with open('need_token.txt', 'w') as myfile:
                myfile.write(str(value))
            print("updated old value " + file_data + " file with " + value)
            time.sleep(10)
    except:
        print("there was nothing there")
        time.sleep(10)



