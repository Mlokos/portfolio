#!/bin/bash
import subprocess
import os

octicons_repo = '../octicons'
scripts_dir = '../project_scripts'
update_repo = 'git pull'

os.chdir(octicons_repo)

process = subprocess.Popen(update_repo.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print('Output: ', output, '\nError: ', error)

os.chdir(scripts_dir)
