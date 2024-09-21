# FastAPI Kafka Mini-Project

## Overview

This project is a simple FastAPI application that consumes messages from a Kafka topic using the `aiokafka` library. It demonstrates how to set up a Kafka consumer, handle messages asynchronously, and manage configuration using environment variables.


## Features

- Asynchronous message consumption from a Kafka topic.
- Easy configuration management using an `.env` file.
- Structured code with separate files for configuration, Kafka handling, and the FastAPI application.

## Technologies Used

- FastAPI
- aiokafka
- python-dotenv

## Prerequisites

- Python 3.7 or higher
- Kafka server running locally (or the specified bootstrap server)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-kafka-mini-project.git
   cd fastapi-kafka-mini-project
    ```

2. Create a virtual environment:
   
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install required packages:

    ```bash
    pip install fastapi aiokafka python-dotenv uvicorn
    ```

4. Create a `.env` file in the root directory and add the following configuration:

    ```env
    KAFKA_BOOTSTRAP_SERVERS=localhost:9092
    KAFKA_TOPIC=sensorData
    KAFKA_GROUP_ID=sensor-producer

    ```