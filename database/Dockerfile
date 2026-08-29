FROM python:3.11

WORKDIR /app

# Install build dependencies for compiling psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY database/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY database/app ./app
COPY database/alembic/ ./alembic
COPY database/alembic.ini .
COPY database/entrypoint.sh .
RUN chmod +x entrypoint.sh
COPY common ./common

EXPOSE 8080

CMD ["./entrypoint.sh"]