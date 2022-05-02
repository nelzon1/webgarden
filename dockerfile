FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8699
STOPSIGNAL SIGTERM
CMD [ "/usr/src/app/start-server.sh" ]