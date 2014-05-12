Shows the use of django and python-social-auth on Google App Engine,
using django-nonrel to use the google datastore as a backend (instead
of google cloud SQL).

This example was built based on the django-nonrel testapp
* https://github.com/django-nonrel/django-testapp

Installation:

* run
	git submodule update --init --recursive
  if you haven't, to get the libraries
* install google app engine SDK and its dependencies
* run manage.py deploy

cd django-social-login
vi app.yaml # change app id
./manage.py deploy
open http://django-social-login.appspot.com

