Django Delegate Voting System
=============================

A barebones minimal requirements delegate voting system created as a proof of concept.

Todo
----

* Create generic views and templates to make this work in the browser.
* Wrap critical sections in a transaction
* Make a celery worker that does the resolution of votes when proposals close.

Setup
-----

1. Install homebrew, by getting the commandline tools: https://developer.apple.com/downloads and then do the install homebrew here: http://mxcl.github.com/homebrew/ (I don't think this is require but the XCode Command Line Tools are.)
2. Open Terminal.app
3. Check python is installed by typing `python`
4. Install pip if you don't have it `sudo easy_install pip`
5. Use pip to install virtualenv (don't ask me why): `sudo pip install virtualenv`
6. Find a fresh place to checkout the project: git@github.com:alper/enhydris.git use the Mac client: http://mac.github.com/
7. In the terminal `cd` to where you just checked out the project, for instance: `cd ~/Documents/projects/enhydris`
8. Create a virtual environment if you don't have one yet: `virtualenv venv --distribute`
9. Start a virtual environment: `source venv/bin/activate`
10. Install all the necessary packages: `pip install -r requirements.txt`
11. If you have never done so, setup the database: `python manage.py syncdb`, follow the instructions you get and note down the username and password that give you /admin access to the django site	
12. Because we use *south* to create the tables for the application (and to update after model changes) you need to run: `python manage.py migrate`
13. Start the server with `python manage.py runserver` and go to your django at http://127.0.0.1:8000/admin
14. Run the nose test by typing: python manage.py test --nologcapture

To restart the server simply repeat steps 9 and 13.
To be up to date again always do: 9, 10, 12, 13.