#  Copyright 2010 - 2012 Mark Finch
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not
#  use this file except in compliance with the License. You may obtain a copy
#  of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

# Libraries
from datetime import datetime
from google.appengine.ext import db

# Database Model
class Info(db.Model):
    original_msg = db.StringProperty()
    sender = db.StringProperty(required=True)
    to = db.StringProperty()
    cc = db.StringProperty()
    date = db.DateTimeProperty(required=True)
    subject = db.StringProperty()
    body_html = db.TextProperty()
    body_txt = db.TextProperty()
    read = db.BooleanProperty()
    read_on = db.DateTimeProperty()
    file_list = db.StringListProperty()
    attachment_list = db.StringListProperty()
    gravatar_url = db.StringProperty()
    replied = db.BooleanProperty()
    reply_key = db.StringProperty()
    received_on = db.DateTimeProperty(auto_now_add=True)

def store_message(msg_original, msg_sender, msg_to, msg_cc, msg_date,
                  msg_subject, msg_html, msg_txt, msg_file, msg_list, msg_avatar):
    new_message = Info(original_msg=msg_original,
                       sender=msg_sender,
                       to=msg_to,
                       cc=msg_cc,
                       date=msg_date,
                       subject=msg_subject,
                       body_html=msg_html,
                       body_txt=msg_txt,
                       read=False,
                       file_list=msg_file,
                       attachment_list=msg_list,
                       gravatar_url=msg_avatar)
    msg_key = new_message.put()
    return msg_key

def fetch_messages():
    messagesq = db.GqlQuery('SELECT * FROM Info ORDER BY received_on DESC')
    messages = messagesq.fetch(10, offset=0)
    return messages

def get_msg_by_key(key):
    msg = db.get(key)
    setattr(msg, "read", True)
    setattr(msg, "read_on", datetime.utcnow())
    msg.put()
    return msg

def set_reply_key(key, msg_key):
    msg = db.get(key)
    setattr(msg, "replied", True)
    setattr(msg, "reply_key", msg_key)
    msg.put()

class InfoReply(db.Model):
    message_key = db.StringProperty()
    sender = db.StringProperty()
    to = db.StringProperty()
    cc = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    subject = db.StringProperty()
    body_html = db.TextProperty()
    body_txt = db.TextProperty()

def store_reply(msg_key, msg_sender, msg_to, msg_cc, msg_subject, msg_html,
                msg_txt):
    new_message = InfoReply(message_key=msg_key,
                            sender=msg_sender,
                            to=msg_to,
                            cc=msg_cc,
                            subject=msg_subject,
                            body_html=msg_html,
                            body_txt=msg_txt)
    m_key = new_message.put()
    return m_key
