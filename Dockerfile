FROM python:alpine
COPY cert.py ./
CMD [ "python", "-u", "./cert.py" ]
