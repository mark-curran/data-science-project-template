# Quickstart

This page describes a quick way to get up and running with the Data Science Project Template for local development.


This project template is in effect a hierarchy of configs that build containers based on the environment data science is being conducted in.

At the bottom of that hierarchy is the local container that runs on a users local machine. This guide describes creating and developing inside the local container.

## Required Software

You will need the following applications installed on your local machine.

### Docker

Docker is the application that will run the local container. To install Docker desktop on a Windows or Mac please to the [official site](https://www.docker.com/products/docker-desktop/).

### For Windows Users: Windows Subsystem for Linux

If you are a Windows user then you must additionally install [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/). Instructions on how to enable WSL with Docker on a windows machine can be found in the [official documentation](https://docs.docker.com/desktop/windows/wsl/).

### Visual Studio Code

Once you have installed Docker, it is highly recommended to install [vscode](https://code.visualstudio.com/). The config for the local container is structured according to the [devcontainer specification](https://containers.dev/implementors/spec/), and vscode has an extension ([Remote - Containers](https://code.visualstudio.com/docs/remote/remote-overview)) that is compatible with this spec.

Once vscode is installed, install the "Remote - Containers" extension as per the [instructions here](https://code.visualstudio.com/docs/remote/containers-tutorial#_install-the-extension).

## Building a Local Development Container

### Persisting Command Line History

The main branch of the [Data Science Project Template repository](https://github.com/mark-curran/data-science-project-template) contains all the files you will need to start developing locally, bar one.

When developing inside the container, your bash history is kept in the file "/root/.bash_history". To prevent your history being destroyed when you rebuilt the container, this file is persisted to the file ".devcontainer/.bash_history" on the local machine. By default this file is part of the ".gitignore", and as such is not present in the main branch. 

If you would like to persist command line history between sessions, create an empty file ".devcontainer/.bash_history" before proceeding to build the container.

### Building and Running the Container

To build and connect to the container, open vscode and open the root folder of the Data Science Project Template repo. Make sure Docker Desktop is running.

If the Remote - Containers extension is installed correctly, then you should be able to build the container by bring up the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) and entering the command "Remote-Containers: Rebuild Container".

### Optional: Storing code inside WSL

If you are using WSL then it is recommended that you further [store your code in WSL 2 filesystem](https://code.visualstudio.com/remote/advancedcontainers/improve-performance#_store-your-source-code-in-the-wsl-2-filesystem-on-windows).
