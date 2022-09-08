FROM python:3.6-stretch


WORKDIR /app/

COPY . .

RUN apk update; \
    # pip install Cmake; \
    apk add make; \
    # /usr/local/bin/python -m pip install --upgrade pip; \
    pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD ["app.py" ]

