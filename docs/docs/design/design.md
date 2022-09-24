# Project Design

This project was designed to integrate with the environments one encounters in a typical data science project. The definitions of said environments, and whether the default settings of the template address them, is of course open to debate. That said, the template design can be used as a starting point, and is not intended as a one size fits all solution.

## Environments in a Data Sciene Project

Though a data science project can have the same phases (data exploration, model design,...) that one finds in any explanation of a DevOps or MLOps workflow, usually there are three distinct environments one works with.

Given the different purposes of these environments, it makes sense to have different configurations to address them. In this project, each environment corresponds to a different docker compose file.

### Local Development

The users local machine, containing source code, git configurations, code linters and checkers. Running elsewhere on the local machine there is probably a service for managing the users [personal credentials](../additional_features/accessing_credentials.md). A local machine might have network and resource constraints, which makes it inappropriate for large scale data processing.

### Dev Development

A remote environment with access to relevant data. This environment would need access to any relevant data manipulation of ML libraries, e.g., numpy, tensorflow, etc. Packages for debugging, logging and telemetry might be required. Depending on data access permissions, it might make sense to mount the credentials of a service account on this machine.

### Staging/Production

A remote environment identical to production. This environment might be used for testing prior to final deployment or might be production itself. Only the necessary packges are installed in this environment, and personal credentials should certainly not be used to access services.

## Configurations

### local

The local config is stored in the [`.devcontainer` folder](https://github.com/mark-curran/data-science-project-template/tree/main/.devcontainer). As per the [devcontainer specification](https://containers.dev/implementors/spec/), the file `devcontainer.json` configures the local environment by starting the `local` service in the file `docker-compose-local.yml` and installing requirements from `requirements-local.txt`.

By default the main branch of the repository contains a number of VSCode extensions that are relevant to local development, including

* [An uncompromising python code formatter](https://github.com/psf/black).
* A [SQL formatter](https://docs.sqlfluff.com/en/stable/index.html) that works with multiple dialects,  in particular, multiple cloud providers.
* Several [python static code checkers](../additional_features/vscode_extensions.md#data-science-project-template-default-extensions).

### dev

The dev config is stored in the [`dev` folder](https://github.com/mark-curran/data-science-project-template/tree/main/dev). Start the `dev` service in `docker-compose-dev.yml` which installs the requirements `requirements-dev.txt`.

By default the main branch of the repository contains a number of packages that are relevant to dev development.

* Exploratory data analysis and visualizations using [Jupyterlab](https://jupyterlab.readthedocs.io/en/stable/index.html).
* Data manipulation using [pandas](https://pandas.pydata.org/).

Further information on using Jupyterlab on remote machine is provided in [this page](../additional_features/jupyterlab.md).

### prod

Finally, the prod config is stored in the [root folder of the repository](https://github.com/mark-curran/data-science-project-template). Start the `prod` service in `docker-compose.yml` which installs the requirements `requirements-prod.txt`.
