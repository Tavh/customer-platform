FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the app code
COPY . .

# Copy the requirements file and install dependencies
RUN python3 -m venv venv && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt


ENV BOOTSTRAP_SERVERS ${BOOTSTRAP_SERVERS}
ENV TOPIC ${TOPIC}
ENV CUSTOMER_MANAGEMENT_URL ${CUSTOMER_MANAGEMENT_URL}


# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the application using flask run
CMD python3 main.py
