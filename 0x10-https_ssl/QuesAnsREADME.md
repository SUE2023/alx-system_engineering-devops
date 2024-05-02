0x10. HTTPS SSL
DevOpsSysAdminSecurity
Concepts
For this project, we expect you to look at these concepts:
•	DNS (check on the last pages)
•	Web stack debugging (chek on last pages)

Background Context
What happens when you don’t secure your website traffic?
 
Resources
Read or watch:
•	What is HTTPS?  : https://www.instantssl.com/http-vs-https 
•	What are the 2 main elements that SSL is providing : https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html 
•	HAProxy SSL termination on Ubuntu16.04 : https://docs.ionos.com/cloud 
•	SSL termination : https://en.wikipedia.org/wiki/TLS_termination_proxy 
•	Bash function : https://tldp.org/LDP/abs/html/complexfunct.html 
man or help:
•	awk
•	dig
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General
•	What is HTTPS SSL 2 main roles
•	What is the purpose encrypting traffic
•	What SSL termination means
Requirements
General
•	Allowed editors: vi, vim, emacs
•	All your files will be interpreted on Ubuntu 16.04 LTS
•	All your files should end with a new line
•	A README.md file, at the root of the folder of the project, is mandatory
•	All your Bash script files must be executable
•	Your Bash script must pass Shellcheck (version 0.3.7) without any error
•	The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
•	The second line of all your Bash scripts should be a comment explaining what is the script doing
Quiz questions

Your servers
Name	Username	IP	State	
450205-web-01	ubuntu	34.207.212.225	running	Actions Toggle Dropdown
450205-web-02	ubuntu	54.175.254.141	running	Actions Toggle Dropdown
450205-lb-01	ubuntu	54.197.127.220	running	Actions Toggle Dropdown
Tasks
0. World wide web
mandatory
Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.
Requirements:
•	Add the subdomain www to your domain, point it to your lb-01 IP (your domain name might be configured with default subdomains, feel free to remove them)
•	Add the subdomain lb-01 to your domain, point it to your lb-01 IP
•	Add the subdomain web-01 to your domain, point it to your web-01 IP
•	Add the subdomain web-02 to your domain, point it to your web-02 IP
•	Your Bash script must accept 2 arguments:
1.	domain:
	type: string
	what: domain name to audit
	mandatory: yes
2.	subdomain:
	type: string
	what: specific subdomain to audit
	mandatory: no
•	Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
•	When only the parameter domain is provided, display information for its subdomains www, lb-01, web-01 and web-02 - in this specific order
•	When passing domain and subdomain parameters, display information for the specified subdomain
•	Ignore shellcheck case SC2086
•	Must use:
o	awk
o	at least one Bash function
•	You do not need to handle edge cases such as:
o	Empty parameters
o	Nonexistent domain names
o	Nonexistent subdomains
Example:
sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
Repo:
•	GitHub repository: alx-system_engineering-devops
•	Directory: 0x10-https_ssl
•	File: 0-world_wide_web
 Done? Get a sandbox
1. HAproxy SSL termination
mandatory
“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.
Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..
Requirements:
•	HAproxy must be listening on port TCP 443
•	HAproxy must be accepting SSL traffic
•	HAproxy must serve encrypted traffic that will return the / of your web server
•	When querying the root of your domain name, the page returned must contain Holberton School
•	Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
The file 1-haproxy_ssl_termination must be your HAproxy configuration file
Make sure to install HAproxy 1.5 or higher, SSL termination is not available before v1.5.
Example:
sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
Repo:
•	GitHub repository: alx-system_engineering-devops
•	Directory: 0x10-https_ssl
•	File: 1-haproxy_ssl_termination
 Done? Get a sandbox
2. No loophole in your website traffic
#advanced
A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.
Requirements:
•	This should be transparent to the user
•	HAproxy should return a 301
•	HAproxy should redirect HTTP traffic to HTTPS
•	Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
The file 100-redirect_http_to_https must be your HAproxy configuration file
Example:
sylvain@ubuntu$ curl -sIL http://www.holberton.online
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://www.holberton.online/
Connection: close

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 02:19:18 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$
Repo:
•	GitHub repository: alx-system_engineering-devops
•	Directory: 0x10-https_ssl
•	File: 100-redirect_http_to_https
 Done? Get a sandbox






