FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Europe/Kiev /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

WORKDIR /app

COPY . /app

RUN python -m venv /app/env && \
    . /app/env/bin/activate && \
    python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/main.py"]
