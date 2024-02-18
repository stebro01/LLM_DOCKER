# Use python as base image
FROM python

# Set the working directory in the container
WORKDIR /app

# Install the needed packages
RUN pip install llama-cpp-python
RUN pip install Flask
RUN pip install -U flask-cors

# Expose port 5000 outside of the container
EXPOSE 5000

