#!/usr/bin/env python
# coding: utf-8

# <h2>Deploying Dash application using  [Heroku](https://dashboard.heroku.com/apps)</h2>

# Heroku was one of the first platform as a service providers. It started as a hosting option for Ruby based applications, but then grew to support many other languages like Java, Node.js and our favorite, Python.
# 
# In essence, deploying a web application to Heroku requires just uploading the application using git. Heroku looks for a file called Procfile in the application's root directory for instructions on how to execute the application. For Python projects Heroku also expects a requirements.txt file that lists all the module dependencies that need to be installed.

# <p><strong><!-- react-text: 4442 -->Step 1. Create an account in [Github](http://www.github.com)<!-- /react-text --></strong></p>
# 
# <a href="https://github.com/join"  class="btn btn-sm btn-primary" data-ga-click="Dashboard, click, Sidebar header new repo button - context:user">Sign up for GitHub</a>
# 
# 
# <p><strong> Step 2. Create a new Repository in </strong></p>
# 
# <a href="http://www.github.com/new" class="btn btn-sm btn-primary" data-ga-click="Dashboard, click, Sidebar header new repo button - context:user">New repository</a>
# 
# * call it `dash_app_example`
# * Check: `Initialize this repository with a README``
# * Add .gitignore: Python
# 
# <p><strong> Step 3. Clone your repository </strong></p>
# 
# * Find this button:
# 
# <details class="get-repo-select-menu js-menu-container float-right position-relative dropdown-details details-reset" open="">
#   <summary class="btn btn-sm btn-primary">
#     Clone or download
#     <span class="dropdown-caret"></span>
#   </summary>
# </details>
# 
# * And select Open in Desktop. Shortly the github desktop application will be downloaded. 
# * Choose a local folder called `dash_app_example` for cloning the remote repository
# 
# 
# <p><strong>Step 4. Download your app notebook as py :</strong></p>
# 
# * Open your notebook Dash application
# * Replace `app = dash.Dash()` line with:
# ```
#     app = dash.Dash(__name__)
#     server = app.server
# ```
# * add an external css adding this line, after previous one :
# 
# ```
#     app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
# 
# ```
# * Go to File -> Download as -> Python (.py) 
# * save as `app.py` into `dash_app_example` folder
# 
# 
# 
# 
# 
# 
# 

# <strong>Step 5. Creating Heroku account</strong>
# 
# Before we can deploy to Heroku we need to have an account with them. So head over to [www.heroku.com](http://www.heroku.com) and create an account.
# Once you are logged in you have access to a dashboard, where all your apps can be managed. 
# 
# <strong>Step 6 Installing the Heroku client</strong>
# 
# Heroku offers a tool called the "Heroku client" that we'll use to create and manage our application. This tool is available for Windows, Mac OS X and Linux. If there is a [Heroku toolbelt](https://toolbelt.heroku.com/) download for your platform then that's the easiest way to get the Heroku client tool installed.
# 
# The first thing we should do with the client tool is to login to our account:
# 
#     $ heroku login
# 
# 
# 

# <strong>Step 7 Creating a Heroku app</strong>
# 
# To create a new Heroku app you just use the create command from the root directory of the application:
# 
# > $ heroku apps:create dask-app-example
# 
# Or clicking the **NEW** button in Heroku web application
# 
# Of course the name dask-app-example is now taken, so make sure you use a different app name.

# <strong>Step 8. Creating the requirements.txt file</strong>
# 
# * create a requirements.txt with all pyhon packages dependences:
# 
# ```
# plotly==2.2.1
# dash==0.19.0
# dash-core-components==0.14.0
# dash-html-components==0.8.0
# dash-renderer==0.11.1
# dash.ly==0.17.3
# pandas==0.19.1
# gunicorn==19.6.0
# ```
# 
# Heroku does not provide a web server. Instead, it expects the application to start its own server on the port number given in environment variable $PORT.
# 
# We know the Flask web server is not good for production use because it is single process and single threaded, so we need a better server. The Heroku tutorial for Python suggests `gunicorn`, a pre-fork style web server written in Python, so that's the one we'll use.
# 
# The `gunicorn` web server needs to be added to the `requirements.txt` inside the app directory
# 
# 

# <strong>Step 9. Creating Procfile file</strong>
# 
# The last requirement is to tell Heroku how to run the application. For this Heroku requires a file called `Procfile` in the root folder of the application.
# 
# This file is extremely simple, it just defines process names and the commands associated with them (file `Procfile`):
# 
#     web: gunicorn app:server
# 
# (Note that app refers to the filename app.py. server refers to the variable server inside that file. The web label is associated with the web server. Heroku expects this task and will use it to start our application.)
# 

#     
# <p><strong>Step 10. Push changes to remote repository:</strong></p>
# 
# Go to Github Desktop and commit and push the new python file:
# * Add a Summary (a message telling what modifications you did to your code)
# * Click the commit to master button
# * Click on the push origin tab 

# <p><strong>Step 11. Deploying the application:</strong></p>
# 
# And now, we push the application to our Heroku hosting account. It can be done using the heroku web application:
# *  Go to the deployment panel (up arrow) 
# * Scroll down until you find "Deployment method" and select GITHUB
# * Find your repo and connect it
# * Pick the master branch and deploy it
# 
# 
# If the process worked well, now the application is online: 
# 
#     Your app was successfully deployed.
# 
# [https://dask-app-example.herokuapp.com/](https://dask-app-example.herokuapp.com/)
