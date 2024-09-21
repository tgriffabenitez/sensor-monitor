import os
from dotenv import load_dotenv

load_dotenv()

class KafkaConfiguration:
    def __init__(self):
        self.bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        self.topic = os.getenv("KAFKA_TOPIC")
        self.group_id = os.getenv("KAFKA_GROUP_ID")
