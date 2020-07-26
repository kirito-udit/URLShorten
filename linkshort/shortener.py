import pyshorteners

a = input()
s=pyshorteners.Shortener()
x=s.tinyurl.short(a)