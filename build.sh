#!/bin/bash

# Build script for Project Manager Docker image

echo "Building Project Manager Docker image..."
echo "Performing a clean build (no cache)..."
docker build --no-cache -t project-manager:latest .

# Tag with date for versioning
DATE_TAG=$(date +"%Y%m%d")
echo "Tagging image with date: $DATE_TAG"
docker tag project-manager:latest project-manager:$DATE_TAG

echo "Build complete!"
echo "You can now deploy the application using: docker compose up -d" 