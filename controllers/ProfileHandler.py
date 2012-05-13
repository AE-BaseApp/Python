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

#  Validation Libraries
import uuid

#  Import Models
from models.UserProfile import ProfileCrud
from models.EnvVars import env_vars
from models.EnvVars import tz_list
from models.Validate import save_validation_code

#  Import Views
from views.profile_view import profile_view
from views.send_verification import send_verification


#  Login page Request Handler Class
class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.abort(401)  # TODO: self.redirect doesn't work look into it
        uid = user.user_id()
        crud = ProfileCrud(uid)

        # If no profile send them to complete it otherwise route them back to home
        # TODO: Expose the update functionality it is already in place
        if not crud.profile():
            values = {'user': user,
                      'profile': crud.profile(),
                      'app_vars': env_vars(),
                      'time_zones': tz_list()}
            profile_view(self, values)
        else:
            crud.update_ip(self.request.remote_addr)
            self.redirect('/')

    def post(self):
        user = users.get_current_user()
        uid = user.user_id()
        crud = ProfileCrud(uid)

        # Create or Update the profile
        crud.update_profile(user_name=self.request.get('user_name'),
                            first_name=self.request.get('first_name'),
                            last_name=self.request.get('last_name'),
                            email=self.request.get('email'),
                            time_zone=self.request.get('time_zone'),
                            last_ip=self.request.remote_addr)

        #  Check if user has created a profile if not Generate Validation Code
        #  and Send out Validation Email
        if not crud.is_validated():
            validation_code = str(uuid.uuid4())
            #  TODO: Update validation_link to use coded domain
            validation_link = "http://ae-python.appspot.com/verify?" + validation_code
            email_values = {'first_name': self.request.get('first_name'),
                            'validation_link': validation_link}
            address = self.request.get('email')
            send_verification(self, email_values, validation_link, address)
            #  Store Validation Information in Datastore
            save_validation_code(self, uid, validation_code)

        #  Send the user back home after saving the profile
        self.redirect('/')
