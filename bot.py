import os
from slackrobot import SlackRobot

slackbot = SlackRobot(os.environ['SLACK_API_TOKEN'])
slackbot.start()