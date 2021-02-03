import firebase_admin
from firebase_admin import credentials

from django.conf import settings

from .models import FCM
# from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


cred = credentials.Certificate(settings.GOOGLE_APPLICATION_CREDENTIALS)
app = firebase_admin.initialize_app(cred)


@api_view(['POST'])
def register_token(request):
    token = request.data['token']
    if token is not None:
        FCM.objects.create(token=token)
    else:
        return "No token"


@api_view(['GET', 'POST'])
def subscribe(request):
    registration_tokens = request.data['token']
    # These registration tokens come from the client FCM SDKs.

    # Subscribe the devices corresponding to the registration tokens to the
    # topic.
    response = app.messaging.subscribe_to_topic(registration_tokens, topic)
    # See the TopicManagementResponse reference documentation
    # for the contents of response.
    print(response.success_count, 'tokens were subscribed successfully')


@api_view(['GET', 'POST'])
def unsubscribe(request):
    registration_tokens = request.data['token']

    # Unubscribe the devices corresponding to the registration tokens from the
    # topic.
    response = app.messaging.unsubscribe_from_topic(registration_tokens, topic)
    # See the TopicManagementResponse reference documentation
    # for the contents of response.
    print(response.success_count, 'tokens were unsubscribed successfully')