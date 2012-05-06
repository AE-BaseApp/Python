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

# Import Models
from models.UserProfile import UserProfile
from models.EnvVars import EnvVars


#  Login page Request Handler Class
class ProfileHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        uid = user.user_id()
        profile = db.GqlQuery('SELECT * FROM UserProfile WHERE uid = :1', uid)
        app_vars = db.GqlQuery('SELECT * FROM EnvVars')

        # If no profile send them to complete it otherwise route them back to home
        if not profile.get():
            values = {'user': user, 
                      'profile': profile.get(), 
                      'app_vars': app_vars,
                      'time_zones': pytz.common_timezones}
            self.response.out.write(template.render('views/profile.html', values))
        else:
            self.redirect('/')

    def post(self):
        user = users.get_current_user()
        cid = user.user_id()
        profile = UserProfile(uid=cid,
                              user_name=self.request.get('user_name'),
                              first_name=self.request.get('first_name'),
                              last_name=self.request.get('last_name'),
                              email=self.request.get('email'),
                              time_zone=self.request.get('time_zone'))
        profile.put()
        self.redirect('/')
