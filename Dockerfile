ARG PYTHON_VERSION=3.13
ARG APP_NAME=face-recognition-engine

# Build stage
FROM python:${PYTHON_VERSION}-alpine AS build

WORKDIR /app

# Install build dependencies
RUN apk update && \
    apk add --no-cache \
    build-base \
    gfortran \
    && rm -rf /var/cache/apk/*

COPY requirements.txt .

# Install dependencies (but without cache)
RUN pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:${PYTHON_VERSION}-alpine

WORKDIR /app

# Install runtime dependencies (without build dependencies)
RUN apk update && \
    apk add --no-cache \
    rm -rf /var/cache/apk/*

# Copy dependencies from build stage
COPY --from=build /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
# Copy application code
COPY main.py .

# Expose the port
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_ENV=production

# Set entrypoint for Flask app
CMD ["python", "main.py"]
