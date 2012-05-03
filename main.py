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
import wsgiref.handlers

#  Local Controllers
from controllers.HomeHandler import HomeHandler
from controllers.LoginHandler import LoginHandler
from controllers.ProfileHandler import ProfileHandler
from controllers.AdminHandler import AdminHandler

#  Run the App and Setup Routes
app = webapp2.WSGIApplication([
    (r'/', HomeHandler),
    (r'/login', LoginHandler),
    (r'/profile', ProfileHandler),
    (r'/admin', AdminHandler)
], debug=True)


def main():
    application.run()
