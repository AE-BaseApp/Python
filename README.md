[AE-Python](http://ae-python.appspot.com) - Python / webapp2 / Google App Engine Base App
==============================================

AE Python BaseApp
---------------

[AE-BaseApp](http://AE-BaseApp.appspot.com) is a multi-platform app-engine base-app created by 
[Mark Finch](http://markfinch.info) to assist developers looking to build their first applications 
leveraging [Google's Cloud Infrastructure](http://developers.google.com/appengine/). AE-Python is loosely based 
on the video from [Brett Slatkin](http://www.google.com/profiles/bslatkin) introducing Google App Engine at 
[Google IO 2008](http://sites.google.com/site/io/).

The AE-Python version of AE-BaseApp uses the Python Language along with 
the webapp2 Framework to provide a simple application base to launch new Google
App Engine Applications from.

Features of version 4 include ad provider integration, examples of how to 
use basic templates, access the datastore to create and read, user 
authentication & registration.

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
  * Version 3
    * Date/Time Conversion from UTC
    * User Profile Time Zone Picker
    * Admin Default Time Zone Selector
    * Store User IP from Headers
    * Email Account Validation
    * Strip Shouts to remove formating and scripts
    * Error Pages (eg 404...)
  * Version 4
    * db.Model Upgrades
    * Transition to MVC Design Pattern
    * Swapped PYTZ for GAEPYTZ
    * Add Internal Validation and Error Handling (In Progress)

Project Road Map:
-----------------
  * Version 4
    * Add Shout update and delete functionality
    * JavaScript form validation
    * Page Security
    * Application Logging
  * Version 5
    * Shout Navigation
    * Add OpenID URL based Authentication
    * Add OAuth
    * Add Facebook Connect 
    * Add Avatars
  * Planned Features
    * Add Docstrings to source files (PEP 257)
    * Update model to key based
    * Setup Memcahce
    * Add MarkDown or similar functionality
    * Cron job for cleaning profiles and validate data
    * Email Validation Manual Entery Form 
    * Enable User Update and Delete Functionality
    * Search (by user, by content, by date)
    * Robust Admin Module
    * Geo Location
    * Add From Location
    * Add MiniMap popout
    * Integrate with Twitter / Facebook / ...
    * Rails style Flash Notice / Warning
    * Many many more!!!

Application Stack:
------------------
  * Google App Engine Python
  * Google webapp2 Framework
  * Django Forms
  * Blueprint CSS Framework
  * PyTZ Time Zone Framework


Issues:
-------
  * THIS APP IS NOT PRODUCTION READY!!!
  * Read the file ISSUES to see a list of known issues and resolutions.

No Warranties:
--------------
There are no warranties expressed or implied.  Use at your own RISK!

Setup:
------
  * Edit the app.yaml file to change the application name.
  * Run the dev server.
  * You will be greeted with a 500 Error, go to the `/login` page and login/create an admin user.
  * Visit `/admin` page to setup the default environment variables.
  * Go back to the home page and double check everything is working.
  * Hack away, but remember you break it you bought it!  *wink* [1][1]

License:
--------
AE-Python BaseApp source code is licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0).  

Please check the file LICENSE to see other licenses that impact this project.

Notes:
------
*  [1] The corollary is you got what you paid for!
