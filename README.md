# python_dashboard_resources

This repo is a place to store some info, notebooks and code samples for the X-sensing workshop Python Plotly dashboard building demo. 

Note the **deploy_cloud_and_AWS** directory for more detailed notes on parts of the process 
such as AWS deployment, EC2 and NGINX setup etc

##  Directory Contents Overview

**data** place holder directory with relative path required by the apps

**deploy_cloud_and_AWS** More detailed notes on parts of the process such as AWS deployment and Python setup

**notebooks** The notebooks from the workshop but without the stop points that should execute through

**notebooks_with_workshop_stop_points** The workshop notebooks

**workshop_intermediate_dashboard** The python code for each stage of the dashboard

**xsense_app** This will update as the "stats by eye" app is finished off





### Purpose of the demo workshop 

The goal for this demo is not to make  professional level web-apps but to serve as an example of an all in one solution for serving simple interactive dashboards at a level 
that would be useful for scientific teams or internal analytics and data sharing. 

In this context these are the advantages:

<ul>
<li> The entire app can be created in a single python program which handles the construction of webpage, the interactive visualizations and the widget and components to control them.
<li> It only uses free open-source resources. Python, Plotly Charts, Plotly Dash, Flask and deployed on a linux machine.
<li> Once some personal styles are chosen and the basic ideas understood, there are sufficient examples and libraries available that it is reasonable to take a personal "grey box approach" and requires only small amount of web-languages such as HTML and CSS.
<li> It is native to the more powerful data-science, data-manipulation. statistical and mathematical modelling languages. i.e. python (and an R version). And so seamless integrates with modelling and analytics projects.
</ul>

### The demo project will be outlined in a series of Jupyter notebooks where code can be run interactively. Hopefully we will be able to through the following steps:

<ol>
<li> setup the installation of the required python packages and a demo of the mechanics of running an app
<li> outline of a simple project. 
<li> The creation and formatting of the required data using common python models: pandas and scipy.stats
<li> The construction of a python function of an interactive Plotly chart that will be required for the app
<li> Look over the structure of how Dash lays out the webpage and incorporates interactive components
<li> Go through the processes of how the interactive components are coded to manipulate the page and graphics
<li> Run the created app in a web browser on your computer
<li> A demonstration of deployment on AWS (data-science style not developer style) 
<li> Outline somethings that have not been covered
</ol>


### A running version of the dashboard demo we are making can be found here (not currently finished):

http://xsensing_dash_demo.utscicdata.io

The username and password will be given to access this.

Some intermediate versions for demonstration will also be run at the following URLs:

http://xsensing_intermediate_1.utscicdata.io

http://xsensing_intermediate_2.utscicdata.io


# Getting started


## Quick discussion of what is most important to learn?


## Software Requirements and installation

Only requires open source software and it is valuable to have these requirements set up locally


### Requied: python, pip and jupyter-notebooks

- a local instalation in your standard working environement is best

- ssh connection to a linux server

- web based jupyter notebooks collab tools may have difficulty and are last resort


### How many people have a local instalation of this software working?


### If not then are you able to install it on your laptop?

- Anaconda is an easyway to get everything working in one go

- Anaconda can be installed for linux, mac and windows: https://www.anaconda.com/distribution/

- If you need to install  Anaconda via the command-line installation then see EC2 setup in  AWS deploy notes


## Get the project code

## You can download or clone the Repo for this this repo:

- https://github.com/X-Sensing/python_dashboard_resources

- we need to open the notebook: notebook_1_xdash_overview_and_setup.ipynb located in the notebook subdirectory.


# The Python packages for this project. They will need can be installed with the commands below 
<ul>
<li> pip install pip
<li> pip install pandas
<li> pip install numpy
<li> pip install scipy 
<li> pip install dash
<li> pip install dash-auth
<li> pip install requests
<li> pip install matplotlib
</ul>



