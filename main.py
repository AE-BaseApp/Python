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
import logging
from google.appengine.ext.webapp import template

#  Local Controllers
from controllers.HomeHandler import HomeHandler
from controllers.LoginHandler import LoginHandler
from controllers.ProfileHandler import ProfileHandler
from controllers.ValidateHandler import ValidateHandler
from controllers.AdminHandler import AdminHandler
from controllers.VerifyHandler import VerifyHandler

#  Setup the Application & Routes
app = webapp2.WSGIApplication([
    (r'/', HomeHandler),
    (r'/login', LoginHandler),
    (r'/profile', ProfileHandler),
    (r'/verify', ValidateHandler),
    (r'/_ah/mail/verify@.*ae-python\.appspotmail\.com', VerifyHandler),
    (r'/admin', AdminHandler)
], debug=True)
#  TODO: Set debug=False on production


def handle_401(request, response, exception):
    logging.exception(exception)
    values = {}
    response.out.write(template.render('templates/401.html', values))
    response.set_status(401)


def handle_403(request, response, exception):
    logging.exception(exception)
    values = {}
    response.out.write(template.render('templates/403.html', values))
    response.set_status(403)


def handle_404(request, response, exception):
    logging.exception(exception)
    values = {}
    response.out.write(template.render('templates/404.html', values))
    response.set_status(404)


def handle_500(request, response, exception):
    logging.exception(exception)
    values = {}
    response.out.write(template.render('templates/500.html', values))
    response.set_status(500)

app.error_handlers[401] = handle_401
app.error_handlers[403] = handle_403
app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500
#  Add other error pages that you need such as:
#      301 Moved Permanently
#      303 See Other
#      400 Bad Request
#      408 Request Timeout
#      503 Service Unavailable
# http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
