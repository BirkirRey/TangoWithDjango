#Enable virtualenvwrapper.sh which has nice commands for virtual environments
source /Users/birey/anaconda3/bin/virtualenvwrapper.sh

#Virtual environments allows you to work on projects that might have confliciting dependancies on the same computer
#using the command: mkvirtualenv rango , a new environment is created which is stored in ~/.virtualenvironments
#You can activate the environment and install all the programs needed to run the project within the environment
#Then you simply deactivate the environment and it is as nothing had happened globally on the computer.
mkvirtualenv rango #Create the virtual environment
workon rango #Activate virtual environment rango
deactivate rango #Deactivate the environment

#To share an environment it can be smart to simply save all the packages and versions in a file that can be shared
pip freeze > requirements.txt
#Then simply send the requirements file to a collaborator who can run it locally with
pip install -r requirements.txt
#This is a simple way to share environments


#Find processes that have and open port, such as django servers
lsof -nP +c 15 | grep LISTEN
#Gives list of processes. To kill a certain process, find the PID from list and type
kill <PID>
