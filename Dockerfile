FROM python:3.11-slim

# make Python behave
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set working dir to the folder that contains manage.py
WORKDIR /app/thepoll

# system deps needed by Pillow / psycopg2 etc.
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# install Python deps first (speedy rebuilds)
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# now copy project files
COPY . .

# ensure start script is executable
RUN chmod +x start.sh

# set Django settings module (this is the correct one for your layout)
ENV DJANGO_SETTINGS_MODULE=thepoll.settings

# expose the port your host will map (platform may override $PORT)
EXPOSE 8080

# run the start script
CMD ["./start.sh"]
