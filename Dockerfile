FROM amazonlinux
WORKDIR /deploy

RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - && \
  yum install -y python3-pip python3-devel python2-devel python2-pip gcc-c++ make mysql-devel nodejs nano findutils libyaml libyaml-devel git && \
  yum clean all && rm -rf /var/cache/yum

RUN npm install -g serverless

RUN ls -la /usr/local/bin
RUN find / -iname "pip*"

COPY . .

RUN pip-2 install --no-cache-dir -r requirements.txt --target .

RUN ["chmod", "+x", "deploy.sh"]

CMD ./deploy.sh
