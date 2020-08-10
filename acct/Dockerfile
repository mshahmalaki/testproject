FROM python:slim

ENV ACCT_DEBUG 0
ENV ACCT_ENV production
ENV ACCT_DATABASE mysql+pymysql://acctUser:acctPass@acct_db:3306/acctDB?charset=utf8mb4
ENV AUTH_SERVICE_URL http://auth:5001

WORKDIR /app

COPY . .

RUN pip install -U pip
RUN pip install .

EXPOSE 5000

ENTRYPOINT [ "./docker-entrypoint.sh" ]