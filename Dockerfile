# set base image (host OS)
FROM python:3.10.0b3-alpine3.14

# install dependencies
#RUN pip install -r requirements.txt

# Make and set working directorythe working directory
RUN mkdir /stretchsms
WORKDIR /stretchsms 

# Copy files into working dir
COPY . /stretchsms

# Run the cron At minute 15 past every hour from 8-16.
RUN echo '15       8-16       *       *       *       /stretchsms/startup.sh' >> /etc/crontabs/root
