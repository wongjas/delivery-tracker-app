from listeners import messages
from listeners import actions

def register_listeners(app):
    messages.register(app)
    actions.register(app)