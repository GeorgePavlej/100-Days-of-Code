from twilio.rest import Client

TWILIO_SID = "AC7309b4fe59b3e287204ca6591078e715"
TWILIO_AUTH_TOKEN = "2a5e334d50fecf7cf31c74aa4d0ec8b3"
TWILIO_VIRTUAL_NUMBER = '+18564223249',
TWILIO_VERIFIED_NUMBER = '+447897513276'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages \
            .create(
            body=message,
            from_='+18564223249',
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
