from twilio.rest import Client


account_sid = 'AC1f44c880d24aecd7377e44ebd1c3ca7a'
auth_token = 'be47cf78ddfef1eda7b45646b19e5a27'
client = Client(account_sid, auth_token)


message = client.messages.create(
 from_='+18336011146',
 to='+17069496174'
)


print(message.sid)

