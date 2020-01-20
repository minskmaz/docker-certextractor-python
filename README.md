# docker-certextractor-python
This super lightweight container converts Traefik acme.json files to a bunch of certificate and key files.

Configuration is done using environment variables, the defaults are as follows:

ACME_PATH -> '/acme'
CERT_PATH -> '/certs'
ACME_FILE -> 'acme.json'
SLEEP_TIME -> 86400

The certificate and key files will be output to the CERT_PATH directory with the domain name as the filename and .cer and .key as their extensions.

This will also generate a .chain.cer file containing the full cert chain.

The CERT_PATH variable is designed to be used with docker volumes to take the newly created certs out of the directory for use elsewhere.

SLEEP_TIME is the duration (in seconds) that the script will wait before re-checking and processing the acme.json file. By default this is 86400 seconds. Sleeping can be disabled (i.e. the script will run once then exit) using a value of 0.