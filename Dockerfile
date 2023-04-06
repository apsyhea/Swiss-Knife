FROM python:slim-bullseye

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y tzdata

RUN python -m venv /app/env

ENV PATH="/app/env/bin:$PATH"
RUN . env/bin/activate
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN echo "Europe/Kiev" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

RUN ln -sf /usr/share/zoneinfo/Europe/Kiev /etc/localtime


CMD ["python", "src/main.py"]
