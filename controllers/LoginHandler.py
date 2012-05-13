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

# Import Views
from views.login_view import login_view

#  OpenID providers
providers = {
    'Google': 'www.google.com/accounts/o8/id',
    'Yahoo': 'me.yahoo.com/',
    'AOL': 'openid.aol.com',
    # Add your providers here, note only providers who provide a login page
    # are currently supported.  The URL based method will be added in a future
    # version.
}


#  Login page Request Handler Class
class LoginHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        provider_list = []
        if user:
            first_name = user.nickname()
        else:
            first_name = "Anonymous"

        for name, uri in providers.items():
            provider_list.append((name, users.create_login_url(dest_url='/profile',
                          federated_identity=uri)))

        values = {'login_url': users.create_login_url("/profile"),
                  'provider_list': provider_list}
        login_view(self, values)
