0x06-regular_expressions Project INSTRUCTION
===========================================
===========================================
Concepts-For this project, we expect you to look at this concept:
++++++++
Regular Expression-Read about regexp:
http://www.regular-expressions.info/
http://www.w3schools.com/jsref/jsref_obj_regexp.asp Play with regexp (or compose them):

Ruby: http://rubular.com/

PHP/Javascript/Python: https://regex101.com/

Background Context
+++++++++++++++++
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a

Resources
++++++++++++
Read or watch:

Regular expressions - basics: https://www.slideshare.net/neha_jain/introducing-regular-expressions
Regular expressions - advanced: https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518
Rubular is your best friend: https://rubular.com/
Use a regular expression against a problem: now you have 2 problems :https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/
Learn Regular Expressions with simple, interactive exercises : https://regexone.com/

Requirements
+++++++++++
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
All your regex must be built for the Oniguruma library

TASKS
+++++++
+++++++
0. Simply matching School

https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240227%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240227T071006Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=303ed23952f1950375c28c6e7c2f3d04e3e1deb96cd0ad8eba8ea378dfa1894b

Requirements:

The regular expression must match School
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Example:

sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
File: 0-simply_match_school.rb

1. Repetition Token #0
https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240227%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240227T071006Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6f275b20c08b90b045d4b7c6734e14325081b907722e432fe2898b2fd8c589ff

Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
File: 1-repetition_token_0.rb

2. Repetition Token #1
https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240227%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240227T071006Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=94692f87feb6c67633723e01d0652e6a1fba2844065c61e0cbc3ce4b04484865

Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
File: 2-repetition_token_1.rb

3. Repetition Token #2
https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240227%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240227T071006Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=18f67498f1940d2dabc19596333f2c06b2dbaacde3790e84d7de75016618719b

Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
File: 3-repetition_token_2.rb

4. Repetition Token #3
https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240227%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240227T071006Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=792587f623024ade0ee5e11ac31e461611c5509b99edb8796d6ab04bb8790dbe

Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Your regex should not contain square brackets
File: 4-repetition_token_3.rb

5. Not quite HBTN yet
Requirements:

The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Example:

File: 5-beginning_and_end.rb

6. Call me maybe
This task is brought to you by a professional advisor Neha Jain: https://twitter.com/_nehajain , Senior Software Engineer at LinkedIn.

Requirement:

The regular expression must match a 10 digit phone number
Example:

File: 6-phone_number.rb

7. OMG WHY ARE YOU SHOUTING?
Requirement:

The regular expression must be only matching: capital letters
Example:

File: 7-OMG_WHY_ARE_YOU_SHOUTING.rb

ADVANCED TASK
8. Textme
This exercise was prepared for you by Guillaume Plessis: https://www.linkedin.com/in/gplessis/, VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project on Twitter: https://twitter.com/gui .

For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

Requirements:

Your script should output: [SENDER],[RECEIVER],[FLAGS]
The sender phone number or name (including country code if present)
The receiver phone number or name (including country code if present)
The flags that were used
You can find a [log file here]. - log file was notactive

Example:

File: 100-textme.rb
