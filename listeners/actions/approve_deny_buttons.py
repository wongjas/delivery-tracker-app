from logging import Logger

def deny_delivery_callback(ack, body, client, logger: Logger):
    try:
        ack()

        delivery_id = body['message']['text'].split('*')[1]
        # Update the original message so you can't press it twice.
        client.chat_update(
            channel=body["container"]["channel_id"],
            ts=body["container"]["message_ts"],
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"Delivery *{delivery_id}* was incorrect, please enter another delivery ID ❌"
                    }
                }
            ]
        )
        
        logger.info(f"Delivery denied by user {body['user']['id']}")
    except Exception as e:
        logger.error(e)
