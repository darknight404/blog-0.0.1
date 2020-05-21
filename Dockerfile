FROM python:3.6-alpine

RUN adduser -D blog

WORKDIR /home/blog

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY blog blog
COPY migrations migrations
COPY wsgi.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP wsgi.py

RUN chown -R blog:blog ./
USER blog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
