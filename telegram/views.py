import os

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from telegram.client import send_message
from rest_framework.response import Response


@api_view(['POST'])
@csrf_exempt
@authentication_classes([])
@permission_classes([])
def telegram(request):
    try:
        data = request.data
        chat_id = data['message']['chat']['id']
        text = data['message']['text']
        send_message(980106016, text)
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=400)
