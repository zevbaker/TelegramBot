from bot import telegram_chatbot
import gizoogle

bot = telegram_chatbot("config.cfg")


def make_reply(msg):
    reply = None
    if msg is not None:

        reply = gizoogle.text(msg)
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
