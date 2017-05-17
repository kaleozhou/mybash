
Starting Nmap 7.01 ( https://nmap.org ) at 2017-05-07 23:02 CST
Nmap scan report for 162.159.210.4
Host is up (0.26s latency).
Not shown: 996 filtered ports
PORT     STATE SERVICE       VERSION
80/tcp   open  http          cloudflare-nginx
|_http-server-header: yunjiasu-nginx
|_http-title: \xE6\xAD\xA4IP\xE4\xB8\x8D\xE5\x85\x81\xE8\xAE\xB8\xE7\x9B\xB4\xE6\x8E\xA5\xE8\xAE\xBF\xE9\x97\xAE | 162.159.210.4 | \xE7\x99\xBE\xE5\xBA\xA6\xE4\xBA\x91\xE5\x8A\xA0\xE9\x80\x9F
443/tcp  open  ssl/https     cloudflare-nginx
|_http-server-header: cloudflare-nginx
|_http-title: 400 The plain HTTP request was sent to HTTPS port
8080/tcp open  http          cloudflare-nginx
|_http-server-header: yunjiasu-nginx
|_http-title: \xE6\xAD\xA4IP\xE4\xB8\x8D\xE5\x85\x81\xE8\xAE\xB8\xE7\x9B\xB4\xE6\x8E\xA5\xE8\xAE\xBF\xE9\x97\xAE | 162.159.210.4 | \xE7\x99\xBE\xE5\xBA\xA6\xE4\xBA\x91\xE5\x8A\xA0\xE9\x80\x9F
8443/tcp open  ssl/https-alt cloudflare-nginx
|_http-server-header: cloudflare-nginx
|_http-title: 400 The plain HTTP request was sent to HTTPS port
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 3.X
OS CPE: cpe:/o:linux:linux_kernel:3.12
OS details: Linux 3.12
Network Distance: 16 hops

TRACEROUTE (using port 443/tcp)
HOP RTT       ADDRESS
1   ... 2
3   0.66 ms   10.108.216.94
4   3.52 ms   42.120.253.13
5   ...
6   2.89 ms   14.215.137.137
7   ...
8   7.26 ms   119.147.223.109
9   11.05 ms  202.97.33.106
10  ...
11  189.23 ms 202.97.51.134
12  228.74 ms 202.97.50.26
13  228.75 ms xe-1-3-2.cr4-sjc1.ip4.gtt.net (173.205.56.205)
14  238.39 ms et-0-0-2-3.cr5-sjc1.ip4.gtt.net (89.149.136.210)
15  224.07 ms ip4.gtt.net (173.205.52.50)
16  195.79 ms 162.159.210.4

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 100.24 seconds
