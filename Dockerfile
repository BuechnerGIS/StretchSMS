# set base image (host OS)
FROM python:3.10.0b3-alpine3.14

# set the working directory in the container
WORKDIR /home

# copy the dependencies file to the working directory
#COPY requirements.txt .

# install dependencies
#RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

# command to run on container start
CMD [ "python3", "./run.py" ] 
