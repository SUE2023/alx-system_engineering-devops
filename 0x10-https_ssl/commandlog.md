SSL INSTALLATION PROCESS/certbot
sudo apt update
sudo apt install snapd
sudo apt-get remove certbot
sudo apt-get install certbot
sudo service haproxy stop  # to stop port 80 from listening
curl localhost  # to see if there is connect. There should be any connection
sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -dtechwe.tech -d www.techwe.tech
sudo ls /etc/letsencrypt/live/techwe.tech
sudo mkdir -p /etc/haproxy/certs
DOMAIN='www.techwe.tech' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
sudo chmod -R go-rwx /etc/haproxy/certs
sudo vim  /etc/haproxy/haproxy.cfg      #edit configuration file by pasting content of 100-redirect_http_to_https
sudo service haproxy star
