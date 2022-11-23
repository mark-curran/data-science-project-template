# Running Docker Containers as a non-root User

This document explains some of the difficulties of using a container as a non-root user, and provides links to resources for changing the default container user.

## Dangers of running as a non-root user

[It is recommended that you run docker containers as a non-root user](https://www.howtogeek.com/devops/why-processes-in-docker-containers-shouldnt-run-as-root/) because it could be that the docker daemon is performing operations on the host machine with the same privelages as the container user. If that user is root, then the container can become a conduit for exploiting security flaws in the host system.

## Changing the Container User

### Local Environment

The [_Remote - Containers_ documentation](https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user) provides some information on using a non-root user to build the container in the local environment.

### Other Environments

It is recommended to [add any container users to the Dockerfile](https://docs.docker.com/compose/compose-file/#user). Further information on these commands can be found in the [official dockerfile documentation](https://docs.docker.com/engine/reference/builder/#user).