CONCEPTS
DNS
Basics
DNS is, in simple words, the technology that translates human-adapted, text-based domain names to machine-adapted, numerical-based IP:
•	Learn everything about DNS in cartoon : https://howdns.works/ 
•	Be sure to know the main DNS record types:
o	A : https://support.dnsimple.com/articles/a-record/ Managing A records: https://support.dnsimple.com/articles/manage-a-record/ (Adding, updating, removing
o	CNAME : https://en.wikipedia.org/wiki/CNAME_record 
o	MX : https://en.wikipedia.org/wiki/MX_record 
o	TXT: https://en.wikipedia.org/wiki/TXT_record 
Advanced
•	Use DNS to scale with round-robin DNS: https://www.dnsknowledge.com/whatis/round-robin-dns/ 
•	What’s an NS Record?: https://support.dnsimple.com/articles/ns-record/ 
•	What’s an SOA Record? https://support.dnsimple.com/articles/soa-record/ 
The root domain and sub domain - differences
A root domain is the parent domain to a sub domain, and its name is not, and can not be divided by a dot.
While creating any domain at a website of domain provider, the provider system will always ask you to choose a domain name without a dot in the name. In other words, the address of the root domain may be mydomain.com but it can never be my.domain.com. Domain providers block the ability to create such a root domain until you type a name without the dot. Why?
The dot in the domain name delimits the sub domain name (the part of the name before the dot, eg. www.my.) and the root domain name ( the part after the dot, ie .domain.com). This means that the address my.domain.com is a sub domain of the root domain, whose name is domain.com
In an administrator panel at domain provider account, you can create any number of sub domains. This means that for the root domain called domain.com it is possible to create different sub domains eg. my.domain.com, your.domain.com, school.domain.com… Creating multiple sub domains is always free and does not require you to set up new accounts on a domain provider website.
As you can see, all of the domain addresses used as an example (above) do not start with the www prefix. www is also a sub domain. The www prefix always leads to the main domain. See: What’s the point in having www in a url?
The root domain and sub domain - differences
A root domain is the parent domain to a sub domain, and its name is not, and can not be divided by a dot.
While creating any domain at a website of domain provider, the provider system will always ask you to choose a domain name without a dot in the name. In other words, the address of the root domain may be mydomain.com but it can never be my.domain.com. Domain providers block the ability to create such a root domain until you type a name without the dot. Why?
The dot in the domain name delimits the sub domain name (the part of the name before the dot, eg. www.my.) and the root domain name ( the part after the dot, ie .domain.com). This means that the address my.domain.com is a sub domain of the root domain, whose name is domain.com
In an administrator panel at domain provider account, you can create any number of sub domains. This means that for the root domain called domain.com it is possible to create different sub domains eg. my.domain.com, your.domain.com, school.domain.com… Creating multiple sub domains is always free and does not require you to set up new accounts on a domain provider website.
As you can see, all of the domain addresses used as an example (above) do not start with the www prefix. www is also a sub domain. The www prefix always leads to the main domain. See: What’s the point in having www in a url?


Web stack debugging
Intro
Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions.

Non-exhaustive guide to debugging
School specific
If you are struggling to get something right that is run on the checker, like a Bash script or a piece of code, keep in mind that you can simulate the flow by starting a Docker container with the distribution that is specified in the requirements and by running your code. Check the Docker concept page for more info.
Test and verify your assumptions
The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:
•	Is the web server started? - You can check using the service manager, also double check by checking process list.
•	On what port should it listen? - Check your web server configuration
•	Is it actually listening on this port? - netstat -lpdn - run as root or sudo so that you can see the process for each listening port
•	It is listening on the correct server IP? - netstat is also your friend here
•	Is there a firewall enabled?
•	Have you looked at logs? - usually in /var/log and tail -f is your friend
•	Can I connect to the HTTP port from the location I am browsing from? - curl is your friend
There is a good chance that at this point you will already have found part of the issue.
Get a quick overview of the machine state
Youtube video First 5 Commands When I Connect on a Linux Server: https://www.youtube.com/watch?v=1_gqlbADaAw 
When you connect to a server/machine/computer/container you want to understand what’s happened recently and what’s happening now, and you can do this with 5 commands : https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/  in a minute or less:
w
•	shows server uptime : https://www.techtarget.com/whatis/definition/uptime-and-downtime  which is the time during which the server has been continuously running
•	shows which users are connected to the server
•	load average will give you a good sense of the server health - (read more about load here : https://scoutapm.com/blog/understanding-load-averages  and here: https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html )
history
•	shows which commands were previously run by the user you are currently connected to
•	you can learn a lot about what type of work was previously performed on the machine, and what could have gone wrong with it
•	where you might want to start your debugging work
top
•	shows what is currently running on this server
•	order results by CPU, memory utilization and catch the ones that are resource intensive
df
•	shows disk utilization
netstat
•	what port and IP your server is listening on
•	what processes are using sockets
•	try netstat -lpn on a Ubuntu machine
Machine
Debugging is pretty much about verifying assumptions, in a perfect world the software or system we are working on would be working perfectly, the server is in perfect shape and everybody is happy. But actually, it NEVER goes this way, things ALWAYS fail (it’s tremendous!).
For the machine level, you want to ask yourself these questions:
•	Does the server have free disk space? - df
•	Is the server able to keep up with CPU load? - w, top, ps
•	Does the server have available memory? free
•	Are the server disk(s) able to keep up with read/write IO? - htop
If the answer is no for any of these questions, then that might be the reason why things are not going as expected. There are often 3 ways of solving the issue:
•	free up resources (stop process(es) or reduce their resource consumption)
•	increase the machine resources (adding memory, CPU, disk space…)
•	distributing the resource usage to other machines
Network issue
For the machine level, you want to ask yourself these questions:
•	Does the server have the expected network interfaces and IPs up and running? ifconfig
•	Does the server listen on the sockets that it is supposed to? netstat (netstat -lpd or netstat -lpn)
•	Can you connect from the location you want to connect from, to the socket you want to connect to? telnet to the IP + PORT (telnet 8.8.8.8 80)
•	Does the server have the correct firewall rules? iptables, ufw:
o	iptables -L
o	sudo ufw status
Process issue
If a piece of Software isn’t behaving as expected, it can obviously be because of above reasons… but the good news is that there is more to look into (there is ALWAYS more to look into actually).
•	Is the software started? init, init.d:
o	service NAME_OF_THE_SERVICE status
o	/etc/init.d/NAME_OF_THE_SERVICE status
•	Is the software process running? pgrep, ps:
o	pgrep -lf NAME_OF_THE_PROCESS
o	ps auxf
•	Is there anything interesting in the logs? look for log files in /var/log/ and tail -f is your friend
Debugging is fun
Debugging can be frustrating, but it will definitely be part of your job, it requires experience and methodology to become good at it. The good news is that bugs are never going away, and the more experienced you become, trickier bugs will be assigned to you! Good luck :)

Bug #415
Bug #416
Bug #417
Bug #418
Bug #419
Bug #420





