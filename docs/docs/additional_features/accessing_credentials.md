# Accessing Credentials

This page explains how to access credentials inside the container.

## Git credentials in local environment

Git credentials in local environment using ssh-agent or the vscode remote extensions package.

### Starting ssh-agent on the host machine

Script to run ssh agent locally.

## Credentials from other Providers

Accessing credentials on remotely hosted environments depends on how the remote host is configured, and how
the provider's clients (e.g. python, cli,...) access those credentials.

Below are some links to resources that explain how provider credentials are accessed, along with example
for mounting those credentials on a container.

### GCP

* [Blog post](https://medium.com/google-cloud/use-google-cloud-user-credentials-when-testing-containers-locally-acb57cd4e4da) on mounting the local machine's user credentials onto a container in a local environment.
* Note, that tor remote environments, Google recommends using [authenticating using a client library](https://cloud.google.com/run/docs/securing/service-identity#per-service-identity) instead of an environment variable in the container.

### AWS

* Similarly to GCP, a [Blog Post](https://prabhatsharma.in/blog/vscode-dev-container-aws-credentials/) on mounting your credentials on a docker container in a local environment.
* Official [AWS advice](https://docs.aws.amazon.com/sdkref/latest/guide/feature-container-credentials.html) on credentials for containers running in an AWS remote environment. Like GCP, it's recommended to use language specific
SDK to authenticate.
* Official [AWS deep dive](https://aws.amazon.com/blogs/containers/diving-into-iam-roles-for-service-accounts/) on using service account if the remote environment is EKS.
