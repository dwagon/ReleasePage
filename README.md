# ReleasePage
Create a simple and configurable website showing release versions of various software

This is for when you keep getting asked what version of your application / whatever is installed on which environment.

For each thing that you want to track create a python script in the samplers directory.

It should expose an attribute called 'application' which is the name of the application.

It should also expose a method called getDetails() which should return a list of dictionaries.
The keys of note are:
 * env - environment
 * release - the release number or name for the application in the environment
 * notes - Any random text (optional)
 * url - A url to somewhere relevant and interesting (optional)
