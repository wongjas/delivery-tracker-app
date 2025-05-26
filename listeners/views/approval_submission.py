from logging import Logger
import os

def handle_approve_delivery_view(ack, client, view, logger: Logger):
    try:
        ack()
        
        delivery_id, update_channel = view["private_metadata"].split("|")
        delivery_notes = view["state"]["values"]["delivery_notes"]["delivery_notes_input"]["value"]
        delivery_location = view["state"]["values"]["delivery_location"]["delivery_location_input"]["value"]

        # Update original message
        client.chat_postMessage(
            channel=update_channel,
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"✅ Delivery *{delivery_id}* has been approved with the following details:"
                    }
                },
                {
                    "type": "section", 
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Delivery Notes:*\n{delivery_notes if delivery_notes else 'No additional notes provided'}"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn", 
                        "text": f"*Delivery Location:* {delivery_location if delivery_location else 'No location specified'}"
                    }
                }
            ]
        )

        # Extract just the numeric portion from delivery_id
        delivery_number = ''.join(filter(str.isdigit, delivery_id))


    except Exception as e:
        logger.error(f"Error in approve_delivery_view: {e}")