sudo systemctl stop cicd
cd /home/ubuntu/cicd_practice3/ && git pull origin master
sudo systemctl start cicd
