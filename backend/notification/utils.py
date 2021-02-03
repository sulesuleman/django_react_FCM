import firebase_admin
from firebase_admin import credentials

from django.conf import settings

cred = credentials.Certificate(settings.GOOGLE_APPLICATION_CREDENTIALS)
app = firebase_admin.initialize_app(cred)


def notifcation(title, message):
    notification = {
        title: title,
        message: message,
    }
    print(notification)


def add_registered_token(token):
    try:
        if token is not None:
            message = token+': successfully added!'
            return message
        return 0
    except Exception as e:
        return e


def add_devices_to_topic(topic, registration_tokens=[]):
    try:
        response = app.messaging.subscribe_to_topic(registration_tokens, topic)
        if response.status in ["200", 200]:
            return response.success_count
        return 0
    except Exception as e:
        return e


def remove_device_to_topic(topic, registration_tokens=[]):
    try:
        response = app.messaging.unsubscribe_from_topic(registration_tokens, topic)
        if response.status in ['200', 200]:
            return(response.success_count)
        return 0
    except Exception as e:
        return e


def send_message_to_topic(topic, data={}):
    message = app.messaging.Message(
        data=data,
        topic=topic,
    )
    try:
        response = app.messaging.send(message)
        if response.status in ['200', 200]:
            return response
        return 0
    except Exception as e:
        return e


