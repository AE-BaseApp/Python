[GAE-Py](http://gae-py.appspot.com) - Python / webapp / Google App Engine Base App
==============================================

GAE-Py Base-App
---------------

[Project-GAE](http://project-gae.appspot.com) is a multi-platform app-engine base-app created by 
Mark Finch to assist developers looking to build their first applications 
leveraging Google's Cloud Infrastructure. GAE-Py is loosely based 
on the video from Brett Slatkin introducing Google App Engine at 
[Google IO 2008](http://sites.google.com/site/io/).

The GAE-Py version of Project-GAE uses the Python Language along with 
Google's webapp Framework to provide a simple application base to launch
new Google App Engine Applications from.  

Features of version 1 include Ad-Sense integration, examples of how to 
use basic templates, access the datastore to create and read.  Another 
goal of version 1 is to have a very simple application to benchmark 
various frameworks running on App Engine.  The reason to keep it simple 
is to see how much a performance hit a framework has on App-Engine.
GAE-Py being the lightest of the base apps will likely perform the 
fastest.  That is the question we hope is answered with version 1 of
Project-GAE.

NOTE: Due to App Engine requirements version numbers will all be integers.

Goals:
------
  * Version 2
    * Add update and delete
    * Add registration
    * Add authentication and application security
  * Planned Features
    * Add Date/Time Conversion from UTC
    * Add Gravatars
    * Add Validation and Error Handling
    * Error Pages (404...)
    * Add Safe HTML to Shouts
    * Integrate with Twitter / Facebook / MySpace / ...
    * Many many more!!!

Application Stack:
------------------
  * Google App Engine Python
  * Google webapp Framework
  * Blueprint CSS Framework


Issues:
-------
  * THIS APP IS NOT PRODUCTION READY!!!
  * App currently implicitly trusts user input (a really big NO NO for Production)
  * There is no validation and error handling
  * No Authentication

No Warranties:
-------------
There are no warranties expressed or implied.  Use at your own RISK!

License:
--------
GAE-Py Base-App source code is licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0).  

Please check the file LICENSE to see other licenses that impact this project.

