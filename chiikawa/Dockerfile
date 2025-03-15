FROM python:3.11-slim

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y libopencv-dev ffmpeg sudo \
    build-essential g++ cmake && \
    apt-get clean

WORKDIR /root/workspace

RUN pip install --upgrade pip

RUN pip install poetry
COPY . .
RUN poetry config virtualenvs.create false \
    && poetry install --without ml --no-interaction --no-ansi

RUN rm pyproject.toml poetry.lock
