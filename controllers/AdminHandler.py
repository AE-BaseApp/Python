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
import pytz

# Import Models
from models.EnvVars import EnvVars


#  Homepage Request Handler Class
class AdminHandler(webapp2.RequestHandler):
    def get(self):
        if not users.is_current_user_admin():  # secure the page only admin can access
            self.redirect('/')
        app_vars = db.GqlQuery('SELECT * FROM EnvVars')
        values = {'logout_url': users.create_logout_url("/"), 
                  'app_vars': app_vars.get(),
                  'time_zones': pytz.common_timezones}
        self.response.out.write(template.render('views/admin.html', values))

    def post(self):
        app_vars = db.GqlQuery('SELECT * FROM EnvVars')
        if not app_vars.get():  # record does not exist yet create it
            app_vars = EnvVars(ad_provider=self.request.get('adp'),
                               default_tz=self.request.get('default_tz'))
            app_vars.put()
        else:  # record exists so update it
            record = app_vars.get()
            setattr(record, 'ad_provider', self.request.get('adp'))
            setattr(record, 'default_tz', self.request.get('default_tz'))
            record.put()
        self.redirect('/admin')

# try http://stackoverflow.com/questions/5066357/update-app-engine-entity
