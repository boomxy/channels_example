from django.urls import path, re_path

from chat import consumers

# 这 4 个 path 都是互斥 请使用其中一个测试
websocket_urlpatterns = [
    # path('ws/chat/<str:room_name>/', consumers.ChatConsumer),  # 单人版本
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),  # 使用正则path 版 1
    # path('ws/chat/<str:room_name>/', consumers.ChatConsumerSync),  # group 版本
    path('ws/chat/<str:room_name>/', consumers.ChatConsumerAsync),  # Async 版本
]
