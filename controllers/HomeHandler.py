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
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp import template

# Import Models
from models.Shout import Shout
from models.UserProfile import UserProfile
from models.EnvVars import EnvVars


#  Homepage Request Handler Class
class HomeHandler(webapp2.RequestHandler):
    def get(self):
        loggedin = "?"
        user = users.get_current_user()
        app_vars = db.GqlQuery('SELECT * FROM EnvVars')
        shouts = db.GqlQuery('SELECT * FROM Shout ORDER BY when DESC LIMIT 10')
        if user:
            uid = user.user_id()
            profile = db.GqlQuery('SELECT * FROM UserProfile WHERE uid = :1', uid)
            values = {'shouts': shouts, 'loggedin': loggedin,
                      'logout_url': users.create_logout_url("/"),
                      'profile': profile.get(), 'app_vars': app_vars.get()}
        else:
            loggedin = "Anonymous"
            values = {'shouts': shouts, 'loggedin': loggedin,
                      'logout_url': users.create_logout_url("/"),
                      'app_vars': app_vars.get()}
        self.response.out.write(template.render('views/home.html', values))

    def post(self):
        user = users.get_current_user()
        cid = user.user_id()
        profileq = db.GqlQuery('SELECT * FROM UserProfile WHERE uid = :1', cid)
        profile = profileq.get()
        shout = Shout(message=self.request.get('message'),
                      who=profile.user_name, uid=cid)
        shout.put()
        self.redirect('/')
