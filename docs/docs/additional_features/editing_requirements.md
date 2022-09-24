# Editing a Requirements File

The requirements file contains a complete list of all python packages needed for an environment to run.

## Commands to Edit a Requirements

If you would like to add a package to an environment, first install the package using the command

`pip install <package_name>`

This will add the package to the evironment's python installation. One can also remove packages using the `pip uninstall` command. To automatically install these packages next time the container is built, you will need to update the requirements file. To produce the updated package list in the format required, run the command

`pip freeze`

and paste its output into the requirements file.
