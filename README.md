# smsReceiver
It's just a wrapper of sites that provide online phone number to receive sms.

http://hs3x.com/

https://ireceivesmsonline.com/

#Install
<pre>
pip install smsReceiver
</pre>

#Usage
<pre>
from smsReceiver.numberGen import hs3x
from smsReceiver.numberGen import ireceivesmsonline

#using http://hs3x.com/
m = hs3x.generator()
number,countryCode = m.getNumber()
print countryCode,number
#your code goes Here
print m.checkSMS('Message Pattern')

#using https://ireceivesmsonline.com
m = ireceivesmsonline.generator()
number,countryCode = m.getNumber()
print countryCode,number
#your code goes Here
print m.checkSMS('Message Pattern')
</pre>
