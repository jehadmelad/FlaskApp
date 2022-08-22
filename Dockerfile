FROM python:3-alpine


WORKDIR /app/

COPY . .

RUN pip3 install -r requirements.txt 

ENTRYPOINT [ "python3" ]

CMD ["app.py" ]

