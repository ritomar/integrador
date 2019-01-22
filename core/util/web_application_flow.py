from requests_oauthlib import OAuth2Session

client_id = 'd5d295a844634ad0b423f5e2fb5151ae'
client_secret = 'dd51a6374cd34e90a567c0a454410287'
redirect_uri = 'http://ritomar.pythonanywhere.com/'

# Note that these are Google specific scopes
# scope = ['https://www.googleapis.com/auth/userinfo.email',
#              'https://www.googleapis.com/auth/userinfo.profile']
scope = ['read:pedidos', 'read:clientes', 'read:produtos']

# oauth = OAuth2Session(client_id, redirect_uri=redirect_uri,
#                       scope=scope)

oauth = OAuth2Session(client_id=client_id, scope=scope)

# authorization_url, state = oauth.authorization_url(
#     'https://accounts.google.com/o/oauth2/auth',
#     # access_type and prompt are Google specific extra
#     # parameters.
#     access_type="offline", prompt="select_account")

authorization_url, state = oauth.authorization_url(
    'https://developers.tagplus.com.br/authorize',
)

print('Please go to %s and authorize access.' % authorization_url)
authorization_response = input('Enter the full callback URL: ')

# token = oauth.fetch_token(
#     'https://accounts.google.com/o/oauth2/token',
#     authorization_response=authorization_response,
#     # Google specific extra parameter used for client
#     # authentication
#     client_secret=client_secret)

token = oauth.fetch_token(
    'https://api.tagplus.com.br/oauth2/token',
    code='00ebf63875fd485dadbef1f4a3897935',
    client_id=client_id,
    client_secret=client_secret,
    headers={'enctype': 'application/x-www-form-urlencoded'},
)


# r = oauth.get('https://www.googleapis.com/oauth2/v1/userinfo')
# # Enjoy =)

r = oauth.get('https://api.tagplus.com.br/produtos')
print(r.text)




