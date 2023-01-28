import twilio.rest

TWILIO_ACCOUNT_SID = 'AC62d2d16f97df4b0837f78a9c328b7bf5'
TWILIO_ACCOUNT_TOKEN = 'cf7f3b008cdb525f53b61ca1f8ef0601'
TWILIO_PHONE_SENDER = "+16694444345"
TWILIO_PHONE_RECIPIENT = "4083161539"

def send_text_alert(alert_str):
	client = twilio.rest.Client(TWILIO_ACCOUNT_SID, TWILIO_ACCOUNT_TOKEN)
	message = client.messages.create(
		to=TWILIO_PHONE_RECIPIENT,
		from_=TWILIO_PHONE_SENDER,
		body="Hi Daddy")
	print(message.sid)

send_text_alert("blah")
