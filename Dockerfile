FROM python:alpine
COPY cert.py ./
CMD [ "python", "./cert.py" ]
