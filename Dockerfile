FROM python:3.8.18-alpine

RUN addgroup -S monkeyray \
&&  adduser -S monkeyray -G monkeyray \
&&  pip3 install flask==1.1.4 \
    requests \
    jsonify \
    markupsafe==1.1.1 \
&&  mkdir -p /tmp/run \
&&  chown monkeyray:monkeyray -R /tmp/run

WORKDIR /tmp/run

COPY --chown=monkeyray:monkeyray . /tmp/run/

EXPOSE 8080

ENTRYPOINT ["python", "app.py"]
