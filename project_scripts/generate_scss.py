#!/bin/bash
import subprocess
import os

scss_dir = '../scss'
scripts_dir = '../project_scripts'
generated_css = '../generated_css'
generate_scss = 'scss ' + scss_dir + '/introduction.scss' + ' ' + generated_css + '/introduction.css'

process = subprocess.Popen(generate_scss.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print('Output: ', output, '\nError: ', error)