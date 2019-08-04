FROM python:3.7.4-slim-stretch

COPY ./src/backend/requirements.txt /deploy/app/requirements.txt
RUN pip install -r /deploy/app/requirements.txt
COPY ./src/backend/ /deploy/app/
RUN pip install gunicorn

WORKDIR /deploy/app/server

CMD ["/bin/bash", "/deploy/app/server/entrypoint.sh"]
