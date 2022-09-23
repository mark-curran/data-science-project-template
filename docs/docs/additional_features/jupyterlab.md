# Jupyterlab

[Jupyterlab](https://jupyterlab.readthedocs.io/en/stable/index.html#) is a web-based development environment that is particularly useful for data manipulation and visualization in python.

This page explains how to setup Juypyterlab, i.e., the jupyterlab server, in the dev environment. It is strongly recommended to read the section on port mapping below before starting the server.

## Starting the dev container

Start the `dev` service on the machine that will host the jupyter server

`docker-compose run -it --service-ports dev /bin/bash`

Jupyterlab creates notebook files, and it is convenient to run the command to start the server from the folder where you want to store these files. For example, to store your notebooks in `dev/notebooks`, run this command

`cd /workspaces/dev/notebooks`

Note that the root of the repository is `/workspaces` inside the dev environment.

From here start the server by running

`jupyter lab --port=8001 --ip 0.0.0.0 --no-browser`

or if you are running as root inside the container

`jupyter lab --port=8001 --ip 0.0.0.0 --no-browser --allow-root`

A message should print to the terminal with a URL from which can access the server, for example

`http://127.0.0.1:8001/lab?token=`

followed by a long string of characters. These characters are the token that permits access to the server, and by extension the host machine. **Do not share the token with people who should not have access to the host machine.**

You can detach from the container by pressing the [detach keys sequence](https://docs.docker.com/engine/reference/commandline/attach/#options) for your system (the default is `CTRL-p CTRL-q`).

## Port Mapping

By starting the jupyter lab server, you give any user direct access to the host. Therefore, it is important to consider
who can access the host's ip address before starting the server.

You can specify the host ip address and the port to expose, as explained in the [docker-compose specification](https://docs.docker.com/compose/compose-file/#ports).

Note, that by default docker-compose will [not expose ports when running a container](https://docs.docker.com/engine/reference/commandline/compose_run/), hence when ports are specified in the compose file, then the argument `--service-ports` must also be passed.

## Managing extensions and configs

It is possible to standardize the behavior of Jupyterlab across a wider team by mounting jupyter configs on the host machine. The jupyter documentation lists [common directories and file locations](https://docs.jupyter.org/en/latest/use/jupyter-directories.html) that one could leverage.
