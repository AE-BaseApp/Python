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

# Libraries
from google.appengine.ext import db
from validation.email import email_re

# Import Models
from Validate import Validate

#  Database Model
class UserProfile(db.Model):
    uid = db.StringProperty(required=True)
    user_name = db.StringProperty(required=True)
    first_name = db.StringProperty(required=True)
    last_name = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    avatar = db.StringProperty()
    time_zone = db.StringProperty(required=True)
    last_ip = db.StringProperty(required=True)
    since = db.DateTimeProperty(auto_now_add=True)
    validated = db.BooleanProperty(required=True)
    # add last login date time


class ProfileCrud:
    def __init__(self, cid):
        self.cid = cid

    def update_ip(self, ip):
        profile = db.GqlQuery('SELECT * FROM UserProfile WHERE uid = :1',
                              self.cid).get()
        setattr(profile, "last_ip", ip)
        profile.put()

    def profile(self):
        return db.GqlQuery('SELECT * FROM UserProfile WHERE uid = :1',
                           self.cid).get()

    def update_profile(self, user_name, first_name, last_name, email, avatar,
                       time_zone, last_ip):
        #  Validate the input
        if not email_re.match(email):
            return("email")
        elif user_name == None or "":
            return("user")
        elif first_name == None or "":
            return("first")
        elif last_name == None or "":
            return("last")
        elif time_zone == None or "":
            return("tz")

        #  Store the Profile
        profile = db.GqlQuery('SELECT * FROM UserProfile WHERE uid = :1',
                              self.cid).get()
        if not profile:
            new_profile = UserProfile(uid=self.cid,
                                      user_name=user_name,
                                      first_name=first_name,
                                      last_name=last_name,
                                      email=email,
                                      avatar=avatar,
                                      time_zone=time_zone,
                                      last_ip=last_ip,
                                      validated=False)
            new_profile.put()
        else:
            setattr(profile, "first_name", first_name)
            setattr(profile, "last_name", last_name)
            setattr(profile, "email", email)
            setattr(profile, "avatar", avatar)
            setattr(profile, "time_zone", time_zone)
            setattr(profile, "last_ip", last_ip)
            profile.put()
        return("OK")

    def delete_profile(self):  # TODO: expose delete profile to user add verification
        profile = db.GqlQuery('SELECT * FROM UserProfile WHERE uid = :1',
                              self.cid).get()
        db.delete(profile)

    def is_validated(self):
        profile = db.GqlQuery('SELECT * FROM UserProfile WHERE uid = :1',
                              self.cid).get()
        return(profile.validated)

    def validate_email(self, query_string):
        validate = db.GqlQuery('SELECT * FROM Validate WHERE uid = :1',
                               self.cid).get()
        profile = db.GqlQuery('SELECT * FROM UserProfile WHERE uid = :1',
                              self.cid).get()
        if validate.validation_code == query_string:
            setattr(profile, 'validated', True)
            profile.put()
            db.delete(validate)
            return(True)
        else:
            return(False)
