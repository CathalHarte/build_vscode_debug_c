#!/usr/bin/python3

# This creates vscode debug tasks by generating a .vscode folder,
# tasks.json file and launch.json file. The debug tasks (which are all unit tests)
# are generated based on the modules listed in modules_list.

import os

path = os.getcwd()

folder = path.split("/")
if folder[-1] != "build_test":
    raise Exception("script is being run out-of-directory, which is not supported")

target_path = path + "/../.vscode"
if not os.path.exists(target_path):
    try:
        os.mkdir(target_path)
    except OSError:
        raise Exception("Creation of the directory %s failed" % target_path)
    else:
        print ("Successfully created the directory %s " % target_path)


modules = []
with open('modules_list.txt', 'r') as modules_list:
    for _, module in enumerate(modules_list):
        # Remove newline
        module = module.split("\n")
        modules.append(module[0])

modules.sort()

for module in modules:
    print(module)


# start of launch.json
#####################################################################################################
lines = []

lines.append("{\n")
lines.append("    // Use IntelliSense to learn about possible attributes.\n")
lines.append("    // Hover to view descriptions of existing attributes.\n")
lines.append("    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387\n")
lines.append("    \"version\": \"0.2.0\",\n")
lines.append("    \"configurations\": [\n")
#####################################################################################################

for module in modules:

    lines.append("        {")
    lines.append("            \"name\": \"launch: debug %s\",\n" % module)
    lines.append("            \"type\": \"cppdbg\",\n")
    lines.append("            \"request\": \"launch\",\n")
    lines.append("            \"program\": \"${workspaceFolder}/%s/build/%s\",\n" % (module, module))
    lines.append("            \"args\": [],\n")
    lines.append("            \"stopAtEntry\": false,\n")
    lines.append("            \"cwd\": \"${workspaceFolder}/%s/build\",\n" % module)
    lines.append("            \"environment\": [],\n")
    lines.append("            \"externalConsole\": false,\n")
    lines.append("            \"MIMode\": \"gdb\",\n")
    lines.append("            \"setupCommands\": [\n")
    lines.append("                {\n")
    lines.append("                    \"description\": \"Enable pretty-printing for gdb\",\n")
    lines.append("                    \"text\": \"-enable-pretty-printing\",\n")
    lines.append("                    \"ignoreFailures\": true\n")
    lines.append("                }\n")
    lines.append("            ],\n")
    lines.append("            \"preLaunchTask\": \"build: %s\",\n" % module)
    lines.append("            \"miDebuggerPath\": \"/usr/bin/gdb\"\n")
    lines.append("        },\n")

# end of launch.json
#####################################################################################################
lines[-1] = lines[-1][0:-2] + "\n"
lines.append("    ]\n")
lines.append("}\n")
#####################################################################################################

# Create and fill the file.
file = open("../.vscode/launch.json", "w")
for line in lines:
    file.write( line )
file.close()

# start of tasks.json
#####################################################################################################
lines = []

lines.append("{\n")
lines.append("    // See https://go.microsoft.com/fwlink/?LinkId=733558\n")
lines.append("    // for the documentation about the tasks.json format\n")
lines.append("    \"version\": \"2.0.0\",\n")
lines.append("    \"tasks\": [\n")
#####################################################################################################

for module in modules:
    lines.append("        {")
    lines.append("            \"label\": \"build: %s\",\n" % module)
    lines.append("            \"type\": \"shell\",\n")
    lines.append("            \"command\": \"mkdir -p build; cd build; cmake -DCMAKE_BUILD_TYPE=Debug ..; make\",\n")
    lines.append("            \"options\": {\n")
    lines.append("                \"cwd\": \"${workspaceFolder}/%s\"\n" % module)
    lines.append("            },\n")
    lines.append("            \"problemMatcher\": {\n")
    lines.append("                \"base\": \"$gcc\",\n")
    lines.append("                \"fileLocation\": \"absolute\"\n")
    lines.append("            },\n")
    lines.append("            \"group\": {\n")
    lines.append("                \"kind\": \"build\",\n")
    lines.append("                \"isDefault\": true\n")
    lines.append("            }\n")
    lines.append("        },\n")

# end of tasks.json
#####################################################################################################
lines[-1] = lines[-1][0:-2] + "\n"
lines.append("    ]\n")
lines.append("}\n")
#####################################################################################################

# Create and fill the file.
file = open("../.vscode/tasks.json", "w")
for line in lines:
    file.write( line )
file.close()