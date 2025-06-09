FROM python:3.10-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt
RUN pip install --user flake8

FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    FLASK_DEBUG=0

CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:5000", "wsgi:app"]