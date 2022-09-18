FROM python:3.7.4-alpine3.10

RUN apk --no-cache add libxml2 libxml2-dev libxslt-dev gcc musl-dev wget ca-certificates

ARG YASS_VERSION="0.11.7"

WORKDIR /yass
RUN wget "https://github.com/mrnfrancesco/yass/archive/v${YASS_VERSION}.zip" -O yass.zip && \
    unzip yass.zip && \
    cd yass-${YASS_VERSION} && \
    ./setup.py install && \
    rm -rf /yass

CMD ["yass", "-h"]
