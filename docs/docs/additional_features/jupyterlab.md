# Jupyterlab

This document should explain how to setup jupyterlab.

## Port Mapping

Make reference to this:

* https://stackoverflow.com/a/46220742
* https://docs.docker.com/compose/compose-file/#ports

For a description of how the `--service-ports` option works.

* https://docs.docker.com/engine/reference/commandline/compose_run/

Command to get jupyter lab running:

`jupyter lab --port=8001 --ip 0.0.0.0 --no-browser --allow-root`