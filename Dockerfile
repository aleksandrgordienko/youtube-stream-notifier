FROM python:3.7-alpine

RUN apk add gcc g++ make libffi-dev openssl-dev

# Create app directory
WORKDIR /app

# Install app dependencies
COPY src/requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY src /app

CMD [ "python", "main.py" ]