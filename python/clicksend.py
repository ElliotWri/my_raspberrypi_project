username='wrightelliot106'
api_key = '5E668A00-8249-F803-7A2E-B7CE03059A74'
msg_to = '+17735956350'
msg_from = ''
msg_body = 'this is a test message'

import json, subprocess

request = { "messages" : [ { "source":"rpi", "from":msg_from, "to":msg_to, "body":msg_body } ] }
request = json.dumps(request)
cmd = "curl https://rest.clicksend.com/v3/sms/send -u " + username + ":" + api_key + " -H \"Content-Type: application/json\" -X POST --data-raw '" + request + "'"
p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
(output,err) = p.communicate()
#print output
