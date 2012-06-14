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
import mimetypes
from google.appengine.api import users

# Import Models
from models.Attachments import get_attach_by_key

#  Homepage Request Handler Class
class AttachmentsHandler(webapp2.RequestHandler):
#    def detect_mime(self, file_name):
#        if file_name.split(".")[-1].upper() == 'PNG': return 'image/png'
#        if file_name.split(".")[-1].upper() == 'GIF': return 'image/gif'
#        if file_name.split(".")[-1].upper() == 'JPEG': return 'image/jpeg'
#        if file_name.split(".")[-1].upper() == 'JPG': return 'image/jpeg'
## grab the string from the file if possible
##        if image[1:4] == 'PNG': return 'image/png'
##        if image[0:3] == 'GIF': return 'image/gif'
##        if image[6:10] == 'JFIF': return 'image/jpeg'
#        return None
    def get(self):
        if users.is_current_user_admin():  # secure the page only admin can access
            attachment_key = self.request.query_string
            attachment = get_attach_by_key(self, attachment_key)
            mimetypes.init()
            attachment_mime = mimetypes.guess_type(attachment.file_name)
            if attachment_mime:
                self.response.headers['Content-Type'] = attachment_mime[0]
            else:
                self.response.headers['Content-Type'] = "application/octet-stream"
            self.response.out.write(attachment.file_blob)
        else:
            self.abort(401)

#from GAE - mail.py http://code.google.com/p/googleappengine/source/browse/trunk/python/google/appengine/api/mail.py?r=245
#EXTENSION_MIME_MAP = {
#    'aif': 'audio/x-aiff',
#    'aifc': 'audio/x-aiff',
#    'aiff': 'audio/x-aiff',
#    'asc': 'text/plain',
#    'au': 'audio/basic',
#    'avi': 'video/x-msvideo',
#    'bmp': 'image/x-ms-bmp',
#    'css': 'text/css',
#    'csv': 'text/csv',
#    'doc': 'application/msword',
#    'docx': 'application/msword',
#    'diff': 'text/plain',
#    'flac': 'audio/flac',
#    'gif': 'image/gif',
#    'gzip': 'application/x-gzip',
#    'htm': 'text/html',
#    'html': 'text/html',
#    'ics': 'text/calendar',
#    'jpe': 'image/jpeg',
#    'jpeg': 'image/jpeg',
#    'jpg': 'image/jpeg',
#    'kml': 'application/vnd.google-earth.kml+xml',
#    'kmz': 'application/vnd.google-earth.kmz',
#    'm4a': 'audio/mp4',
#    'mid': 'audio/mid',
#    'mov': 'video/quicktime',
#    'mp3': 'audio/mpeg',
#    'mp4': 'video/mp4',
#    'mpe': 'video/mpeg',
#    'mpeg': 'video/mpeg',
#    'mpg': 'video/mpeg',
#    'odp': 'application/vnd.oasis.opendocument.presentation',
#    'ods': 'application/vnd.oasis.opendocument.spreadsheet',
#    'odt': 'application/vnd.oasis.opendocument.text',
#    'oga': 'audio/ogg',
#    'ogg': 'audio/ogg',
#    'ogv': 'video/ogg',
#    'pdf': 'application/pdf',
#    'png': 'image/png',
#    'pot': 'text/plain',
#    'pps': 'application/vnd.ms-powerpoint',
#    'ppt': 'application/vnd.ms-powerpoint',
#    'pptx': 'application/vnd.ms-powerpoint',
#    'qt': 'video/quicktime',
#    'rmi': 'audio/mid',
#    'rss': 'text/rss+xml',
#    'snd': 'audio/basic',
#    'sxc': 'application/vnd.sun.xml.calc',
#    'sxw': 'application/vnd.sun.xml.writer',
#    'text': 'text/plain',
#    'tif': 'image/tiff',
#    'tiff': 'image/tiff',
#    'txt': 'text/plain',
#    'vcf': 'text/directory',
#    'wav': 'audio/x-wav',
#    'wbmp': 'image/vnd.wap.wbmp',
#    'webm': 'video/webm',
#    'webp': 'image/webp',
#    'xls': 'application/vnd.ms-excel',
#    'xlsx': 'application/vnd.ms-excel',
#    'zip': 'application/zip'
#    }

#  mime_type = EXTENSION_MIME_MAP.get(extension, None)
#  if mime_type is None:
#    mime_type = 'application/octet-stream'
#  return mime_type
