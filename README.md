# python_dashboard_resources

This repo is a place to store some info, notebooks and code samples for the X-sensing workshop Python Plotly dashboard building demo. 

### Directory contents overview

<ul>
  <li> **notebooks**  will hold jupyter notebooks for demonstrating or implementing various parts of the process
  <li> **xsense_dashboard**  will stores the full version of the dashboard app
  <li> **intermediate_dashboards**  will store a set of sub-directories which conatin the dashboard code at intermediate stages
</ul> 

### Purpose of the demo workshop 

The goal for this demo is not aesthetic visualizations or professional level web-apps but to serve as an example of an all in one solution for serving simple interactive dashboards at a level that would be useful for scientific teams or internal analytics and data sharing. 

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

http://xsensing_final.utscicdata.io

The username and password will be given to access this.

Some intermediate versions for demonstration will also be run at the following URLs:

http://xsensing_intermediate_1.utscicdata.io

http://xsensing_intermediate_2.utscicdata.io

http://xsensing_intermediate_3.utscicdata.io




