from kafka import KafkaProducer
import pandas as pd
import json
import time

# Configure Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Specify the path to your CSV file
csv_file_path = 'customer_churn.csv'

while True:
    # Read data from CSV
    df = pd.read_csv(csv_file_path)

    # Produce data to Kafka topic
    for _, row in df.iterrows():
        message = row.to_dict()
        producer.send('costumerchurn', value=message)

    # Add a delay (adjust as needed)
    time.sleep(0.1)  # Delay for 60 seconds