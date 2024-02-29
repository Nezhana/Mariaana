
# main file


import pyttsx3
import speech_recognition as s

from openai import OpenAI
from config import activation_key
import streamlit as st
import time



class Mariaana():

    def __init__(self):
        self.engine = pyttsx3.init() #initiate engine for speaker
        self.voices = self.engine.getProperty('voices') #get all voices
        self.engine.setProperty('voice', self.voices[2].id) #set Mariannas voice
        self.client = OpenAI(api_key=activation_key)

    def say(self, text):
        time.sleep(7)
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine = 0
        # if self.engine._inLoop:
        #     self.engine.endLoop()
    
    def change_rate(self, rate):
        # corelate rate value:
        if rate >= 100:
            rate = 100
        elif rate <= 0:
            rate = 1
        rate += 100

        old_rate = self.engine.getProperty('rate')
        print('log: old rate value: ' + str(old_rate) +', new rate value: ' + str(rate))
        self.engine.setProperty('rate', rate)

    def change_volume(self, volume):
        # corelate volume value:
        if volume >= 100:
            volume = 100
        elif volume <= 0:
            volume = 1
        volume /= 100
        
        old_volume = self.engine.getProperty('volume')
        print('log: old volume value: ' + str(old_volume) +', new volume value: ' + str(volume))
        self.engine.setProperty('volume', volume)

    def input_recognize(self, user_input):
        match user_input.lower():
            case 'привіт':
                message = 'І тобі привіт! Чим можу допомогти?'
                status = 'answer'
                return message, status
            case 'вітаю':
                message = 'Вітаю вас! Чим можу допомогти?'
                status = 'answer'
                return message, status
            case 'добрий день':
                message = 'Доброго дня. Чим можу допомогти?'
                status = 'answer'
                return message, status
            case 'змінити формат усний':
                message = 'Змінюю формат на: усний.'
                status = 'voice'
                return message, status
            case 'змінити формат письмовий':
                message = 'Змінюю формат на: письмовий.'
                status = 'text'
                return message, status
            case 'змінити гучність':
                volume.disabled = False
                message = 'Для того, щоб змінити гучність, надайте значення від нуля до ста.\n'
                message += 'Наприклад: сорок.'
                # self.say(message)
                # print('Мар\'яна: ' + message)

                # user_input = speech_to_text()
                if volume:
                    volume_val = float(volume)
                    message = f'Змінюю гучність на: {volume_val}%.'
                    self.change_volume(volume_val)
                    messages.chat_message("assistant", avatar='👩‍🦰').write(f"Мар\'янка: {message}")

                # try:
                #     volume_val = float(user_input)
                #     message = f'Змінюю гучність на: {user_input}%.'
                #     # self.say(message)
                #     # print('Мар\'яна: ' + message)
                #     self.change_volume(volume_val)
                #     break
                # except ValueError:
                #     continue
                message = 'Гучність змінена. Що я можу зробити для вас ще?'
                status = 'answer'
                volume.disabled = True
                return message, status
            case 'змінити швидкість':
                rate.disabled = True
                message = 'Для того, щоб змінити швидкість, надайте значення від нуля до ста.\n'
                message += 'Наприклад: шістдесят п\'ять.'
                # self.say(message)
                # print('Мар\'яна: ' + message)

                if rate:
                    rate_val = float(rate)
                    message = f'Змінюю гучність на: {rate_val}%.'
                    self.change_rate(rate_val)
                    messages.chat_message("assistant", avatar='👩‍🦰').write(f"Мар\'янка: {message}")

                # user_input = speech_to_text()
                # try:
                #     rate_val = int(user_input)
                #     message = f'Змінюю швидкість на: {rate_val}%.'
                #     self.say(message)
                #     print('Мар\'яна: ' + message)
                #     self.change_rate(rate_val)
                #     break
                # except ValueError:
                #     continue
                message = 'Швідкість змінена. Що я можу зробити для вас ще?'
                status = 'answer'
                rate.disabled = True
                return message, status
            case _:
                # message = user_input.lower().split()
                # if message[0] in ('як', 'який', 'яке', 'яка', 'які', 'чому', 'що',\
                #                   'де', 'кого', 'хто', 'чи', 'коли', 'якщо'):
                #     message = ' '.join(message) + '?'
                
                # response = self.client.chat.completions.create(
                #     model="gpt-3.5-turbo",
                #     messages=[
                #         {"role": "system", "content": "You are a helpful assistant."},
                #         {"role": "user", "content": message}
                #     ]
                # )
                # answer = response.choices[0].message.content
                answer = user_input
                status = 'answer'
                return answer, status

