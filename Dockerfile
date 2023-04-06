FROM python:slim-bullseye

WORKDIR /app

COPY . /app

RUN apt-get update


RUN python -m venv /app/env

ENV PATH="/app/env/bin:$PATH"
RUN . env/bin/activate
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/main.py"]


