#!/bin/python3

#Created by Lmmp04

import socket
import os
import random
import requests
import sys

port = 80

print("Please be sure the following two inputs are matching ips and urls.")
print ('\n')
ip = input("What is the ip you would like to monitor? : ").lower().strip()
print ("")
url = input("What is the full url of the website you are monitoring? Ex: https://google.com : ").lower().strip()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, port))

print ("Socket succesfully created and connected. Website is online!")
print ('\n')
print ("Pinging ip to check for latency")
print ('\n')

os.system('ping -c 3 ' + ip)

print ('\n')
print ("Ping was succesful!")
print ("")

r = requests.get(url)

print(r)

r = requests.post(url, data = {'key':'value'})

print ("Sending http request to url")
print ("")
print (r)
print ("Outcome depends on status code")
