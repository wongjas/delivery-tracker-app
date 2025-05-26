import re

from slack_bolt import App
from .delivery_message import delivery_message_callback

# To receive messages from a channel or dm your app must be a member!
def register(app: App):
    app.message(re.compile(r"hi|hello|hey", re.IGNORECASE))(delivery_message_callback)
