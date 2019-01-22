from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

client_id = 'd5d295a844634ad0b423f5e2fb5151ae'
client_secret = 'dd51a6374cd34e90a567c0a454410287'

print('BackendApplicationClient')
client = BackendApplicationClient(client_id=client_id)

print('OAuth2Session')
oauth = OAuth2Session(client=client)

print('oauth.fetch_token')
token = oauth.fetch_token(
    token_url='https://api.tagplus.com.br/oauth2/token',
    client_id=client_id,
    client_secret=client_secret,
)

print(token)
