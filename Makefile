keys:

	mkdir -p keys
	openssl genrsa -out keys/jwt-private.pem 2048
	openssl rsa -in keys/jwt-private.pem -pubout -out keys/jwt-public.pem

rekey:

	rm -rf keys
	$(MAKE) keys