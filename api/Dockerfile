# Use slim Python image
FROM python:3.11-slim

WORKDIR /app

# Install system deps required for psycopg2 and other libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

# Copy application code
COPY . /app

# Install Python deps commonly used by the project.
# Adjust if you maintain a requirements.txt in api/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir \
        gunicorn \
        flask \
        flask-cors \
        python-dotenv \
        psycopg2-binary \
        google-genai \
        PyPDF2

# Ensure uploads/kb_info folders exist
RUN mkdir -p /app/uploads /app/kb_info

ENV FLASK_APP=main.py
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin@123
ENV POSTGRES_DB=my_db
ENV POSTGRES_HOST=pgvector
ENV POSTGRES_PORT=5432
ENV EMBEDDING_MODEL=gemini-embedding-001
EXPOSE 5000

# Use gunicorn to serve the Flask app (api/main.py defines app)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app", "--workers", "4", "--threads", "2"]