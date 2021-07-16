# set base image (host OS)
FROM python:3.10.0b3-alpine3.14

# Set the appropriate timezone
RUN apk add tzdata && \
    cp /usr/share/zoneinfo/US/Central /etc/localtime && \
    echo "US/Central" > /etc/timezone && \
    apk del tzdata

# install dependencies
#RUN pip install -r requirements.txt

# Make and set working directorythe working directory
RUN mkdir /stretchsms
WORKDIR /stretchsms 

# Run the cron At minute 15 past every hour from 8-16.
RUN echo '15       8-16       *       *       *       /stretchsms/startup.sh' >> /etc/crontabs/root

