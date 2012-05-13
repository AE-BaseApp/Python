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

import pytz.gae
from google.appengine.ext import db


#  Database Model
class Shout(db.Model):
    message = db.TextProperty(required=True)
    when = db.DateTimeProperty(auto_now_add=True)
    who = db.StringProperty(required=True)
    uid = db.StringProperty(required=True)

def shouts(self, tz):  #  TODO: Expose offset to allow shout navigation
    shouts_querry = db.GqlQuery('SELECT * FROM Shout ORDER BY when DESC')
    shouts_tz = shouts_querry.fetch(10, offset=0)
    for posts in shouts_tz:
        i = shouts_tz.index(posts)
        shouts_tz[i].when = shouts_tz[i].when.replace(tzinfo=pytz.utc).astimezone(tz)
    return shouts_tz

def post_shout(self, message, who, uid):
    #  TODO: decide if validating before posting 
    #  PROS: less garbage in Datastore, less chance of injection/XSS/etc
    #  CONS: higher CPU cost/response time, lack of libraries for app engine
    shout = Shout(message=message, who=who, uid=uid)
    shout.put()

#  TODO:  Add Update and Delete Shout abilities.
