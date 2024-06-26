FROM --platform=linux/amd64 python:3-alpine as build

ENV DATABASE_URL=original_base

COPY src/ /app

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "python3", "app.py" ]