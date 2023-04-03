FROM python:slim-bullseye

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y tzdata
RUN ln -fs /usr/share/zoneinfo/Europe/Kiev /etc/localtime
ENV TZ="Europe/Kiev"

RUN python -m venv /app/env

ENV PATH="/app/env/bin:$PATH"
RUN . env/bin/activate
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/main.py"]
