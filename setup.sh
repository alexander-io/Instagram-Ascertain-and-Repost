# install make utility
sudo apt install make -y

# install python dependencies
sudo apt install python3-pip -y
sudo apt install python-pip -y

# install ffmpeg dependency
sudo apt install ffmpeg -y

# mongo install and db-service start, https://docs.mongodb.com/v3.4/tutorial/install-mongodb-on-ubuntu/ :
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo service mongod start

# create post directory & map
mkdir posts/
touch post_map

# clone instagram api
git clone https://github.com/LevPasha/Instagram-API-python.git

# initialize the ig api
cd Instagram-API-python && pip install -r requirements.txt && cd ..

# python3-pip dependencies
sudo pip3 install pymongo
sudo pip3 install requests_toolbelt
sudo pip3 install moviepy
