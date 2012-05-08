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
from models.Validate import Validate
from models.UserProfile import UserProfile
from models.EnvVars import EnvVars


#  Validation Handler Class
class ValidateHandler(webapp2.RequestHandler):
    def get(self):
        #  Get the environment variables
        user = users.get_current_user()
        uid = user.user_id()
        query_string = self.request.query_string

        #  Setup the Queries
        profileq = db.GqlQuery('SELECT * FROM UserProfile WHERE uid = :1', uid)
        app_varsq = db.GqlQuery('SELECT * FROM EnvVars')
        validateq = db.GqlQuery('SELECT * FROM Validate WHERE uid = :1', uid)

        #  Grab the Records
        profile = profileq.get()
        validate = validateq.get()
        app_vars = app_varsq.get()

        #  Perform Validation
        if validate.validation_code == query_string:
            setattr(profile, 'validated', True)
            profile.put()
            values = {'profile': profile, 'app_vars': app_vars, 'loggedin': "?",
                      'logout_url': users.create_logout_url("/")}
            self.response.out.write(template.render('views/thanks.html', values))
            #  Clean up the verify table
            db.delete(validate)
        else:
            values = {'app_vars': app_vars, 'loggedin': "Anonymous"}
            self.response.out.write(template.render('views/validation-error.html', values))
            #  TODO create a form to allow user to manually enter their code

#  TODO create a cron job to periodically sort through the Validate model to
#  find expired codes and delete them
