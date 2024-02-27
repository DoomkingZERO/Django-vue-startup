# # consumers.py
# import json
# from channels.generic.websocket import WebsocketConsumer
# from .models import PageVisit


# class PageVisitConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()
#
#     def disconnect(self, close_code):
#         # Update tracking data when WebSocket connection is closed
#         pass
#
#     def receive(self, text_data):
#         data = json.loads(text_data)
#         if data['type'] == 'visit':
#             # Create a new PageVisit instance
#             PageVisit.objects.create(
#                 user_id=data['user_id'],
#                 page_id=data['page'],
#                 start_time=data['timestamp']
#             )
#         elif data['type'] == 'leave':
#             # Update the PageVisit instance with stop_time
#             visit = PageVisit.objects.filter(user_id=data['user_id'], page_id=data['page']).last()
#             if visit:
#                 visit.stop_time = data['timestamp']
#                 visit.save()
#
#     def send(self, text_data):
#         # Send message to WebSocket
#         self.send(text_data=text_data)


import json
from channels.generic.websocket import WebsocketConsumer


class PageVisitConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass
