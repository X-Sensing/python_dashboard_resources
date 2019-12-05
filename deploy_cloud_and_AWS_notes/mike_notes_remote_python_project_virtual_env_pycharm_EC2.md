# Notes on new Python Project Setup

## ON EC2

- [if it does not yet exist] make a directory virtual_environments in the home directory of the EC2
- [if not yet done] pip install virtualenv

for each project make a new virutal environment:
```
cd /home/ec2-user/virtual_environments

virtualenv -p $(which python3) [the_project_name_or_similar]

```


also make a project directory that the project will map to:

```
cd 

mkdir [the_project_name_or_similar]
```

## IN PYCHARM

- \> preferences \> project_interpreter \> click the settings wheel and select "add" 
- select ssh intepreter and fill out details for the host and username, e.g:
```
host = the EC2 IP 

user = 'ec2-user'
```
- \> Next
- give the path to the virtualenv execuatable e.g:
 ```
/home/ec2-user/virtual_environments/[project_venv_name]/bin/python
```
- edit name and append easy to understand project name to virtual_env name
- Apply and return to pycharm open screen

## Now in pycharm open screen create a new project
- creat new project
- Emter the project name
- click the project intepreter tab
- select existing intepreter
- click the 3 dots and select ssh interpreter
- select the virtual_envrionment added above remote virtual env 

### Go to deployment tab in Pycharm
Note we only want one top level deployment setup per EC2. So either create by adding EC2 IP etc 
or select previously created deployment for that EC2
- hit auto dectect root path (should be /home/ec2-user)
- go to mappings tab
- add the project path (relative from root). e.g. /[project_directory_name]
- check deployment options but defaults should be ok

### (Optionally) Make some project directories that don't map and update between local and remote:
- on deployment go to excluded_paths tab (SAFEST TO USE CLICK-THROUGH DIRECTORY MENU)
- make a directory on the local machine "local_only"
- likewiase make a directory on the EC2 "remote_only"
- add Add deployment paths at top level of project:
- relative_path/remote_only
- Add local paths and exclude  /full_local_path/local_only
- Make these directories on the remote and local machine respectively (this is done first)



