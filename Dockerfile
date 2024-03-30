FROM python:3.12
LABEL maintainer = 'hyeongbin0516'

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

ARG DEV=false
# 빌드 명령어
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [$DEV = "true"] ; \
        then echo "===THIS IS DEVELOPMENT BUILD===" &&\
        /py/bin/pip3 install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        dajango-user

ENV PATH="/py/bin/:$PATH"

USER dajango-user