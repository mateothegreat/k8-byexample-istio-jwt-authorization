```bash
$ python print.py

Public key: {"e":"AQAB","kid":"uC0f7roWvS-N_RLfSLcuUsOBiXb3MLGWdDUls_2KPCQ","kty":"RSA","n":"tGfd5sP5mUg6cKDocCt2N3Xxhgzbdrg8BjXxeVsEg-fTZVMMIP8LdchyE7e_ZTDaoxJ_iTjhkudezgZbV4BU_cFuZ7ZIcAKOSltj-1uohE6Kr5dT1B-KHpoFiyj4k3gJ7gC3Dt5aRRLIaCNyJmC1q4XEIm_BVBaP-vjE8dMmUR5pkkX9BNJ6LUSx7QJrg1dNdLkYR4kZO0c2qGpnpkKFdZzzuYX_2xVPILiv-0LYz1hyFOuJupiTUw0D7_SCXqEyCnDJcEQZG_h3ZtVNIhO10bVUV-Ad7Dsi_nKSwWYqzphaHaZAsvDpYjR7sOR9rYiG1cjN_BFvAr9rQhik1o4b0w"}
Example JWT Token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJBVURJRU5DRSIsImV4cCI6MTU5MTQzOTEwNCwiaWF0IjoxNTkxNDM1NTA0LCJpc3MiOiJJU1NVRVIiLCJqdGkiOiJ2ZWtZSWpZU3pOU1hnbFdmWUVJYzV3IiwibmJmIjoxNTkxNDM1NTA0LCJwZXJtaXNzaW9uIjoicmVhZCIsInJvbGUiOiJ1c2VyIiwic3ViIjoiU1VCSkVDVCJ9.lhEltETbzOic98NF-9j6ciPU2jt4Zx9JbRs1gOYhu7Yt3c4cxHWRZjheVkxIUpjlp9RWFieHh0spk5oLp9jocM9o2_aXzCfm4LeGXv126Y07twrRQx89ee8npK5wvOv-O2K4pwy7SGlaWlf-QW058A5iizPEgjeYXtWQjeirjpIY00dq8H3t-yzu6v5yWWFARXWlnxSW_5bUlAgqpGqGK1tq7_2OfkQ5NnKstf80nyqde95y9wi-TqNIW8l60sEvHj0A2zFQ1jZr2pb1W1kpS_DFNgIDGnOen-nmfhNZfPkYaVqQTBgYAyteBof-IQOy36npD7IAmRuUoewDEIkftA

Generating a test token and validating..

Header: {'alg': 'RS256', 'typ': 'JWT'}
Claims: {'aud': 'AUDIENCE', 'exp': 1591439104, 'iat': 1591435504, 'iss': 'ISSUER', 'jti': 'vekYIjYSzNSXglWfYEIc5w', 'nbf': 1591435504, 'permission': 'read', 'role': 'user', 'sub': 'SUBJECT'}

---

istio jwks: { "keys": [ {"e":"AQAB","kid":"uC0f7roWvS-N_RLfSLcuUsOBiXb3MLGWdDUls_2KPCQ","kty":"RSA","n":"tGfd5sP5mUg6cKDocCt2N3Xxhgzbdrg8BjXxeVsEg-fTZVMMIP8LdchyE7e_ZTDaoxJ_iTjhkudezgZbV4BU_cFuZ7ZIcAKOSltj-1uohE6Kr5dT1B-KHpoFiyj4k3gJ7gC3Dt5aRRLIaCNyJmC1q4XEIm_BVBaP-vjE8dMmUR5pkkX9BNJ6LUSx7QJrg1dNdLkYR4kZO0c2qGpnpkKFdZzzuYX_2xVPILiv-0LYz1hyFOuJupiTUw0D7_SCXqEyCnDJcEQZG_h3ZtVNIhO10bVUV-Ad7Dsi_nKSwWYqzphaHaZAsvDpYjR7sOR9rYiG1cjN_BFvAr9rQhik1o4b0w"}] }
```