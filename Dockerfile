FROM python:3.7.17-alpine

RUN addgroup -S monkeyray \
&& adduser -S monkeyray -G monkeyray \
&&  pip3 install flask request jsonify \
&&  mkdir -p /tmp/run \
&&  chown monkeyray:monkeyray -R /tmp/run

WORKDIR /tmp/run

COPY --chown=monkeyray:monkeyray . /tmp/run/

EXPOSE 8080

ENTRYPOINT ["python", "app.py"]
