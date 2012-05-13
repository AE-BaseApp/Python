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

#  Import Models
from models.UserProfile import ProfileCrud
from models.EnvVars import env_vars

#  Import Views
from views.validate_view import validate_view

#  Validation Handler Class
class ValidateHandler(webapp2.RequestHandler):
    def get(self):
        #  Get the environment variables
        user = users.get_current_user()
        uid = user.user_id()
        query_string = self.request.query_string

        #  Perform Validation
        crud = ProfileCrud(uid)
        #  TODO catch not logged in error lookup request url to set redirect
        if crud.validate_email(query_string):
            values = {'profile': crud.profile(), 'app_vars': env_vars(),
                      'loggedin': "?", 'logout_url': users.create_logout_url("/")}
            validation_error = False
            validate_view(self, values, validation_error)
        else:
            values = {'app_vars': env_vars(), 'loggedin': "Anonymous"}
            validation_error = True
            validate_view(self, values, validation_error)
            #  TODO create a form to allow user to manually enter their code

#  TODO create a cron job to periodically sort through the Validate model to
#  find expired codes and delete them
