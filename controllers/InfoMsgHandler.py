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
from google.appengine.api import users
from google.appengine.ext.webapp import template

#  Email Libraries
import email
from google.appengine.api import mail

# Import Views
from views.info_msg_view import display_msg

# Import Models
from models.Info import get_msg_by_key
from models.Info import set_reply_key
from models.Info import store_reply
from models.EnvVars import env_vars

#  Homepage Request Handler Class
class InfoMsgHandler(webapp2.RequestHandler):
    def get(self):
        if users.is_current_user_admin():  # secure the page only admin can access
            query_string = self.request.query_string
            message = get_msg_by_key(query_string)
            file_list = message.file_list
            attach_list = message.attachment_list
            attachments = zip(file_list, attach_list)
            values = {'logout_url': users.create_logout_url("/"),
                      'app_vars': env_vars(),
                      'message': message,
                      'attachments': attachments,
                      'qs': query_string}
            display_msg(self, values)
        else:
            self.abort(401)

    def post(self):
        response = self.request.get('message')
        query_string = self.request.get('query')
        msg = get_msg_by_key(query_string)
        email_values = {'response': response,
                        'msg': msg}
        reply = mail.EmailMessage()
        reply.sender="AE-Python Info <info@ae-python.appspotmail.com>"
        if hasattr(msg, 'subject'):
            reply.subject="RE:" + msg.subject
        else:
            reply.subject="RE: Your info Request to AE-Python"
        reply.to = msg.sender # + msg.to TODO split string to remove self
        if msg.cc == "":
            pass
        else:
            reply.cc = msg.cc
        reply.body = template.render('templates/info-email.txt', email_values)
        reply.html = template.render('templates/info-email.html', email_values)
        reply.send()
        reply_key = store_reply(msg_key=query_string,
                                msg_sender=reply.sender,
                                msg_to=reply.to,
                                msg_cc=msg.cc,  # don't set to reply could be none
                                msg_subject=reply.subject,
                                msg_html=reply.html,
                                msg_txt=reply.body)
        set_reply_key(query_string, str(reply_key))
        self.redirect('/infoadmin')
