import re

def process_message(bot, message):

    #how old?
    if re.match('What do you do?', message['text'], re.IGNORECASE):
        response = """ I give a 5 minute warning before standup.

        You can also ask me:
        - How old is IF?
        - How long until IF's birthday?
        """

        bot.send_message(response, message['channel'])