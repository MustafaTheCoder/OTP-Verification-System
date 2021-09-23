import os
import math
import random
import smtplib

digits="0123456789"
OTP=""

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"

msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("your_account", "your_password")
emailid = input("Enter Your Email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP: ")
if a == OTP:
    print("Verified!")
else:
    print("Incorrect OTP!")