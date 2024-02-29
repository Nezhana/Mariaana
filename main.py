
# main file


def input_recognize(user_input):
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
            message = 'Гучність змінена. Що я можу зробити для вас ще?'
            status = 'answer'
            return message, status
        case 'змінити швидкість':
            message = 'Швідкість змінена. Що я можу зробити для вас ще?'
            status = 'answer'
            return message, status
        case _:
            message = user_input
            status = 'answer'
            return message, status


import streamlit as st
st.title('Мар\'янка')

volume = st.slider('Для того, щоб змінити швидкість, надайте значення від нуля до ста.', 0, 100, 100)
rate = st.slider('Для того, щоб змінити гучність, надайте значення від нуля до ста.', 0, 100, 100)

# st.write('Змінюю гучність на: ', volume)
# st.write('Змінюю швидкість на: ', rate)


user_input = st.text_area(
    "Привiт! Скажiть щось або 'До побачення', щоб завершити.",
    height=140, disabled=False,
    help='Ось перелік основних команд:\n- змінити гучніть\n- змінити швидкість\n- змінити формат письмовий\n- змінити формат усний',)

# if txt:
#     st.write("You entered: ", txt)

messages = st.container()
if user_input:
    message = input_recognize(user_input)
    messages.chat_message("user", avatar='👨‍🎓').write(user_input)
    messages.chat_message("assistant", avatar='👩‍🦰').write(f"Echo: {message}")
