# VSCode Extensions and Settings

This page explains how to leverage VSCode extensions and settings.

## Various Personal Preferences

Here are all the minor personal preferences I use in vscode:

## Rebuilding container after changing devcontainer.json

## Note Jupyter always installed locally

See [this GitHub issue](https://github.com/microsoft/vscode-jupyter/issues/5520). Have to manually run

`code --uninstall-extension ms-toolsai.jupyter`

Cannot rely on using the [Lifecycle Scripts](https://containers.dev/implementors/json_reference/#lifecycle-scripts) because these execute before vscode starts installing extensions.

Alternatively, install extensions on the [local host and mount them on the container](https://code.visualstudio.com/remote/advancedcontainers/avoid-extension-reinstalls).

## Other extensions to consider

Make reference to this:

<https://code.visualstudio.com/docs/remote/containers#_managing-extensions>
And maybe this: <https://code.visualstudio.com/docs/python/settings-reference>
and this: <https://code.visualstudio.com/docs/getstarted/settings#_settingsjson>
