# Accessing Credentials

This page explains how to access credentials from inside the local container.

## Git credentials in a local environment

If you are using a [git credentials helper](https://git-scm.com/docs/gitcredentials) on the host machine, then VSCode will automatically forward git actions to the credentials helper for authenticating with the remote git repository.

Another common scenario is the use of ssh keys to authenticate. In this case, the [_Remote - Containeters_ documentation](https://code.visualstudio.com/docs/remote/containers#_using-ssh-keys) explains how ssh authentication can be made accessible from within the local container. In effect, one has to configure the `ssh-agent` on the host machine, after which VSCode makes a socket `SSH_AUTH_SOCK`  available from within the container.

## Credentials from other Providers

Accessing credentials on remotely hosted environments depends on how the remote host is configured, and how the provider's client libraries (e.g. python, cli,...) access those credentials.

Below are some links to resources that explain how with GCP or AWS credentials are accessed, along with examples for mounting those credentials on a container.

In a local environment, setting an environment variable or mounting a read only credentials file is sufficient. On remotely hosted environments, it is recommended to use the provider's language specific SDK to access credentials.

### GCP

* This [blog post](https://medium.com/google-cloud/use-google-cloud-user-credentials-when-testing-containers-locally-acb57cd4e4da) explains mounting the local machine's user credentials onto a container in a local environment.
* Note, that tor remote environments, Google recommends [authenticating using a client library](https://cloud.google.com/run/docs/securing/service-identity#per-service-identity) instead of an environment variable in the container.

### AWS

* Similarly to GCP, this [blog Post](https://prabhatsharma.in/blog/VSCode-dev-container-aws-credentials/) explains mounting credentials on a docker container in a local environment.
* Official [AWS advice](https://docs.aws.amazon.com/sdkref/latest/guide/feature-container-credentials.html) on credentials for containers running in an AWS remote environment. Like GCP, it's recommended to use a language specific
SDK to authenticate.
* Official [AWS deep dive](https://aws.amazon.com/blogs/containers/diving-into-iam-roles-for-service-accounts/) on using service account credentials for containers running on EKS.
