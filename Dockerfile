FROM python:3.11-slim

# Update package lists and install netcat
RUN apt-get update && apt-get install -y netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy folder app
COPY ./app /app

COPY ./env.sample /.env

COPY ./start-dev.sh /start.sh
RUN chmod +x /start.sh

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

EXPOSE 8080

CMD ["/start.sh"]
