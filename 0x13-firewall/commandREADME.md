Process for Advanced task:
========================
in web-01
=>sudo vim /etc/ufw/before.rules
=>Paste:
+++++++
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
=>sudo ufw allow 8080
=>sudo service ufw restart
=>sudo ufw enable # when propted type Yes
