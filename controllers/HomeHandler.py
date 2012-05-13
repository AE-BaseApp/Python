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

#  tz
import pytz.gae

#  Import Models
from models.Shout import post_shout
from models.Shout import shouts
from models.UserProfile import ProfileCrud
from models.EnvVars import env_vars

#  Import Views
from views.home_view import home_view


#  Homepage Request Handler Class
class HomeHandler(webapp2.RequestHandler):
    def get(self):
        loggedin = "?"
        user = users.get_current_user()
        if user:
            uid = user.user_id()
            crud = ProfileCrud(uid)
            shout_tz = pytz.timezone(crud.profile().time_zone)
            shout_list = shouts(self, shout_tz)
            values = {'shouts': shout_list, 'loggedin': loggedin,
                      'logout_url': users.create_logout_url("/"),
                      'profile': crud.profile(), 'app_vars': env_vars()}
        else:
            shout_tz = pytz.timezone(env_vars().default_tz)
            shout_list = shouts(self, shout_tz)
            loggedin = "Anonymous"
            values = {'shouts': shout_list, 'loggedin': loggedin,
                      'logout_url': users.create_logout_url("/"),
                      'app_vars': env_vars()}
        home_view(self, values)

    def post(self):
        user = users.get_current_user()
        uid = user.user_id()
        crud = ProfileCrud(uid)
        post_shout(self, 
                   message=self.request.get('message'), 
                   who=crud.profile().user_name, 
                   uid=uid)
        self.redirect('/')
