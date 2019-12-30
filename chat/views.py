import json

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views import View


# Create your views here.

class IndexView(View):

    def get(self, request):
        return render(request, 'chat/index.html')


index = IndexView.as_view()


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
