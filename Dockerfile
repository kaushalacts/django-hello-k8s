FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install system dependencies for security and monitoring
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# Create non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser
RUN chown -R appuser:appuser /app
USER appuser

# Add health check for container monitoring
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1

# Expose port
EXPOSE 8000

# Run Django app with security considerations
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]