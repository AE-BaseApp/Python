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
import logging
from google.appengine.ext import db

class FileBlob(db.Model):
    file_name = db.StringProperty()
    file_blob = db.BlobProperty()
    stored_on = db.DateTimeProperty(auto_now_add=True)

def store_file(self, file_name, file_blob):
    new_file = FileBlob(file_name = file_name, 
                        file_blob = file_blob)
    try:
        return new_file.put()
    except Timeout:
        logging.info("Timeout occured storing file: " + file_name)
        return ("Put timed out on: " + file_name)
    except BadValueError:
        logging.info("BadValueError on storing file: " + file_name)
        return ("An error occured storing " + file_name)
    except BadRequestError:
        logging.info("BadValueError on storing file: " + file_name)
        return ("An error occured processing the request to store " + file_name)

def get_attach_by_key(self, key):
    try:
        return db.get(key)
    except BadKeyError:
        logging.info("Bad key on: " + key)
        return ("A bad Key was sent: " + key)
    except BadValueError:
        logging.info("Bad Value on: " + key)
        return ("An Error occured getting key: " + key + " the value was invalid.")
