from aiokafka import AIOKafkaConsumer
import logging
import asyncio
from kafka_configuration import KafkaConfiguration

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KafkaHandler:
    def __init__(self, config: KafkaConfiguration):
        self.config = config
        self.consumer: AIOKafkaConsumer = None

    async def start(self):
        self.consumer = AIOKafkaConsumer(
            self.config.topic,
            bootstrap_servers=self.config.bootstrap_servers,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id=self.config.group_id
        )
        await self.consumer.start()
        asyncio.create_task(self.consume_messages())

    async def stop(self):
        await self.consumer.stop()

    async def consume_messages(self):
        try:
            async for message in self.consumer:
                decoded_message = message.value.decode('utf-8')
                logger.info(f"Received message: {decoded_message}")
        except Exception as e:
            logger.error(f"Error while consuming messages: {e}")
