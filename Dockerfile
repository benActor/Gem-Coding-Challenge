FROM python:3.8

# set the working directory in the container
WORKDIR /src

COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY ../ .

EXPOSE 8888

# command to run on container start
CMD [ "python", "./app.py" ]