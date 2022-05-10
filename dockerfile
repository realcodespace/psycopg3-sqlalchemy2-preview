FROM python:3.10

ENV PYTHONPATH "${PYTHONPATH}:/server"
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR '/server'

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./ ./