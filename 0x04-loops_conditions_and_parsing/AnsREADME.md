ANSWERES: How result are to appear
=================================
0. Task
1. Task
sylvain@ubuntu$ head -n 2 1-for_best_school 
#!/usr/bin/env bash
# This script is displaying "Best School" 10 times
sylvain@ubuntu$ ./1-for_best_school 
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 

2. Task
sylvain@ubuntu$ ./2-while_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 

3. Task
sylvain@ubuntu$ ./3-until_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 

4. Task
sylvain@ubuntu$ ./4-if_9_say_hi
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Hi
Best School
sylvain@ubuntu$

5. Task
sylvain@ubuntu$ ./5-4_bad_luck_8_is_your_chance
Best School
Best School
Best School
bad luck
Best School
Best School
Best School
good luck
Best School
Best School
sylvain@ubuntu$ 

6. Task
sylvain@ubuntu$ ./6-superstitious_numbers
1
2
3
4
bad luck from China
5
6
7
8
9
bad luck from Japan
10
11
12
13
14
15
16
17
bad luck from Italy
18
19
20
sylvain@ubuntu$ 

7. Task
sylvain@ubuntu$ ./7-clock | head -n 70
Hour: 0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
Hour: 1
1
2
3
4
5
6
7
8
9
sylvain@ubuntu$ 

8. Task
sylvain@ubuntu$ ls
100-read_and_cut              1-for_best_school         6-superstitious_numbers
101-tell_the_story_of_passwd  2-while_best_school       7-clock
102-lets_parse_apache_logs    3-until_best_school       8-for_ls
103-dig_the-data              4-if_9_say_hi                  9-to_file_or_not_to_file
10-fizzbuzz                   5-4_bad_luck_8_is_your_chance
sylvain@ubuntu$  ./8-for_ls
read_and_cut
tell_the_story_of_passwd
lets_parse_apache_logs
dig_the-data
fizzbuzz
for_best_school
while_best_school
until_best_school
if_9_say_hi
4_bad_luck_8_is_your_chance
superstitious_numbers
clock
for_ls
to_file_or_not_to_file
sylvain@ubuntu$ 

