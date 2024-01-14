FROM python:3.8

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python3 bot.py

RUN pip install python-telegram-bot requests

COPY . .

EXPOSE 1337

USER 1000

CMD [ "python", "./server.py" ]
