FROM bmltenabled/uvicorn-gunicorn-fastapi:python3.10-slim

RUN pip3 install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt

RUN mkdir -p /src
COPY ./src/ /src

COPY ./src/run.sh /run.sh
RUN chmod a+rwx /run.sh
RUN chmod -R a+rwx /src

ENV PORT=80
EXPOSE $PORT
WORKDIR /src
ENTRYPOINT ["/run.sh"]