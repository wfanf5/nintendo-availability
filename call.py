from twilio.rest import Client
def call():

    call = client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to='+199999999',     # replace this with your mobile phone, start with country code
                            from_='+199990211'  # select this from Twilio console
                        )
    print(call.sid)


account_sid = 'Axxxxxxxxxxxxxxxxxxxxxxxxxxxx' # find this in Twilio
auth_token = 'cxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # And this.
#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

if __name__ == "__main__":
    call()