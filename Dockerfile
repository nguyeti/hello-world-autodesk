# Initialize the base image
FROM python:3.10.4-alpine

WORKDIR /hello-world-autodesk

ADD . $WORKDIR

RUN pip install -r requirements.txt

# Setting up this environment variable in order to be able to change the value during the docker image build
ARG ENV="production"
ENV FLASK_APP="src/app.py"
ENV FLASK_ENV=$ENV

# Running the unit tests
RUN ["python", "-m", "unittest", "discover", "-v"]

# Command to start the container
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]