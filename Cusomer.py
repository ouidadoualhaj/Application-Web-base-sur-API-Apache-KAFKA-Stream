from kafka import KafkaConsumer
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Configure Kafka consumer
consumer = KafkaConsumer('costumerchurn', bootstrap_servers='localhost:9092', group_id='1', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Placeholder for pre-processed data
preprocessed_data = []

try:
    for message in consumer:
        # Extract the message value
        data = message.value
        
        # Pre-processing steps (replace with your own pre-processing logic)
        # Example: Convert data to DataFrame and scale numeric features
        df = pd.DataFrame([data])
        numeric_features = df.select_dtypes(include=['float64']).columns
        scaler = StandardScaler()
        df[numeric_features] = scaler.fit_transform(df[numeric_features])
        
        # Save pre-processed data to a CSV file
        df.to_csv('data_from_kafkaaa.csv', mode='a', index=False, header=not bool(preprocessed_data))  # Append mode after the first write
        # Append pre-processed data to the list
        preprocessed_data.append(df)
        
        # Print the pre-processed data (replace with your own logic)
        print("Pre-processed Data:")
        print(df)

except KeyboardInterrupt:
    pass  # Handle keyboard interrupt gracefully, allowing the script to be stopped

# Close the consumer
consumer.close()