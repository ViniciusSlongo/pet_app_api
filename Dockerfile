FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt / 

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app 

# Make serve.sh executable
RUN chmod +x serve.sh

ENTRYPOINT ["./serve.sh"]