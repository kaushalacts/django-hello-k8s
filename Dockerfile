# Multi-stage build for optimization
FROM python:3.12-slim as builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies in builder stage
COPY requirements.txt /app/
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Production stage
FROM python:3.12-slim

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    curl \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy wheels from builder stage and install
COPY --from=builder /app/wheels /wheels
COPY requirements.txt /app/
RUN pip install --no-cache /wheels/*

# Copy project files
COPY . /app

# Set environment variables for production
ENV DJANGO_ENV=production
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8000

# Use gunicorn for production with multiple workers
CMD ["python", "-m", "gunicorn", "--workers", "2", "--bind", "0.0.0.0:8000", "hello_world.wsgi:application"]