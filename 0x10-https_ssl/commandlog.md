SSL INSTALLATION PROCESS/certbot
===============================
sudo apt update
sudo apt install snapd
sudo apt-get remove certbot  # to confirm that certbot was not previously installed
sudo apt-get install certbot
sudo service haproxy stop  # to stop port 80 from listening
curl localhost  # to see if there is connect. There should be no any connection/connection refused
# NB: oomit this it was due to wrong action instead of picking the whole sudo I picked udo hene the propting although I installed it. Have it in proces just incase it will have an effect to help me know at what point the issued okay and trace way of correcting it# sudo apt install udo # not found hence requested to be installed before the below command# 
sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d www.techwe.tech #NB:sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d techwe.tech -d www.techwe.tech (# there was no nginx hence installed : sudo apt install nginx-full, confirmed the version: nginx -v, port 80 not accessible, sudo lsof -i :80 #to list PID on port 80, sudo systemctl stop nginx # stop the processes )
sudo ls /etc/letsencrypt/live/www.techwe.tech or #sudo ls /etc/letsencrypt/live/techwe.tech  # this is to ensure that ssl is working
sudo mkdir -p /etc/haproxy/certs #DONE DISPITE THE ABOVE 2 having issues.
DOMAIN='www.techwe.tech' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
sudo chmod -R go-rwx /etc/haproxy/certs

sudo chmod 777 /etc/haproxy/haproxy.cfg # to enable writing on the file

sudo vim  /etc/haproxy/haproxy.cfg      #edit configuration file by pasting content of 100-redirect_http_to_https
sudo service haproxy start
