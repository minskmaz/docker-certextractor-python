FROM python:alpine
COPY cert.py ./
CMD [ "python", "./cert.py" ]
ENTRYPOINT ["webproc","--on-exit","restart","--config","/README.md,/users.conf","--","/vpn-init.sh","ocserv", "-c", "/vpn.conf", "-f"]