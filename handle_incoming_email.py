# -*- coding: utf-8 -*-
"""
Botch-System

References:
- http://code.google.com/intl/en/appengine/docs/python/mail/sendingmail.html
- http://code.google.com/intl/ja/appengine/docs/python/mail/receivingmail.html
"""
import logging, webapp2

from random import Random
from google.appengine.api import mail
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

r = Random()

def get_receiver_addr(sender_addr):
    return "your-friend@botch-system.appspotmail.com"

def get_random_body():
    return r.choice(
        ["メールありがと！",
         "おはよう！",
         "o(^-^)o"])

class MyInboundMailHandler(InboundMailHandler):
    def receive(self, message):
        mail.send_mail(sender=get_receiver_addr(message.sender),
                       to=message.sender,
                       subject="RE: %s" % message.subject,
                       body=get_random_body())

app = webapp2.WSGIApplication([MyInboundMailHandler.mapping()], debug=True)

