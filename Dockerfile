FROM python:slim-bullseye

WORKDIR /app

COPY . /app

RUN python -m venv /app/env

ENV PATH="/app/env/bin:$PATH"
RUN . env/bin/activate
RUN python -m pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt 

ENV TZ="Europe/Kiev"
RUN ln -sf /usr/share/zoneinfo/Europe/Kiev /etc/localtime


CMD ["python", "src/main.py"]
