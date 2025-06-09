FROM python:3.10-slim AS builder

WORKDIR /app
COPY requirements.txt requirements-dev.txt ./
RUN pip install -r requirements.txt && \
    pip install -r requirements-dev.txt

FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .

ENV PATH=/root/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    FLASK_DEBUG=0

CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:5000", "wsgi:app"]