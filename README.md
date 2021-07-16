# StretchSMS
SMS reminders to standup and stretch - sent directly to your phone!<br>
By default, messages are sent hourly at the 15-minute mark of each hour (during business hours only).<br>
This frequency can be adjusted by editing the `crontab` in the `Dockerfile`.<br>
Successful builds are posted up to [StretchSMS DockerHub](https://hub.docker.com/repository/docker/buechnergis/stretchsms).

## Quick Start (docker-compose)
```
docker-compose build stretchsms
docker-compose up -d stretchsms
```
