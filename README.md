# Flask-SocketIO-Supervisord Example Application

This is a simple example application of a chat using Flask and Flask-SocketIO.

It consists of:

- A Flask application using Flask-SocketIO that handles the Websocket connections
  (running with gunicorn and an eventlet worker)
- A Flask application that contains the REST interface for the chat
  (running with gunicorn and normal sync workers)
- Redis for handling the inter process communication between the two Flask applications
- A nginx reverse proxy in front of the two Flask applications
- Supervisord for running everything in a Docker container
- Docker compose that runs the Docker container with the example application and a Redis container

# Motivation

Flask-SocketIO recommends either using eventlet or gevent as the worker type for the gunicorn web server.
However, an existing Flask application might already run using the regular sync gunicorn workers. Assuming we don't 
want to change the setup for the existing Flask application we can run the Flask-SocketIO application in a separate
process. In this case a Redis server can be used to handle the inter process communication between the two Flask applications.

# TODO

- Extend the clients for load testing
- Add a database for storing the chat messages
- Goal: Run everything in AWS Elastic Beanstalk

