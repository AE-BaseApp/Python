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

#  Libraries
import webapp2
import email
from datetime import datetime
from google.appengine.api import users
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

#  Gravatar Libraries
import urllib
import hashlib
from email.utils import parseaddr

#  Import Models
from models.Info import Info
from models.Info import store_message
from models.Attachments import store_file

#  Login page Request Handler Class
class InfoInboundHandler(InboundMailHandler):
    def receive(self, mail_message):
        # Field Validation - if the fields are not present then we don't error
        if hasattr(mail_message, 'cc'):
            info_cc = mail_message.cc
        else:
            info_cc = ""

        if hasattr(mail_message, 'subject'):
            info_subject = mail_message.subject
        else:
            info_subject = ""

        # Retrieve file attachments
        info_file = []
        info_list = []
        if hasattr(mail_message, 'attachments'):
            file_name = ""
            file_blob = ""
            for filename, filecontents in mail_message.attachments:
                file_name = filename
                file_blob = filecontents.decode()
                # Hack to strip out Unicode and leave only ASCII to prevent 
                # blob from erroring about the unicode 
                if isinstance(file_blob, unicode):
                    file_blob = file_blob.encode('ascii', 'ignore')
                    file_name = file_name + ".unicode"
                    info_file.append(file_name)
                    info_list.append(str(store_file(self, file_name, file_blob)))
                else:
                    info_file.append(file_name)
                    info_list.append(str(store_file(self, file_name, file_blob)))

        # Retrieve the bodies from message
        html_msg = ""
        for text in mail_message.bodies('text/html'):
            html_msg = text[1].decode()

        text_msg = ""        
        for text in mail_message.bodies('text/plain'):
            text_msg = text[1].decode()

        # Create Gravatar URL
        default_avatar = "http://ae-python.appspot.com/static/images/avatar.png"
        avatar_size = 64
        avatar_email = parseaddr(mail_message.sender)[1]
        gravatar_url = "http://www.gravatar.com/avatar.php?"
        gravatar_url += urllib.urlencode(
            {'gravatar_id':hashlib.md5(avatar_email.lower()).hexdigest(),
             'default':default_avatar, 'size':str(avatar_size)})


        # Retrieve the original message for storage
        info_original = mail_message.original
        info_key = store_message(msg_original="original", # mail_message.original,
                                 msg_sender=mail_message.sender,
                                 msg_to=mail_message.to,
                                 msg_cc=info_cc,
                                 msg_date=datetime.strptime(mail_message.date,
                                                 '%a, %d %b %Y %H:%M:%S -0700'),
                                 msg_subject=info_subject,
                                 msg_html=html_msg,
                                 msg_txt=text_msg,
                                 msg_file=info_file,
                                 msg_list=info_list,
                                 msg_avatar=gravatar_url)
