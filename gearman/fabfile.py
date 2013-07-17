# -*- coding: utf-8 -*-

# http://docs.fabfile.org/en/1.5/tutorial.html

from fabric.api import *

project = "gearman"

# the user to use for the remote commands
env.user = ''
# the servers where the commands are executed
env.hosts = ['']

def apt_get(*packages):
    sudo('apt-get -y --no-upgrade install %s' % ' '.join(packages), shell=False)


def setup():
    apt_get("libboost-program-options-dev uuid-dev libevent-dev build-essential g++ libcloog-ppl0")
    with cd ("/usr/local/lib"):
        sudo("wget http://launchpad.net/gearmand/1.0/0.23/+download/gearmand-0.23.tar.gz")
    sudo("tar -xvzf gearmand-0.23.tar.gz")
    with cd("gearmand-0.23"):
        sudo("./configure && sudo make && sudo make install")
    sudo("ldconfig")
    sudo("gearmand -d -u root")

 
def setup_admin():
    apt_get("apache2 php5 php-pear libapache2-mod-php5 git")
    try:
        sudo("pear install Net_Gearman-0.2.3")
    except:
        print "cannot install pear or it is already installed "
    with cd("/var/www/"):
        sudo("git clone https://github.com/yugene/Gearman-Monitor.git")