9. Task
sylvain@ubuntu$ file school
school: cannot open `school' (No such file or directory)
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
school file does not exist
sylvain@ubuntu$ touch school
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
school file exists
school file is empty
school is a regular file
sylvain@ubuntu$ echo 'betty' > school 
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
school file exists
school file is not empty
school is a regular file
sylvain@ubuntu$ rm school 
sylvain@ubuntu$ mkdir school
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
school file exists
school file is not empty
sylvain@ubuntu$ 

10. Task
sylvain@ubuntu$ ./10-fizzbuzz | head -20
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
sylvain@ubuntu$
 
11. Task
sylvain@ubuntu$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
messagebus:x:102:106::/var/run/dbus:/bin/false
landscape:x:103:109::/var/lib/landscape:/bin/false
sshd:x:104:65534::/var/run/sshd:/usr/sbin/nologin
pollinate:x:105:1::/var/cache/pollinate:/bin/false
vagrant:x:1000:1000::/home/vagrant:/bin/bash
colord:x:106:112:colord colour management daemon,,,:/var/lib/colord:/bin/false
statd:x:107:65534::/var/lib/nfs:/bin/false
sylvain:98:99:Sylvain:/home/sylvain:/bin/bash
puppet:x:108:114:Puppet configuration management daemon,,,:/var/lib/puppet:/bin/false
ubuntu:x:1001:1001:Ubuntu:/home/ubuntu:/bin/bash
sylvain@ubuntu$ ./100-read_and_cut
root:0:/root
daemon:1:/usr/sbin
bin:2:/bin
sys:3:/dev
sync:4:/bin
games:5:/usr/games
man:6:/var/cache/man
lp:7:/var/spool/lpd
mail:8:/var/mail
news:9:/var/spool/news
uucp:10:/var/spool/uucp
proxy:13:/bin
www-data:33:/var/www
backup:34:/var/backups
list:38:/var/list
irc:39:/var/run/ircd
gnats:41:/var/lib/gnats
nobody:65534:/nonexistent
libuuid:100:/var/lib/libuuid
syslog:101:/home/syslog
messagebus:102:/var/run/dbus
landscape:103:/var/lib/landscape
sshd:104:/var/run/sshd
pollinate:105:/var/cache/pollinate
vagrant:1000:/home/vagrant
colord:106:/var/lib/colord
statd:107:/var/lib/nfs
sylvain:99:/bin/bash
puppet:108:/var/lib/puppet
ubuntu:1001:/home/ubuntu
sylvain@ubuntu$ 

12. Task 
sylvain@ubuntu$ ./101-tell_the_story_of_passwd
The user root is part of the 0 gang, lives in /root and rides /bin/bash. 0's place is protected by the passcode x, more info about the user here: root
The user daemon is part of the 1 gang, lives in /usr/sbin and rides /usr/sbin/nologin. 1's place is protected by the passcode x, more info about the user here: daemon
The user bin is part of the 2 gang, lives in /bin and rides /usr/sbin/nologin. 2's place is protected by the passcode x, more info about the user here: bin
The user sys is part of the 3 gang, lives in /dev and rides /usr/sbin/nologin. 3's place is protected by the passcode x, more info about the user here: sys
The user sync is part of the 65534 gang, lives in /bin and rides /bin/sync. 4's place is protected by the passcode x, more info about the user here: sync
The user games is part of the 60 gang, lives in /usr/games and rides /usr/sbin/nologin. 5's place is protected by the passcode x, more info about the user here: games
The user man is part of the 12 gang, lives in /var/cache/man and rides /usr/sbin/nologin. 6's place is protected by the passcode x, more info about the user here: man
The user lp is part of the 7 gang, lives in /var/spool/lpd and rides /usr/sbin/nologin. 7's place is protected by the passcode x, more info about the user here: lp
The user mail is part of the 8 gang, lives in /var/mail and rides /usr/sbin/nologin. 8's place is protected by the passcode x, more info about the user here: mail
The user news is part of the 9 gang, lives in /var/spool/news and rides /usr/sbin/nologin. 9's place is protected by the passcode x, more info about the user here: news
The user uucp is part of the 10 gang, lives in /var/spool/uucp and rides /usr/sbin/nologin. 10's place is protected by the passcode x, more info about the user here: uucp
The user proxy is part of the 13 gang, lives in /bin and rides /usr/sbin/nologin. 13's place is protected by the passcode x, more info about the user here: proxy
The user www-data is part of the 33 gang, lives in /var/www and rides /usr/sbin/nologin. 33's place is protected by the passcode x, more info about the user here: www-data
The user backup is part of the 34 gang, lives in /var/backups and rides /usr/sbin/nologin. 34's place is protected by the passcode x, more info about the user here: backup
The user list is part of the 38 gang, lives in /var/list and rides /usr/sbin/nologin. 38's place is protected by the passcode x, more info about the user here: Mailing List Manager
The user irc is part of the 39 gang, lives in /var/run/ircd and rides /usr/sbin/nologin. 39's place is protected by the passcode x, more info about the user here: ircd
The user gnats is part of the 41 gang, lives in /var/lib/gnats and rides /usr/sbin/nologin. 41's place is protected by the passcode x, more info about the user here: Gnats Bug-Reporting System (admin)
The user nobody is part of the 65534 gang, lives in /nonexistent and rides /usr/sbin/nologin. 65534's place is protected by the passcode x, more info about the user here: nobody
The user libuuid is part of the 101 gang, lives in /var/lib/libuuid and rides . 100's place is protected by the passcode x, more info about the user here: 
The user syslog is part of the 104 gang, lives in /home/syslog and rides /bin/false. 101's place is protected by the passcode x, more info about the user here: 
The user messagebus is part of the 106 gang, lives in /var/run/dbus and rides /bin/false. 102's place is protected by the passcode x, more info about the user here: 
The user landscape is part of the 109 gang, lives in /var/lib/landscape and rides /bin/false. 103's place is protected by the passcode x, more info about the user here: 
The user sshd is part of the 65534 gang, lives in /var/run/sshd and rides /usr/sbin/nologin. 104's place is protected by the passcode x, more info about the user here: 
The user pollinate is part of the 1 gang, lives in /var/cache/pollinate and rides /bin/false. 105's place is protected by the passcode x, more info about the user here: 
The user vagrant is part of the 1000 gang, lives in /home/vagrant and rides /bin/bash. 1000's place is protected by the passcode x, more info about the user here: 
The user colord is part of the 112 gang, lives in /var/lib/colord and rides /bin/false. 106's place is protected by the passcode x, more info about the user here: colord colour management daemon,,,
The user statd is part of the 65534 gang, lives in /var/lib/nfs and rides /bin/false. 107's place is protected by the passcode x, more info about the user here: 
The user puppet is part of the 114 gang, lives in /var/lib/puppet and rides /bin/false. 108's place is protected by the passcode x, more info about the user here: Puppet configuration management daemon,,,
The user ubuntu is part of the 1001 gang, lives in /home/ubuntu and rides /bin/bash. 1001's place is protected by the passcode x, more info about the user here: Ubuntu
sylvain@ubuntu$

13. Task
sylvain@ubuntu$ ./102-lets_parse_apache_logs | tail -n 10
185.130.5.207 301
185.130.5.207 301
91.224.140.223 200
62.210.142.23 304
92.222.20.166 304
180.76.15.19 200
2.1.201.36 304
198.58.99.82 304
50.116.30.23 304
209.133.111.211 200
sylvain@ubuntu$

14. Tasks
sylvain@ubuntu$ ./103-dig_the-data | head -n 10
    141 130.0.236.153 200
    140 62.210.250.66 200
    117 103.243.26.232 404
    67 195.154.172.143 200
    60 78.154.190.29 200
    45 195.154.172.59 200
    41 62.210.248.185 200
    41 167.114.156.198 200
    36 2.1.201.36 304
    36 195.154.172.53 200
sylvain@ubuntu$

