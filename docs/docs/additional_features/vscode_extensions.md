# VSCode Extensions and Settings

This page explains how to leverage VSCode extensions and settings.

## Installing Extensions

[VSCode extensions](https://code.visualstudio.com/docs/editor/extension-marketplace) add additional features to the editor. In the [quickstart guide](../quickstart/quickstart.md#optional-visual-studio-code), we installed the VSCode _Remote - Containers_ extension. Additional extensions will be instaleld automatically when the local contianer is built.

To specify which extensions are installed, you can add the extension id to the `devcontainer.json` as specified in the [devcontain.json reference](https://containers.dev/supporting), under the propery `"customizations": "vscode": "extensions"`. You can [use the VSCode UI](https://code.visualstudio.com/docs/editor/extension-marketplace#_command-line-extension-management) to find an extension's id. Moreover, extensions can be selected through the VSCode UI and added to the `devcontainer.json` file through the [VSCode UI](https://code.visualstudio.com/docs/remote/containers#_managing-extensions).

In addition, you can specify general VSCode settings under the propery `"customizations": "vscode": "settings"`. In particular, you can specify extension settings.

### Extension Locations

The final piece of information to be specified is where the extension will run; either in "ui" (i.e. the host machine) or "workspace"(inside the container). Not all extensions have the flexibility to run in both, and running in the "ui" reduces latency. However, if latency is not an issue and the extension supports it, then it's recommended to install the extension in "workspace" so that any binaries the extension requires are not installed in the host machine's default environment.

To specify a running location edit the property `"remote.extensionKind"` as explained in the [official documentation](https://code.visualstudio.com/docs/remote/containers#_advanced-forcing-an-extension-to-run-locally-or-remotely). A more detailed explanation is provided in [VSCODE API documentation](https://code.visualstudio.com/api/advanced-topics/extension-host#preferred-extension-location).

### Installing binaries

In order for an extension to run, it may require the installation of additional packages. Separating out these packages from the packages needed to run the Data Science project itself, is one of the main reasons behind [separating local development from dev and prod environments](../design/design.md#environments-in-a-data-sciene-project).

If additional python packages are required, then they must be added to the [local requirements file](https://github.com/mark-curran/data-science-project-template/blob/main/.devcontainer/local-requirements.txt). See the section on [editing the requirements file](../additional_features/editing_requirements.md) for more information.

## Changing Extension Settings

### Rebuilding container after changing devcontainer.json

You can add additional extension settings by creating and editing the file `.vscode/settings.json`. This file is not git tracked.

Moreover, any changes to extension settings in the `devcontainer.json` file are not enacted until the container is rebuilt.

Alternatively, on can install extensions on the [local host and mount them on the container](https://code.visualstudio.com/remote/advancedcontainers/avoid-extension-reinstalls).

### Note Jupyter always installed locally

As of September 2022, the Jupyter extension will always be installed when the python extension is. See [this GitHub issue](https://github.com/microsoft/vscode-jupyter/issues/5520) for further information. If you would like to uninstall jupyter after building the local container, run the command

`code --uninstall-extension ms-toolsai.jupyter`

Note, one cannot rely on using the [Lifecycle Scripts](https://containers.dev/implementors/json_reference/#lifecycle-scripts) because these trigger before vscode starts installing extensions.

## Data Science Project Template Default Extensions

The Data Science Project Template main branch includes the id and settings for several extensions that are useful in the development of a Data Science application, though like most of the template this reflects personal taste and is not supposed to be prescriptive.

These extensions are:

* **RunOnSave:** The [RunOnSave extension](https://marketplace.visualstudio.com/items?itemName=emeraldwalk.RunOnSave) coordinates commond line actions that are taken upon file save. Different commands are run depending on the file extension.
* **Python:** The default python extension provided by Microsoft. The settings file uses mostly default values, with a few exceptions. The main configuration decisions are:

    * [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) is the language server. Problems identified by pylance appear in the _PROBLEMS_ tab in the VSCode UI.
    * [pylint](https://pylint.pycqa.org/en/latest/) and [pydocstyle](http://www.pydocstyle.org/en/stable/) are enabled. Problems identified by these static code checkers appear in the _PROBLEMS_ tab in the VSCode UI.
    * [autoDocstring](https://github.com/NilsJPWerner/autoDocstring) is enabled and provides shortcuts to generate `google` style docstrings.
    * Upon save, both [isort](https://pypi.org/project/isort/) and [black](https://pypi.org/project/black/) are run on all python files. Moreover notifications raised by pylance, pylint and pydocstyle are also refreshed.
    * All code checkers will ignore unresolved imports. This is because heavyweight libraries should be [installed in a dev and prod environments](../design/design.md#environments-in-a-data-sciene-project), the local environment should be as lightweight as possible.
    * Telemetry is disabled.
    * [VSCode UI for unit testing](https://code.visualstudio.com/docs/python/testing) are disabled. Tests can be run from [the command line](../additional_features/unit_tests.md).
    * Rulers are drawn at 79 and 99 characters as a visual guide to stay within the [pep8 recommended line length](https://peps.python.org/pep-0008/#maximum-line-length).
    * Requirements files are [automatically sorted](https://github.com/rehandalal/sort-requirements).

* **SQLFluff:** [SQLFluff]([https://www.sqlfluff.com/) is run on every file with an sql extension upon file save. You must specify a dialect in the RunOnSave command.
* **VSCode:** Several settings are also imposed on the VSCode editor. These can be overwritten in the `devcontainer.json` file, or by adding `.vscode/settings.json` file to the local repository.

    * Quick suggestions are disabled.
    * Popups with recommended extensions are disabled.
    * The [Cobalt2 theme](https://marketplace.visualstudio.com/items?itemName=wesbos.theme-cobalt2) is the default color theme.

* **Markdown Lint:** Markdown files are automatically linted with an indent set to `4` by [Markdown Lint](https://github.com/DavidAnson/markdownlint).
* **TODO Tree:** Keep track of `TODO` statements using [TODO tree](https://github.com/Gruntfuggly/todo-tree).

## Links

* Settings for the [VSCode python extension](https://code.visualstudio.com/docs/python/settings-reference).
* Settings for the [VSCode editor](https://code.visualstudio.com/docs/getstarted/settings#_settingsjson).
