import json
from channels.generic.websocket import WebsocketConsumer


class PageVisitConsumer(WebsocketConsumer):
    page_id = None
    user_id = None

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        print(f"disconnect  Page ID - {self.page_id}, User ID - {self.user_id}")
        pass

    def receive(self, text_data):
        # Parse the incoming JSON data
        data = json.loads(text_data)

        self.page_id = data.get('page_id')
        self.user_id = data.get('user_id')

        print(f"Received data: Page ID - {self.page_id}, User ID - {self.user_id}")
