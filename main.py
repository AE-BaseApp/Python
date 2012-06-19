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
import os
import logging
from google.appengine.ext.webapp import template

#  Local Controllers
from controllers.HomeHandler import HomeHandler
from controllers.LoginHandler import LoginHandler
from controllers.RouteLogin import RouteLogin
from controllers.ProfileHandler import ProfileHandler
from controllers.ValidateHandler import ValidateHandler
from controllers.AdminHandler import AdminHandler
from controllers.VerifyHandler import VerifyHandler
from controllers.InfoHandler import InfoHandler
from controllers.InfoMsgHandler import InfoMsgHandler
from controllers.InfoInboundHandler import InfoInboundHandler
from controllers.AttachmentsHandler import AttachmentsHandler

#  Register Django Template Filters
template.register_template_library('views.djangofilters')

# os.environ idea from dave-w-smith on StackOverflow question 1916579
if os.environ['SERVER_SOFTWARE'].startswith('Development'):
    app_scheme = 'http'
else:
    app_scheme = 'https'

#  Setup the Application & Routes
app = webapp2.WSGIApplication([
    webapp2.Route(r'/', HomeHandler),
    webapp2.Route(r'/verify', ValidateHandler, schemes=[app_scheme]),
    webapp2.Route(r'/login', LoginHandler, name='login', schemes=[app_scheme]),
    webapp2.Route(r'/login', RouteLogin),
    webapp2.Route(r'/profile', ProfileHandler, name='profile', schemes=[app_scheme]),
    webapp2.Route(r'/admin', AdminHandler, name='admin', schemes=[app_scheme]),
    webapp2.Route(r'/infoadmin', InfoHandler, name='infoadmin', schemes=[app_scheme]),
    webapp2.Route(r'/infomsg', InfoMsgHandler, name='infomsg', schemes=[app_scheme]),
    webapp2.Route(r'/attachment', AttachmentsHandler, schemes=[app_scheme]),
    (r'/_ah/mail/verify@.*ae-python\.appspotmail\.com', VerifyHandler),
    (r'/_ah/mail/info@.*ae-python\.appspotmail\.com', InfoInboundHandler)
], debug=True)
#  TODO: Set debug=False on production

def main():
    logging.getLogger().setLevel(logging.DEBUG)


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
