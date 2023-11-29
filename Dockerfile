# Use the official Ubuntu base image
FROM ubuntu

# Install Python and Flask
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install flask

# Copy the app code into the container
COPY app.py /app.py

# Expose the necessary port
EXPOSE 8080

# Command to run the Flask app
CMD ["python3", "/app.py"]