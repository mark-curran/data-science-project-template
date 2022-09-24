# Using mkdocs

This page explains how to use [mkdocs](https://www.mkdocs.org/) to build project documentation. mkdocs converts collections of markdown files into a website. The developer writes the documentation in a series of markdown files, and writes a single configuration file. In particuarl, the developer does not have to write the html code of the documentation website.

In this page, we explain creating documentation using files that are in the `docs/` folder of the main branch of the template repository. The setup of the documentation in this project is not supposed to be prescriptive, but rather to explain a possible documentation solution.

## Building mkdocs Locally

If you are unfamiliar with mkdocs, we recommend reading [the official tutorial](https://www.mkdocs.org/getting-started/).

To host documentation locally you will need to install the mkdocs python package in the local environment and make sure the appropriate port is forward from your container to the host machine.

First, make sure a port is exposed on your container by uncommenting the relevant part of the [`docker-compose.yml` file](https://github.com/mark-curran/data-science-project-template/blob/main/docker-compose.yml) and rebuilding the container. The choice of port 8000 is arbitrary.

To install the mkdocs package, navigate to the `docs/` directory and run the command

`pip install -r docs-requirements.txt`

To build the documentation website and begin hosting it, run the command:

`mkdocs serve -a 0.0.0.0:8000`

This will build the docs website and host it in port 8000 _inside the container_. If this port has been forwarded correctly, then opening `localhost:8000` in a web browser should load the documentation website.

## Publishing Docs on GitHub

GitHub offers limited amounts of free documentation hosting through [github pages](https://pages.github.com/). You can manually push to GitHub pages by following the instructions in the [mkdocs documentation](https://www.mkdocs.org/user-guide/deploying-your-docs/#github-pages).

You can also setup a [GitHub Action](https://github.com/features/actions) to automatically deploy documentation upon merges into a specific branch of the repsoitory. For this project, documentation is deployed upon merges into the `main` branch.

For further information on setting up a GitHub action to deploy documentation, see [this post](https://parkererickson.github.io/portfolio/blog/MkDocsCD/), and the [corresponding file](https://github.com/mark-curran/data-science-project-template/blob/main/.github/workflows/deploy-gh-pages.yml) in the Data Science Template respository.
