# Multi-stage build with security - keeping original simplicity
FROM python:3.12-slim as builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install dependencies in builder stage for optimization
COPY requirements.txt /app/
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Production stage - your original structure enhanced
FROM python:3.12-slim

# Install runtime dependencies (curl for health checks)
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set work directory (keeping your original)
WORKDIR /app

# Install dependencies from wheels (faster and smaller)
COPY --from=builder /app/wheels /wheels
COPY requirements.txt /app/
RUN pip install --no-cache /wheels/*

# Copy project files (keeping your original)
COPY . /app

# Add security without breaking your workflow
RUN groupadd -r appuser && useradd -r -g appuser appuser
RUN chown -R appuser:appuser /app
USER appuser

# Add health check using your new endpoint
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1

# Environment variables for production
ENV PYTHONUNBUFFERED=1
ENV DJANGO_ENV=production

# Expose port (keeping your original)
EXPOSE 8000

# Keep your original Django runserver for development, but make it production-ready
# You can switch this to gunicorn later if needed
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]