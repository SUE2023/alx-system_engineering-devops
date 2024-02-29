INSTRUCTION FOR THE 0x07-networking_basics PROJECT
==================================================
Resources
Read or watch:
++++++++++++++
OSI model: https://en.wikipedia.org/wiki/OSI_model
Different types of network : https://www.lifewire.com/lans-wans-and-other-area-networks-817376
LAN network : https://en.wikipedia.org/wiki/Local_area_network
WAN network : https://en.wikipedia.org/wiki/Wide_area_network
Internet : https://en.wikipedia.org/wiki/Internet
MAC address : https://whatismyipaddress.com/mac-address
What is an IP address : https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/
Private and public address: https://www.iplocation.net/public-vs-private-ip-address
IPv4 and IPv6 : https://www.webopedia.com/insights/ipv6-ipv4-difference/
Localhost : https://en.wikipedia.org/wiki/Localhost
TCP and UDP : https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/
TCP/UDP ports List : https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
What is ping /ICMP : https://en.wikipedia.org/wiki/Ping_%28networking_utility%29
Positional parameters : https://www.adminschoice.com/bash-positional-parameters
man or help:

netstat
ping

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

OSI Model
What it is
How many layers it has
How it is organized
What is a LAN
Typical usage
Typical geographical size
What is a WAN
Typical usage
Typical geographical size
What is the Internet
What is an IP address
What are the 2 types of IP address
What is localhost
What is a subnet
Why IPv6 was created
TCP/UDP
What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
What is the main difference between TCP and UDP
What is a port
Memorize SSH, HTTP and HTTPS port numbers
What tool/protocol is often used to check if a device is connected to a network
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
All your Bash script files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass shellcheck without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing
More Info
The second line of all your Bash scripts should be a comment explaining what is the script doing

For multiple choice question type tasks, just type the number of the correct answer in your answer file, add a new line for every new answer, example:

What is the most important position in a software company?

Project manager
Backend developer
System administrator
sylvain@ubuntu$ cat foo_answer_file
3
sylvain@ubuntu$

Source for question 1 here: https://twitter.com/devopsreact/status/831922429215662080

TASKS
++++
0. OSI model
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:

The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc
Keep in mind that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.
https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/4e6a0ad87a65d7054248.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240228T105546Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8afa8c653a9697326a0afe8ffb1e0155e90123af10b6dfea0c0d06ba0e674331

In this project we will mainly focus on:

The Transport layer and especially TCP/UDP
On the Network layer with IP and ICMP
The image bellow describes more concretely how you can relate to every level.

https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/0fc96bd99faa7941b18bcae4c5f90c6acd11791d.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240228T105546Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f67790fcc233102d3cc624594b8cbeee889dfcfcff4f5f2bf56470993d34ca64

Questions:

What is the OSI model?

Set of specifications that network hardware manufacturers must respect
The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology
How is the OSI model organized?

Alphabetically
From the lowest to the highest level
Randomly
File: 0-OSI_model

1. Types of network
https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/4b995d4f8078b44afa968d68a98035d2bd7e8fac.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240228T105546Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e244498cbe2b1d4adfdbb86dd1a5c4dc6f4556f86c4d4031fc374a3ccda0966c
LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

Questions:

What type of network a computer in local is connected to?

Internet
WAN
LAN
What type of network could connect an office in one building to another office in a building a few streets away?

Internet
WAN
LAN
What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

Internet
WAN
LAN
File: 1-types_of_network

2. MAC and IP address
https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1e348ba3bcbb094b02922f821ffeb3d8c5438b7b.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240228T105546Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7c423819f61a784b83fc060af632ba8d5305a46245f8af179d0b26e18fd7437b
Questions:

What is a MAC address?

The name of a network interface
The unique identifier of a network interface
A network interface
What is an IP address?

Is to devices connected to a network what postal address is to houses
The unique identifier of a network interface
Is a number that network devices use to connect to networks
File: 2-MAC_and_IP_address

3. UDP and TCP
https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/3d92e3c4a470f8ecf4c73db511fcbbadaa002e1c.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240228T105546Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=31afc11458327732cd92740151024fd71289fe4c844facf711ccfef7e141e58a
Let’s fill the empty parts in the drawing above.

Questions:

Which statement is correct for the TCP box:
It is a protocol that is transferring data in a slow way but surely
It is a protocol that is transferring data in a fast way and might loss data along in the process
Which statement is correct for the UDP box:
It is a protocol that is transferring data in a slow way but surely
It is a protocol that is transferring data in a fast way and might loss data along in the process
Which statement is correct for the TCP worker:
Have you received boxes x, y, z?
May I increase the rate at which I am sending you boxes?
File: 3-UDP_and_TCP

4. TCP and UDP ports
Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:

22 for SSH
80 for HTTP
443 for HTTPS
Note that a specific IP + port = socket.

Write a Bash script that displays listening ports:

That only shows listening sockets
That shows the PID and name of the program to which each socket belongs

EXAMPLE
File: 4-TCP_and_UDP_ports

5. Is the host on the network
The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command ping uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.

Write a Bash script that pings an IP address passed as an argument.

Requirements:

Accepts a string as an argument
Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
Ping the IP 5 times
Example:

It is interesting to look at the time value, which is the time that it took for the ICMP request to go to the 8.8.8.8 IP and come back to my host. The IP 8.8.8.8 is owned by Google, and the quickest roundtrip between my computer and Google was 7.57 ms which is pretty fast, which is a sign that the network path between my computer and Google’s datacenter is in good shape. A slow ping would indicate a slow network.

Next time you feel that your connection is slow, try the ping command to see what is going on!
File: 5-is_the_host_on_the_network
