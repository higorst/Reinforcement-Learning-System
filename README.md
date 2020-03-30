# Reinforcement-Learning-System
System for teaching Reinforcement Learning (RL)

-- install Python 3.6 on Ubuntu 12.04

To add the PPA, Open terminal and run:

    sudo add-apt-repository ppa:fkrull/deadsnakes

You may read the PPA description in the output and then:

Install Python 3.4 using the following command:

    sudo apt-get update; sudo apt-get install python3.4

To set your installed python as default, run the below commands one by one:

    rm /usr/bin/python && ln -s /usr/bin/python3.4 /usr/bin/python

Install pip

    sudo apt-get install python3-setuptools
    sudo easy_install3 pip

Install tkinter

    sudo apt-get install python3-tk

Install Pillow

    sudo pip install Pillow

------------------------------------------
sudo apt install python-pip
sudo apt install python3-pip
sudo apt-get install python3-tk
sudo apt-get install python3-pil python3-pil.imagetk
sudo pip3 install Pillow
------------------------------------------
we need C compiler and other stuff to compile Python

sudo apt-get install build-essential

SQLite libs need to be installed in order for Python to have SQLite support.

sudo apt-get install libsqlite3-dev
sudo apt-get install sqlite3 # for the command-line client
sudo apt-get install bzip2 libbz2-dev
 
Download and compile Python:

wget http://www.python.org/ftp/python/3.3.5/Python-3.3.5.tar.xz
tar xJf ./Python-3.3.5.tar.xz
cd ./Python-3.3.5
./configure --prefix=/opt/python3.3
make && sudo make install

you can install a bash alias named python3 instead:

echo 'alias python3="/opt/python3.3/bin/python3.3"' >> .bashrc