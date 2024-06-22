# Makefile for Docker build and run

# Define variables
IMAGE_NAME=web-reflex
TAG=latest
CONTAINER_NAME=app
DOCKERFILE_PATH=.
DOCKER_USERNAME=vfedotovsdocker


# Function to detect architecture
ARCH := $(shell uname -m | sed 's/x86_64/x86/;s/aarch64/arm/')

# Default target
all: build run

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME):$(TAG)-$(ARCH) $(DOCKERFILE_PATH)

# Run the Docker container
run:
	docker run -it --rm -p 80:3000 -p 8000:8000 --name $(CONTAINER_NAME) $(IMAGE_NAME):$(TAG)-$(ARCH)


# Push the Docker image to Docker Hub
push: build
	@echo "Pushing $(DOCKER_USERNAME)/$(IMAGE_NAME):$(TAG)-$(ARCH) to Docker Hub"
	docker login -u $(DOCKER_USERNAME)
	docker push $(DOCKER_USERNAME)/$(IMAGE_NAME):$(TAG)-$(ARCH)

# Phony targets
.PHONY: all build run push