def speech_to_text():
    sr = s.Recognizer()
    with s.Microphone() as source:
        audio = sr.listen(source)
        source_text = sr.recognize_google(audio, language='uk-UA', show_all=True)
        print('you said: ' + source_text['alternative'][0]['transcript'])
    return source_text['alternative'][0]['transcript']

def main():
    
    mariaana = Mariaana()
    chat_form = 'text'

    # print("Привiт! Скажiть щось або 'До побачення', щоб завершити.")
    # print("Ось перелік основних команд:")
    # print("- змінити гучніть")
    # print("- змінити швидкість")
    # print("- змінити формат письмовий")
    # print("- змінити формат усний")

    if chat_form == 'voice':
        user_input = speech_to_text()
    elif chat_form == 'text':
        # user_input = input('Введіть репліку: ')
        pass
    else:
        raise ValueError(f'chat_form = {chat_form}')
    if user_input:
        if user_input.lower() == "до побачення" or user_input.lower() == "бувай" :
            message = 'До зустрiчi!'
            messages.chat_message("user", avatar='👨‍🎓').write(user_input)
            messages.chat_message("assistant", avatar='👩‍🦰').write(f"Мар\'янка: {message}")

        message, status = mariaana.input_recognize(user_input)
        match status:
            case 'answer':
                messages.chat_message("user", avatar='👨‍🎓').write(user_input)
                messages.chat_message("assistant", avatar='👩‍🦰').write(f"Мар\'янка: {message}")
                # mariaana.say(message)
                # print('Мар\'яна: ' + message)
            case 'voice':
                messages.chat_message("user", avatar='👨‍🎓').write(user_input)
                messages.chat_message("assistant", avatar='👩‍🦰').write(f"Мар\'янка: {message}")
                # mariaana.say(message)
                # print('Мар\'яна: ' + message)
                chat_form = status
            case 'text':
                messages.chat_message("user", avatar='👨‍🎓').write(user_input)
                messages.chat_message("assistant", avatar='👩‍🦰').write(f"Мар\'янка: {message}")
                # mariaana.say(message)
                # print('Мар\'яна: ' + message)
                chat_form = status

if __name__ == '__main__' :

    st.set_page_config(page_title='Mariaana', page_icon='👩‍🦰', layout="centered", initial_sidebar_state="auto", menu_items=None)
    st.title('Мар\'янка')

    volume = st.slider('Для того, щоб змінити швидкість, надайте значення від нуля до ста.', 0, 100, 100, disabled=True)
    rate = st.slider('Для того, щоб змінити гучність, надайте значення від нуля до ста.', 0, 100, 100, disabled=True)

    messages = st.container(border=True)

    user_input = st.text_area(
                        "Привiт! Скажiть щось або 'До побачення', щоб завершити.",
                        height=140, disabled=False,
                        help='Ось перелік основних команд:\n- змінити гучніть\n- змінити швидкість\n- змінити формат письмовий\n- змінити формат усний',)

    main()


# st.write('Змінюю гучність на: ', volume)
# st.write('Змінюю швидкість на: ', rate)


# if txt:
#     st.write("You entered: ", txt)


#if volume:
#    message = f'Змінюю гучність на: {volume}%.'
#    messages.chat_message("assistant", avatar='👩‍🦰').write(f"Мар\'янка: {message}")

#if rate:
#    message = f'Змінюю швидкість на: {rate}%.'
#    messages.chat_message("assistant", avatar='👩‍🦰').write(f"Мар\'янка: {message}")
