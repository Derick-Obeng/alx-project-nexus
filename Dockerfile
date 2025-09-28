FROM python:3.11-slim

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy everything at once
COPY . .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=thepoll.settings


EXPOSE 8000

RUN chmod +x start.sh

CMD ["./start.sh"]
