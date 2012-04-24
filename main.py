#!/usr/bin/env python

#  Copyright 2010-2012 Mark Finch
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

import webapp2
import wsgiref.handlers
import datetime
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users

class Shout(db.Model):
  message = db.TextProperty(required=True)
  when = db.DateTimeProperty(auto_now_add=True)
  who = db.StringProperty()

class MyHandler(webapp2.RequestHandler):
  def get(self):
    shouts = db.GqlQuery('SELECT * FROM  Shout ORDER BY when DESC LIMIT 10')
    values = { 'shouts': shouts }
    self.response.out.write(template.render('main.html', values ))
  def post(self):
    shout = Shout(message=self.request.get('message'),
                  who=self.request.get('who'),
                  when=self.request.get('when'))
    shout.put()
    self.redirect('/')


app = webapp2.WSGIApplication([('/', MyHandler)], debug=True)

def main():
    application.run()

if __name__ == "__main__":
    main()
