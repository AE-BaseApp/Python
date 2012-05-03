[AE-Python](http://ae-python.appspot.com) - Python / webapp2 / Google App Engine Base App
==============================================

AE Python BaseApp
---------------

[AE-BaseApp](http://AE-BaseApp.appspot.com) is a multi-platform app-engine base-app created by 
Mark Finch to assist developers looking to build their first applications 
leveraging Google's Cloud Infrastructure. AE-Python is loosely based 
on the video from Brett Slatkin introducing Google App Engine at 
[Google IO 2008](http://sites.google.com/site/io/).

The AE-Python version of AE-BaseApp uses the Python Language along with 
the webapp2 Framework to provide a simple application base to launch new Google
App Engine Applications from.

Features of version 2 include AdSense integration, examples of how to 
use basic templates, access the datastore to create and read, user 
authentication & registration.

NOTE: Due to App Engine requirements version numbers will all be integers.

Accomplished:
-------------
  * Version 1
    * Ad-Sense Integration
    * Basic Template Usage
    * Access the Datastore to create and Read
  * Version 2
    * Updated to Python 2.7
    * Updated to Webapp2
    * Configured for High Replication Datastore
    * User Authentication
      * Google
      * OpenID
    * Basic User Registration
    * Basic Application Security
    * Basic Ad-Provider Framework
    * Basic Admin Framework
    * Basic Authentication Decorator

Project Road Map:
-----------------
  * Version 3
    * Add Date/Time Conversion from UTC
    * Email Authentication
    * Add Internal Validation and Error Handling
    * Add Safe HTML to Shouts
    * Store User IP from Headers
  * Version 4
    * db.Model Upgrades
    * Add update and delete
    * Error Pages (eg 404...)
    * JavaScript form validation
  * Version 5
    * Shout Navigation
    * Add OAuth
    * Add Facebook Connect 
    * Add Avatars
  * Planned Features
    * Robust Admin Module
    * Geo Location
    * Integrate with Twitter / Facebook / ...
    * Rails style Flash Notice / Warning
    * Many many more!!!

Application Stack:
------------------
  * Google App Engine Python
  * Google webapp2 Framework
  * Blueprint CSS Framework


Issues:
-------
  * THIS APP IS NOT PRODUCTION READY!!!
  * App currently implicitly trusts user input (a really big NO NO for Production)
  * There is no validation and error handling (Another big NO NO)
  * OpenID only supports providers that use an authentication page.  Providers
    whom use a URL for login are currently not supported.
  * Some of the code is not the best way to accomplish a task.  This is on 
    purpose as this app is also serving as an example for an online class I'm 
    creating.  Thats why there are small incremental versions.

No Warranties:
--------------
There are no warranties expressed or implied.  Use at your own RISK!

License:
--------
AE-Python BaseApp source code is licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0).  

Please check the file LICENSE to see other licenses that impact this project.

