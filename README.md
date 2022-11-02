# Simple Task tracker.

## The application is set with Authentication and API features.
* Log-in.
* Log-out.
* Signe-in.
* APIs
* ALChemy database.

## Requirements:

```
Package          Version
---------------- -------
click            8.1.3
Flask            2.2.2
Flask-Login      0.6.2
Flask-SQLAlchemy 3.0.2
greenlet         2.0.0
itsdangerous     2.1.2
Jinja2           3.1.2
MarkupSafe       2.1.1
pip              22.3
setuptools       63.2.0
SQLAlchemy       1.4.42
Werkzeug         2.2.2
wheel            0.37.1
```

* Python +3.x.x.

## Run the application.

It is a good habit to run the application within python virtual environment. By following the next structure you will be able to do so.


install python virtual environment 'virtualenv' using pip:
```
pip3 install virtualenv 
```

Go to the folder that you would like to work in (In this case: /FlaskApp), then create an virtual environment by:
```
virtualenv <name-you-would-like>
```

Now, try to install the required packeage for this application.
```
c:/users/hp/documents/folder/FlaskApp/:~ pip3 install -r requiremnets.txt
```

Finally, open your browser and write the `localhost:5001` or your `ip addres:5001`.


## Run by Docker:

### Install Docker on Ubuntu:
```
~: apt-get install docker.io

# Check docker if installed.
~: docker --version

```

### Run the `docker-compose` within the directory `/FlaskApp`:
```
/FlaskApp~: docker-compose up
```

## Issues: NOTE :
In my case, I created a docker `macvlan` to reach the container from my host.

The command to enable `macvlan`:
```

# The ip of macvlan needs to be same as the parent interface
~: docker network create -d macvlan --subnet <your-subnet-range>  --gateway <you-gateway> --ip-range <range-of-container-ip> -o parent=<interface-name> <name-of-network>

# To get the name of interface on your PC
~:ip addr
.
...
1: ens37: ....
...
```

Finally, you will be able to run the server as shown:


[app.webm](https://user-images.githubusercontent.com/37592486/187088989-28fe3216-cfa4-47dc-8174-bdcf085c82d0.webm)

