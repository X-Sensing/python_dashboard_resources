## EC2 set

EC2 is the standard cloud computer in Amazon Web Services (AWS). 

- It can be thought of as a fully contained remote computer. 

- It can be accessed in a similar way to any linux server via ssh. 

- during setup you are given the option to generate a key pair, use and existing one or 
provide one. This is used for secure login. Password an 2-factor can be added if needed.

Several versions of Linux are available (** The instructions in this doc are for default AWS 
instance**) and there would be some minor syntax changes for Ubuntu etc. Windows EC2 are 
available but approximately double the cost.

_ EC2 are compute elements and not designed for displaying GUI or graphics. In 
general there are two options:

1) make all your code locally and move across when ready for deploying

2) port map between your machine and the EC2 so you can code locally using jupyter or an 
IDE but the project is synced to the EC2. In this case the python kernal will generally be on
the EC2 as will the data. This can be a necessity if the data-set must be stored in the cloud.

** I will make a separate document on connection and port forwarding for terminal users, with 
some handy workflow hints **
 
 ### Creating an EC2 in the Amazon console
 
 - **details to add**
 
 
 ### Some setup hints
 
 I usually install some basic software straight away. Most notably Anaconda Python 
 but also some other basic software. ** After ssh-ing into the terminal:**
 
- sudo yum update -y 
 
**Anaconda Python Install Anaconda**

<ol>
<li> get the link to the latest version of Anaconda: https://www.anaconda.com/download/#linux
<li> right click the 'x86 link 64 bit link' and copy link location
<li> in the ec2 terminal "wget [and paste link]"
<li> this should look like this but the latest version: wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
<li> This will download the install script which just needs to be run to install
<li> e.g.: bash /bin/sh Anaconda3-XXXXXXXXX-Linux-x86_64.sh
</ol>


A few other installs I copy and paste in:

sudo yum install emacs
sudo yum install xorg-x11-xauth.x86_64 xorg-x11-server-utils.x86_64 dbus-x11.x86_64
sudo yum-config-manager --enable epe



  
 
 