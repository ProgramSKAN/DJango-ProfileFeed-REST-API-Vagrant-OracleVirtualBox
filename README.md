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

> ls ~/.ssh  :to make sure there is no ssh keys in our directory

generate private and public key to authenticate>
> ssh-keygen -t rsa -b 4096 -C "youremail@gmail.com"


to get the public key and paste in github new ssh>
>cat ~/.ssh/id_rsa.pub

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

ex:if you run "touch test.txt" in vagrant@ubantu-bionic:/vagrant>   then it will create text file in project directory

ex:if you run ls in vagrant@ubantu-bionic:/vagrant>   then it will match to project directory
