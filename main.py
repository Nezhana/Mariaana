# main file
import streamlit as st
st.title('Мар\'янка')

volume = st.slider('Для того, щоб змінити швидкість, надайте значення від нуля до ста.', 0, 100, 100)
rate = st.slider('Для того, щоб змінити гучність, надайте значення від нуля до ста.', 0, 100, 100)

# st.write('Змінюю гучність на: ', volume)
# st.write('Змінюю швидкість на: ', rate)

txt = st.text_area(
    "Привiт! Скажiть щось або 'До побачення', щоб завершити.",
    height=300, disabled=False,
    help='Ось перелік основних команд:\n- змінити гучніть\n- змінити швидкість\n- змінити формат письмовий\n- змінити формат усний',)

# if txt:
#     st.write("You entered: ", txt)

messages = st.container()
if txt:
    messages.chat_message("user", avatar='👨‍🎓').write(txt)
    messages.chat_message("assistant", avatar='👩‍🦱').write(f"Echo: {txt}")
