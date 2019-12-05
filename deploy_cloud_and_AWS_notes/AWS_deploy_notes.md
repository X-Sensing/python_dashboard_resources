# EC2 set up

## General overview

EC2 is the standard cloud computer on Amazon Web Services (AWS). 

- It can be thought of as a fully contained remote computer. 

- It can be accessed in a similar way to any linux server via ssh. 

- during setup you are given the option to generate a key pair, use and existing one or 
provide one. This is used for secure login. Password an 2-factor can be added if needed.

Several versions of Linux are available (**The instructions in this doc are for default AWS 
instance**) and there would be some minor syntax changes for Ubuntu etc. Windows EC2 are 
available but approximately double the cost.

EC2 are compute elements and not designed for displaying GUI or graphics. In 
general there are two options:

1) make all your code locally and move across when ready for deploying

2) port map between your machine and the EC2 so you can code locally using jupyter or an 
IDE but the project is synced to the EC2. In this case the python kernal will generally be on
the EC2 as will the data. This can be a necessity if the data-set must be stored in the cloud.

**I will make a separate document on connection and port forwarding for terminal users, with 
some handy workflow hints**
 
 
 ## Creating an EC2 in the Amazon console
 
 In the main AWS console:
 
 - select Launch Instance button
 
 - Select your instance type (I use the default Amazon Linux 2 AMI)
 
 - Select the computer size. Be aware of th costs involved! 
 
 **>> Next: configure instance details**
 
 - The next page should be left as the default unless you know what 
 you are doing 
 
 **>> Next: Add Storage**
 
 - Storage cost charged while the instance exists (whether on or off). So it should be 
 chosen conservatively. It can be easily increased at any time. 
 
 **>> Next: Add Tags**
 
 - Tags are key-value pairs used as basic meta data and searching. 
 They are optional and can be added if desired. 
 
 **>> Next: Add Security**
 
 - Security groups allow passage or access to the EC2 from selected ports over selected 
 IP ranges. In general you will need to open the ssh port (22) over some range 
 (0.0.0.0/0 would allow connection from anywhere). For a dashboard the http, https 
 protocols will need to be open. If security is an issue than these 
 should be used as appropriate. 
 
 **>> Next: Review and Launch**
 
 - Check and **Launch**
 
 At this point you will be prompted to: use-an-existing-key-pair, create-new-key-pair. There is also
 an option to proceed with None. **you should use a key-pair**
 
 
 
 ## Adding an elastic (static/unchanging) IP
 
 A static IP is preferable for an EC2 running webapps or for simplifying  
 ssh login. Without a fixing elastic IP to your EC2 the IP address will change 
 each time you turn the instance off and on. 
 
 
From the main EC2 dashboard menu: 

- Action Menu >> Manage IP >> Allocate an Elastic IP
- On the new screen select: Allocate
- This makes a new Static (Elastic) IP address
- Action Menu >> Associate Elastic IP >> From the Pulldown menu select the appropriate EC2 >> Select Associate 

The EC2 now has an IP address that will not change.


 
 ### Some setup hints for Linux EC2
 
 I usually install some basic software straight away. Most notably Anaconda Python 
 but also some other basic software. **After ssh-ing into the terminal:**
 
 ```
sudo yum update -y 
```

**Anaconda Python Install Anaconda**

<ul>
<li> get the link to the latest version of Anaconda: https://www.anaconda.com/download/#linux
<li> right click the 'x86 link 64 bit link' and copy link location
<li> in the ec2 terminal "wget [and paste link]"
<li> this should look like this but the latest version: 
wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
<li> This will download the install script which just needs to be run to install
<li> e.g.: bash /bin/sh Anaconda3-XXXXXXXXX-Linux-x86_64.sh
</ul>


A few other installs I copy and paste in:

```
sudo yum install emacs

sudo yum install xorg-x11-xauth.x86_64 xorg-x11-server-utils.x86_64 dbus-x11.x86_64

sudo yum-config-manager --enable epe
```

# NGINX and Route 53:  serving multiple apps and (optionally) assigning personal URls


### (Optional) Route 53 Buying a personal Domain (if you don't have one)

- Go to the Route 53 (service pull down)

- You can buy a new domain from the menu. It will then be list in the Hosted Zone Menu 




### (Optional) Creating sub-domain names and assigning them to the EC2
  
To create a sub-domain from the Hosted Zone

- Select the domain

- Create record Set

- In the top of the right hand panel input the new sub-domain name you want

Then assign the URL to the appropriate EC2 by either:

<ol>
<li> leave type=A - IPv4 address and in the value box enter the IP of the EC2
<li> change type=CNAME and use the CNAME of the EC2
</ol>

## NGINX setup


The mapping of the port to the appropriate URL can be done via a configuration file: This can be done in the
file: /etc/nginx/conf.d/virtual.conf 

check if the file /etc/nginx/conf.d/virtual.conf exists and if it does not exist create it:

sudo touch /etc/nginx/conf.d/virtual.conf

An example config file is below: 

```
#
# A virtual host using mix of IP-, name-, and port-based configuration
#

#server {
#    listen       8000;
#    listen       somename:8080;
#    server_name  somename  alias  another.alias;

#    location / {
#        root   html;
#        index  index.html index.htm;
#    }
#}

server {
       listen 80;
       server_name zombie_king.utscicdata.io;
       location / {
       proxy_pass http://127.0.0.1:8000;
       }
}

server {
       listen 80;
       server_name xsensing_intermediate_1.utscicdata.io;
       location / {
       proxy_pass http://127.0.0.1:8001;
       }
}

```

This would serve an app at: 

    zombie_king.utscicdata.io 
    
which needed to be run on port 8000: For example an Plotly Dash app with the following app.run_server() command:

```
app.run_server(host='0.0.0.0', port=8000)
```

Another app would be served at: 
    server_name xsensing_intermediate_1.utscicdata.io 

that was run on port 8001 e.g. a Plotly Dash app run with:

```
app.run_server(host='0.0.0.0', port=8001)
```

# Deploy: screen and run 

To run the web apps without them terminating when we log out. The python code can be run in 
background using "screen". The -S option names the screen which can be used to identify it later if many are running.


- Make sure the python code has the appropriate port in app.run_server command. Should match the one given in the
NGINX virtual.conf file, e.g. the following line would use port: 8000:

```
app.run_server(host='0.0.0.0', port=8000)
```

From the linux command line start the screen:


```
screen -S sensible_name
```


then run the app code: 

```
python app_file_name.py
```

and close the terminal i.e. press the GUI "x" in the top corner


