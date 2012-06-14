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

from google.appengine.ext import db
from google.appengine.api import users
import pytz.gae


#  Database Model
class EnvVars(db.Model):
    ad_provider = db.StringProperty(required=True,
                                    choices=set(['AdSense', 'devMode']))
    default_tz = db.StringProperty(required=True)


def tz_list():
    return pytz.common_timezones

def env_vars():
    app_vars = db.GqlQuery('SELECT * FROM EnvVars')
    if not app_vars.get():
        ad_provider = 'devMode'
        default_tz = 'America/Los_Angeles'
        record = EnvVars(ad_provider=ad_provider, default_tz=default_tz)
        record.put()
    return app_vars.get()

def update_vars(self, adp, dtz):
    app_vars = db.GqlQuery('SELECT * FROM EnvVars')
    if not app_vars.get():  # record does not exist yet create it
        record = EnvVars(ad_provider=adp, default_tz=dtz)
        # check if user is admin and update the data else raise 401
        if users.is_current_user_admin():
            try:  
                record.put()
                return(True)
            except:
                self.error(500)
        else:
            self.error(401)
    else:  # record exists so update it
        record = app_vars.get()
        setattr(record, 'ad_provider', adp)
        setattr(record, 'default_tz', dtz)
        # check if user is admin and update the data else raise 401
        if users.is_current_user_admin():
            try:  
                record.put()
                return(True)
            except:
                self.error(500)
        else:
            self.error(401)
