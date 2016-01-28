# -*- coding: utf-8 -*-
from datetime import datetime

cron_interval = 60

def cron_job(bot):
    now = datetime.now()
    if now.weekday() not in [5,6]:
        if now.hour == 9 and now.minute == 55:
            channel = bot.slack_client.server.channels.find('general')
            bot.send_message('🕙 Standup in 5 minutes', channel.id)