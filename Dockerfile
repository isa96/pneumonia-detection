FROM python:3.8.10

WORKDIR /app

COPY . /app

RUN apt-get update
RUN pip install --upgrade pip setuptools wheel
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

EXPOSE 80

CMD ["/bin/bash"]