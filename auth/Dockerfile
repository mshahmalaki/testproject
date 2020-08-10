FROM python:slim

ENV AUTH_DEBUG 0
ENV AUTH_ENV production
ENV AUTH_DATABASE mysql+pymysql://authUser:authPass@auth_db:3306/authDB?charset=utf8mb4
ENV ACCT_SERVICE_URL http://acct:5000

WORKDIR /app

COPY . .

RUN pip install -U pip
RUN pip install .

EXPOSE 5001

ENTRYPOINT [ "./docker-entrypoint.sh" ]