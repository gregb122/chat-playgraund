FROM bmltenabled/uvicorn-gunicorn-fastapi:python3.10-slim

RUN pip3 install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt

RUN mkdir -p /src
COPY ./src/ /src

WORKDIR /src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--ws", "'auto'", "--loop", "'auto'", "--workers 4"]