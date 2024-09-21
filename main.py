from fastapi import FastAPI
from kafka_handler import KafkaHandler
from kafka_configuration import KafkaConfiguration

kafka_config = KafkaConfiguration()
kafka_handler = KafkaHandler(config=kafka_config)

class MyFastAPI:
    def __init__(self, kafka_handler: KafkaHandler):
        self.kafka_handler = kafka_handler
        self.app = FastAPI()

        @self.app.on_event("startup")
        async def startup_event():
            await self.kafka_handler.start()

        @self.app.on_event("shutdown")
        async def shutdown_event():
            await self.kafka_handler.stop()

my_fastapi = MyFastAPI(kafka_handler)

app = my_fastapi.app
