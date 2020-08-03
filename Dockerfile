FROM python:alpine

ENV ACME_PATH /acme
ENV CERT_PATH /certs
ENV ACME_FILE acme.json
ENV SLEEP_TIME 86400
ENV ACME_KEYS le

COPY cert.py ./
CMD ["python", "-u", "cert.py"]
