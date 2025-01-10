FROM python:3.12

RUN mkdir /notice_bot

WORKDIR /notice_bot

COPY requeriments.txt .

RUN pip install -r requeriments.txt

COPY . .

RUN chmod a+x /notice_bot/*.sh

CMD [ "python", "main.py" ]

