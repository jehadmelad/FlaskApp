# Simple Task tracker.
## The application is set with Authentication and API features.
* Log-in.
* Log-out.
* Signe-in.
* APIs
* ALChemy database.

## Requirements:

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

**NOTE :** In my case I created a docker `macvlan` to reach the container from my host.

The command to enable `macvlan`:
```
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

