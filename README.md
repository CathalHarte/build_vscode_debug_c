Generate Debug Tasks for VS Code
=================================
This repo is intended to be added as a submodule any time it is desired to debug C modules inside VS Code.

Instructions
------------
Add this repo as a submodule to the repo that you wish to debug on.

    cd ${REPO_ROOT}
    git submodule add git@github.com:CathalHarte/build_vscode_debug_c.git build_debug

Next create the file modules_list.txt at the ${REPO_ROOT}. Populate it with the names of the modules you want to debug. It is assumed that the modules to debug are contained in their own folders, and that folder_name = module_name = executable_name.

Effect
-------
The folder .vscode will be created at ${REPO_ROOT}, and two files along with it, launch.json and tasks.json. Be careful as the process will currently overwrite any pre-existing .json files. In VS Code the dropdown box "RUN AND DEBUG" found in the top corner of the "RUN AND DEBUG" page will be populated by the modules written in modules_list.txt.
