
FROM python:3.6-slim
# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
# Copy application dependency manifests to the container image.
# Copying this separately prevents re-running pip install on every code change.


COPY requirements.txt .
RUN pip uninstall tensorflow
RUN pip install tensorflow==1.14
RUN pip install -r requirements.txt

RUN python test.py

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.



CMD ["python","app.py"]
