# Quickstart

This page describes how to set up the Data Science Project Template for local development.

This project template is in effect a hierarchy of configs that build containers based on the environment data science is being conducted in. At the bottom of that hierarchy is the local container that runs on a users local machine. This guide describes creating and developing inside the local container.

## Required Software

You will need the following applications installed on your local machine.

### Docker

Docker is the application that will run the local container. To install Docker desktop on a Windows or Mac please to the [official site](https://www.docker.com/products/docker-desktop/). There are alternatives such as [podman](https://podman.io/getting-started/), though the project has not been tested on this engine.

### For Windows Users: Windows Subsystem for Linux

If you are using a Windows machine, then you must additionally install [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/). Instructions on how to enable WSL with Docker on a windows machine can be found in the [official documentation](https://docs.docker.com/desktop/windows/wsl/).

### Optional: Visual Studio Code

Once you have installed Docker, it is highly recommended to install [vscode](https://code.visualstudio.com/). The config for the local container is structured according to the [devcontainer specification](https://containers.dev/implementors/spec/), and vscode has an extension ([Remote - Containers](https://code.visualstudio.com/docs/remote/remote-overview)) that is compatible with this spec.

Once vscode is installed, install the "Remote - Containers" extension as per the [instructions here](https://code.visualstudio.com/docs/remote/containers-tutorial#_install-the-extension).

If you are familiar with Docker and are happy to run the container from the command line, then vscode is not necessary.

### Optional: Installing Docker into a Linux Subsystem

At the time of writing (September 2022), Docker desktop is only available as free software for personal projects and organizations below a certain size. However, the docker engine can be freely installed on any linux machine.

To install the docker engine on a linux machine refer to the official documentation which explains how to install the docker engine on various distros, e.g., [Ubuntu](https://docs.docker.com/engine/install/ubuntu/). If you are running Windows or Mac and your organisation does not a license to use Docker desktop, you can still run the docker engine from within a virtual machine.

* [Docker Desktop pricing](https://www.docker.com/pricing/).
* [Running the docker engine in WSL](https://dev.to/bowmanjd/install-docker-on-windows-wsl-without-docker-desktop-34m9).
* [Running the docker engine on MacOS, both arm64 and x86 chips](https://medium.com/carvago-development/my-docker-on-macos-part-1-setup-ubuntu-virtual-machine-both-intel-and-apple-silicon-cpu-5d886af0ebba).

## Building a Local Development Container

### Persisting Command Line History

The main branch of the [Data Science Project Template repository](https://github.com/mark-curran/data-science-project-template) contains all the files you will need to start developing locally, bar one.

When developing inside the container, your bash history is kept in the file "/root/.bash_history" (by default the container runs as the root user, [this page](../reference/users_inside_container.md) explains some of the limitations of this approach). To prevent your history being destroyed when you rebuilt the container, this file is persisted to the file ".devcontainer/.bash_history" on the local machine. By default this file is part of the ".gitignore", and as such is not present in the main branch. 

If you would like to persist command line history between sessions, create an empty file ".devcontainer/.bash_history" before proceeding to build the container for the first time.

If you don't want your caommand line history to be preserved, then comment out [this line](https://github.com/mark-curran/data-science-project-template/blob/999d02b423f3cef22ec2a99f19dd207d69248537/docker-compose.yml#L18) in the `docker-compose.yml` file.

### Building and Running the Container

To build and connect to the container, open vscode and open the root folder of the Data Science Project Template repo. Make sure Docker Desktop is running.

If the _Remote - Containers_ extension is installed correctly, then you should be able to build the container by bringing up the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) and entering the command `Remote-Containers: Rebuild Container`.

### Optional: Storing code inside WSL

If you are using WSL then it is recommended that you further [store your code in WSL 2 filesystem](https://code.visualstudio.com/remote/advancedcontainers/improve-performance#_store-your-source-code-in-the-wsl-2-filesystem-on-windows).
