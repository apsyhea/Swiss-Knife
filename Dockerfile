FROM ubuntu:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y python3-pip python3-venv iputils-ping  

# Create a virtual environment
RUN python3 -m venv /app/myenv

# Set the default virtual environment to be used in the image
ENV VIRTUAL_ENV=/app/myenv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the command to start the bot
CMD ["python", "main.py"]
