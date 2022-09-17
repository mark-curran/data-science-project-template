# Project Design

This project was designed to integrate with the environments one encounters in a typical data science project. The definitions of said environments, and whether the default settings of the template address them, is of course open to debate. That said, the template design can be used as a starting point, and is not intended as a one size fits all solution.

## Environments in a Data Sciene Project

Though a data science project can have different phases (data exploration, model design,...) that one finds in any explanation of a DevOps or MLOps workflow, usually there are three distinct environments one works with.

Given the different purposes of these environments, it makes sense to have different configurations to address them. In this project, each environment corresponds to a service within the [docker compose file](https://github.com/mark-curran/data-science-project-template/blob/main/docker-compose.yml).

### Local Development

The users local machine, containing source code, git configurations, code linters and checkers. Running elsewhere on the local machine there is a service for managing the users personal credntials. A local machine might be resource constrained, so this environment should be lightweight.

### Dev Development

A remote environment with access to relevant data. It may not make sense to pipe large quantities of data to a local machine, but on the other hand, it may not make sense to use a remote machine to upload personal credentials to this machine. This environment would need access to any relevant data manipulation of ML libraries, e.g., numpy, tensorflow, etc. Packages for debugging, logging and telemetry might be required.

### Staging/Production

A remote environment identical to production. This environment might be used for testing prior to final deployment or might be production itself. Only the necessary packges are installed in this environment.


## Configurations

### local

The local config is stored in the `.devcontainer` folder. As per the [devcontainer specification](https://containers.dev/implementors/spec/), the file `.devcontainer.json` configures the local environment by starting the `local` service in the [docker compose file](https://github.com/mark-curran/data-science-project-template/blob/main/docker-compose.yml) and by configuring any vscode extensions.

By default the main branch of the repository contains a number of vscode extensions that are relevant to local development.

* [An uncompromising python code formatter](https://github.com/psf/black).
* A [SQL formatter](https://docs.sqlfluff.com/en/stable/index.html) that works with multiple dialects,  in particular, multiple cloud providers.

The default [requirements file](../additional_features/editing_requirements.md) for this environment is `.devcontainer/local-requirements.txt`.

### dev

The dev environment is created by running the `dev` service in the [docker compose file](https://github.com/mark-curran/data-science-project-template/blob/main/docker-compose.yml). Its [requirements file](../additional_features/editing_requirements.md) is `dev/dev-requirements.txt`.

By default the main branch of the repository contains a number of packages that are relevant to dev development.

* Exploratory data analysis and visualizations using [Jupyterlab](https://jupyterlab.readthedocs.io/en/stable/index.html).
* Data manipulation using [pandas](https://pandas.pydata.org/).

### prod

The prod environment is created by running the `prod` service in the [docker compose file](https://github.com/mark-curran/data-science-project-template/blob/main/docker-compose.yml). Its [requirements file](../additional_features/editing_requirements.md) is `prod-requirements.txt`.

By default the main branch of the repository contains only the packages that might be relevant in a production setting.

* Data manipulation using [pandas](https://pandas.pydata.org/).
* The [python kafka client](https://github.com/dpkp/kafka-python).
