{
killall screen
}

PYTHON_VIRTUAL_PATH='/home/ec2-user/virtual_environments/xsense/bin/'
DASHBOARD_ROOT_PATH='/home/ec2-user/xsense/xsense_dashboard_resources/'

DASHBOARD_NAME='intermediate_1'
cd  $DASHBOARD_ROOT_PATH/workshop_intermediate_dashboard/ ; screen -dm -S $DASHBOARD_NAME $PYTHON_VIRTUAL_PATH'python' ./$DASHBOARD_NAME.py -p 8001

DASHBOARD_NAME='intermediate_2'
cd $DASHBOARD_ROOT_PATH/workshop_intermediate_dashboard/ ; screen -dm -S $DASHBOARD_NAME  $PYTHON_VIRTUAL_PATH'python' ./$DASHBOARD_NAME.py -p 8002

DASHBOARD_NAME='xsense_current'
cd $DASHBOARD_ROOT_PATH/workshop_intermediate_dashboard/ ; screen -dm -S $DASHBOARD_NAME  $PYTHON_VIRTUAL_PATH'python' ./$DASHBOARD_NAME.py -p 8000

cd $DASHBOARD_ROOT_PATH

sudo service nginx restart

screen -ls

source $PYTHON_VIRTUAL_PATH'activate' ; pip freeze > requirements.txt ; deactivate

