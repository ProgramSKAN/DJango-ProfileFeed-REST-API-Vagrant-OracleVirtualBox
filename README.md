# Profile REST API

gitignore> https://gist.github.com/LondonAppDev/dd166e24f69db4404102161df02a63ff

License> https://choosealicense.com/licenses/mit/

# GIT Commands

> git --version
> git config --global user.email "abcd@gmail.com:
> git config --global user.name "abcd"
> git config --list

install virtual box

install vagrant

> vagrant --version
> cd ~
> ls
> pwd
> cd profiles-rest-api
> git init

restart atom

> git add .
> git commit -am "Initial Commit"

-am > all message

> ls ~/.ssh :to make sure there is no ssh keys in our directory

generate private and public key to authenticate>

> ssh-keygen -t rsa -b 4096 -C "youremail@gmail.com"

to get the public key and paste in github new ssh>

> cat ~/.ssh/id_rsa.pub

to push>

> git remote add origin https://github.com/ProgramSKAN/DJango-REST-API.git
> git push -u origin master

# Create Local Development server using vagrant

in project directory

create vagrant file> ubantu image>

> vagrant init ubantu/bionic64

configure vagrant box>
https://gist.github.com/LondonAppDev/199eef145a21587ea866b69d40d28682>
replace varant file with this

running and connecting to our dev server>

> vagrant up

since my machine is guest operating system, so counnect using ssh>
vagrant handles connection to the machine>

> vagrant ssh

now command line changes to vagrant@ubantu-bionic> so new you are in the machine

to disconnect> to get back to local machine>

> exit

vagrant@ubantu-bionic> cd /vagrant :: this will make everything in vagrant directory will synchronize everything in project folder

ex:if you run "touch test.txt" in vagrant@ubantu-bionic:/vagrant> then it will create text file in project directory

ex:if you run ls in vagrant@ubantu-bionic:/vagrant> then it will match to project directory

# every Commit

> git add .
> git commit -am "congifugured vagrant and setup hello world script"
> git push origin

# Create Python Virtual Environment

https://docs.python-guide.org/dev/virtualenvs/

create it in vagrant server home directory not in project directory, which helps in destroy and recreate vagrant server from scratch.at that time we can have a new environment.

> python -m venv ~/env

activate virtual environment

> source ~/env/bin/activate

to deactivate venv

> deactivate

https://pypi.org/search/?q=django&o=> Django latest version

install requirements.txt

> (env) vagrant@ubuntu-bionic:/vagrant\$ pip install -r requirements.txt

# Create new DJango Project & App

. > dot specifies location to create this project

> (env) vagrant@ubuntu-bionic:/vagrant$ django-admin.py startproject profiles_project .
>(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py startapp profiles_api

# Test and commit changes

start running development web server. 0.0.0.0>make it available in all networks that is on app development server.8000>start it in port 8000(which is specified in vagrantfile, we mapped prot 8000 for host machine to port 8000 for development machine.so 8000 is used here to start server)

> python manage.py runserver 0.0.0.0:8000

check in browser

> http://localhost:8000/ or http://17.0.0.1:8000/

to stop server

> ctrl+c

# migrations

> python manage.py makemigrations profiles_api
> python manage.py migrate

# create superuser

python manage.py createsuperuser

###### test django admin 

http://localhost:8000/admin
http://localhost:8000/api/hello-view  >get api view