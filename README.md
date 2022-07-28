
# Chat-application

Without the use of any pre-built libraries and powered by WebSockets, this application is production ready and is suitable for developing a full-fledged traditional messenger application, customer-support application etc. All you have to do is design a User Interface or modify the existing code into REST API to use it with any front-end client.


## Run Locally

Prerequisites

```bash
  Docker Desktop installed on your machine
```

Clone the repository

```bash
  git clone https://github.com/ShubhamJain0/chat-application.git
```

Go to the project directory

```bash
  cd chat-application
```

Build the image

```bash
  docker-compose build
```

Start the container

```bash
  docker-compose up
```


## Usage

Access application on this URL - 127.0.0.1 (Note: Alternatively you can use IPV4 of the network you are connected on to access this application from various devices. For this the device should be connected on the same network and you need to add the IPV4 in project -> settings.py -> Allowed Hosts )


## 🛠 Built with
Django(Python), Django-channels(extends Django's capability to handle asynchronous requests), Redis, WebSockets, Javascript and Docker.