# -*- coding: utf-8 -*-
import humanize
import datetime
import re

def process_message(bot, message):

    #how old?
    if re.match('How old is IF\?', message['text'], re.IGNORECASE):
        response = humanize.naturaltime(datetime.datetime.now() - datetime.datetime(2015, 9, 30))
        response = response.replace(' ago', ' old')
        bot.send_message(response, message['channel'])

    if re.match("How long until IF.?s birthday\?", message['text'], re.IGNORECASE):
        birthday = datetime.datetime(2015, 9, 30)
        today = datetime.datetime.now()
        next_birthday = datetime.datetime(today.year, 9, 30)
        if today > datetime.datetime(today.year, 9, 30):
            next_birthday = datetime.datetime(today.year + 1, 9, 30)

        delta =  next_birthday - today
        if delta.days == 1:
            response = "%s %s" % (delta.days, "day to go!")
        elif delta.days == 0:
            response = "Happy Birthday! 🎂🎂🎂"
        else:
            response = "%s %s" % (delta.days, "days to go!")

        bot.send_message(response, message['channel'])