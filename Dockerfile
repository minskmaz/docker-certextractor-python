FROM python:alpine

ENV ACME_PATH /acme
ENV CERT_PATH /certs
ENV ACME_FILE acme.json
ENV SLEEP_TIME 86400

COPY cert.py ./
ENTRYPOINT ["python3"]
CMD ["-u", "cert.py"]
