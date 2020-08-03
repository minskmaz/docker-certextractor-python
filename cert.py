import json
from base64 import b64decode
import os
from time import sleep

def main():
    acme_path = os.getenv('ACME_PATH', '/acme')
    cert_path = os.getenv('CERT_PATH', '/certs')
    acme_file = os.path.join(acme_path,os.getenv('ACME_FILE', 'acme.json'))
    sleep_time = int(os.getenv('SLEEP_TIME', '86400'))
    acme_keys = os.getenv('ACME_KEY', 'le').split(',')

    acme_content_raw = ''
    print('Using acme file: '+acme_file)
    with open(acme_file,'r') as fhand:
        acme_content_raw = fhand.read()

    acme_content = json.loads(acme_content_raw)

    for acme_key in acme_keys:
        certificates = acme_content[acme_key]['Certificates']

        print('Found '+str(len(certificates))+' certs.')
        for cert in certificates:
            domain = cert['domain']['main']
            cert_b64 = cert['certificate']
            key_b64 = cert['key']
            chaincert = b64decode(cert_b64)
            key = b64decode(key_b64)
            cert = chaincert.split(b'\n\n')[0]

            print('Writing cert chain file: '+domain+'.chain.cer')
            certchainfile = os.path.join(cert_path,domain+'.chain.cer')
            with open(certchainfile,'wb') as fhnd:
                fhnd.write(chaincert)

            print('Writing cert file: '+domain+'.cer')
            certfile = os.path.join(cert_path,domain+'.cer')
            with open(certfile,'wb') as fhnd:
                fhnd.write(cert)

            print('Writing key file: '+domain+'.key')
            keyfile = os.path.join(cert_path,domain+'.key')
            with open(keyfile,'wb') as fhnd:
                fhnd.write(key)
            
    
    if sleep_time < 1:
        print('Sleep time below 1 second, exiting!')
        exit()
    print('Sleeping for '+str(sleep_time)+' seconds.')
    sleep(sleep_time)
        


if __name__ == '__main__':
    while True:
        main()