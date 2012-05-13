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

# import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users

#  Email Libraries
from google.appengine.api import mail

def send_verification(self, email_values, validation_link, address):
    message = mail.EmailMessage(sender="AE-BaseApp <verify@ae-python.appspotmail.com>",
                                subject="AE-BaseApp Account Verification")
    message.to = address
    message.body = template.render('templates/validation-email.txt', email_values)
    message.html = template.render('templates/validation-email.html', email_values)
    message.send()
