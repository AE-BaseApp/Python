#  Copyright 2010 - 2012 Mark Finch
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not use this
#  file except in compliance with the License. You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software distributed under
#  the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
#  ANY KIND, either express or implied. See the License for the specific language
#  governing permissions and limitations under the License.

#  Libraries
import webapp2
from pytz.gae import pytz
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp import template

#  Email Libraries
from google.appengine.api import mail

#  Validation Libraries
import uuid

#  Import Models
from models.UserProfile import UserProfile
from models.EnvVars import EnvVars
from models.Validate import Validate


#  Login page Request Handler Class
class ProfileHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        uid = user.user_id()
        profileq = db.GqlQuery('SELECT * FROM UserProfile WHERE uid = :1', uid)
        app_varsq = db.GqlQuery('SELECT * FROM EnvVars')

        # If no profile send them to complete it otherwise route them back to home
        if not profileq.get():
            values = {'user': user,
                      'profile': profileq.get(),
                      'app_vars': app_varsq,
                      'time_zones': pytz.common_timezones}
            self.response.out.write(template.render('views/profile.html', values))
        else:
            profile = profileq.get()
            setattr(profile, 'last_ip', self.request.remote_addr)
            profile.put()
            self.redirect('/')

    def post(self):
        user = users.get_current_user()
        cid = user.user_id()

        #  Store the Profile
        profile = UserProfile(uid=cid,
                              user_name=self.request.get('user_name'),
                              first_name=self.request.get('first_name'),
                              last_name=self.request.get('last_name'),
                              email=self.request.get('email'),
                              time_zone=self.request.get('time_zone'),
                              last_ip=self.request.remote_addr,
                              validated=False)
        profile.put()

        #  Generate Validation Code and Send out Validation Email
        validation_code = str(uuid.uuid4())
        validation_link = "http://ae-python.appspot.com/verify?" + validation_code
        email_values = {'first_name': self.request.get('first_name'),
                        'validation_link': validation_link}
        message = mail.EmailMessage(sender="AE-BaseApp <verify@ae-python.appspotmail.com>",
                                    subject="AE-BaseApp Account Verification")
        message.to = self.request.get('email')
        message.body = template.render('views/validation-email.txt', email_values)
        message.html = template.render('views/validation-email.html', email_values)
        message.send()
        #  Store Validation Information in Datastore
        validate = Validate(uid=cid,
                             validation_code=validation_code)
        validate.put()
        self.redirect('/')
