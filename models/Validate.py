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

from google.appengine.ext import db


#  Database Model
class Validate(db.Model):
    uid = db.StringProperty(required=True)
    validation_code = db.StringProperty(required=True)
    validation_time = db.DateTimeProperty(auto_now_add=True)

def save_validation_code(self, uid, validation_code):
    record = Validate(uid = uid, validation_code = validation_code)
    record.put()
