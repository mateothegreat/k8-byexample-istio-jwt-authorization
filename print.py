import datetime

import jwcrypto.jwk as jwk
import python_jwt as jwt


payload = {

    'iss': 'ISSUER',
    'sub': 'SUBJECT',
    'aud': 'AUDIENCE',
    'role': 'user',
    'permission': 'read'

}

with open('keys/jwt-public.pem', "rb") as f:
    public_key = jwk.JWK.from_pem(f.read())
    public_key = public_key.export()

with open('keys/jwt-private.pem', "rb") as f:
    private_key = jwk.JWK.from_pem(f.read())
    private_key = private_key.export()

token = jwt.generate_jwt(payload, jwk.JWK.from_json(private_key), 'RS256', datetime.timedelta(minutes = 60))

print(f'Public key: {public_key}')
print(f'Example JWT Token: {token}')

print('Generating a test token and validating..')

header, claims = jwt.verify_jwt(token, jwk.JWK.from_json(public_key), ['RS256'])

print(f'Header: {header}')
print(f'Claims: {claims}')

print('---')
print('istio jwks: { "keys": [ ' + public_key + '] }')
