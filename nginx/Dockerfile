FROM debian

ARG ELK_VERSION

RUN apt-get update -y -q
RUN apt-get upgrade -y -q
RUN apt-get install nginx curl vim apt-utils ssh -y -q
RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${ELK_VERSION}-amd64.deb

RUN dpkg -i filebeat-${ELK_VERSION}-amd64.deb

ADD config/filebeat/filebeat.yml /etc/filebeat/filebeat.yml

RUN chmod go-w /etc/filebeat/filebeat.yml
RUN ln -s /etc/filebeat/filebeat.yml /usr/share/filebeat/filebeat.yml
RUN filebeat test config -c /etc/filebeat/filebeat.yml
RUN systemctl enable filebeat

CMD ["nginx", "-g", "daemon off;"]