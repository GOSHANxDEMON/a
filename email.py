from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
from dotenv import load_dotenv


def main():
    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    load_dotenv()
    password = os.getenv("PASSWORD")
    completed_modules = ["Введение в JS"]
    unfinished_modules = ["Основы Python"]
    time = "6 месяцев"
    email = "doscachgosha@ya.ru"
    to_email = "doscachgosha@ya.ru"
    msg = MIMEMultipart()
    msg["From"] = "doscachgosha@ya.ru"
    msg["To"] = "emaykrutoy537@gmail.com"
    msg["Subject"] = "nothing"
    if completed_modules:
        text = f"Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. Сейчас я работаю над модулями {unfinished_modules}. Пока что я улучшаю свои навыки и узнаю много нового!"
    else:
        text = f"Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. В процессе я выполнил модули: {completed_modules}! Сейчас я работаю над модулями {unfinished_modules}. Обучение мне нравится, я получил море знаний!"
    msg.attach(MIMEText(text,"plain"))
    server.login(email,password)
    server.sendmail(email,to_email,msg.as_string())
    server.quit()


if __name__=="__main__":
    main()

