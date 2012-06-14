#  Copyright 2010 - 2012 Mark Finch, 
#  Snippet truncate Copyright phektus 2011
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
import webapp2
from google.appengine.ext.webapp import template

register = template.create_template_register()

# truncate returns the string truncated to the last word that fits into the
# limit set currently at +5 otherwise it truncates at the argument.  It can 
# return a string longer than the argument.
# DJango Snippet 2382 http://djangosnippets.org/snippets/2382/
@register.filter
def truncate(value, arg):
    data = str(value)
    if len(value) < arg:
        return data     
        
    if data.find(' ', arg, arg+5) == -1:
        return data[:arg] + '...'
    else:
        return data[:arg] + data[arg:data.find(' ', arg)] + '...'
