# Stage 1: Build dependencies
FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade system packages to reduce vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only requirements.txt from FinalProject
COPY FinalProject/requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels


# Stage 2: Runtime
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade system to reduce vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=builder /wheels /wheels
COPY FinalProject /app

RUN pip install --no-cache /wheels/*

# Create unprivileged user
RUN useradd -m appuser
USER appuser

EXPOSE 5000
CMD ["python", "app.py"]

