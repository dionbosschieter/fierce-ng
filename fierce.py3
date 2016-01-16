#!/usr/bin/env python3
import dns.resolver
import sys

if len(sys.argv) < 3:
	print("""Fierce-NG <dionbosschieter@gmail.com>
Specify a hostname to check its subdomains on
You can also specify a dns server to use as nameserver 

The script will check for a file named `hosts.txt` and query for the subdomains defined in this file.

Todo:
* Add default dns zone transfer check
* Add a nice parameter to sleep between multiple queries

Example""", sys.argv[0], "dionbosschieter.nl 8.8.8.8")
	exit()

resolver = dns.resolver.Resolver()
resolver.nameservers = [sys.argv[2]]
print('[*] using nameserver', resolver.nameservers)
host_to_attack = sys.argv[1]

def query(hostname):
	try:
		data = resolver.query(hostname, 'A')

		for host in data:
			print('[*] Host ', hostname, 'found', host, 'has settings')
	except dns.resolver.NXDOMAIN:
		print('[*] No match for', hostname)
	except dns.resolver.NoNameservers:
		print('[*] Weird domain??', hostname)

handler = open('hosts.txt', 'r')

for line in handler:
	subdomain = line.strip()
	#try: 
	query(subdomain + '.' + host_to_attack)
	#except:
	#	handler.close()
	#	exit()
