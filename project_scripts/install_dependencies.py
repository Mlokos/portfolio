#!/bin/bash
import subprocess
import os

install_ruby_sass = 'sudo apt install ruby-sass'

try:
    # pipe output to /dev/null for silence
    null = open("/dev/null", "w")
    subprocess.Popen("scss", stdout=null, stderr=null)
    null.close()
except OSError:
    print("scss not found")

    choice = input("install ruby-sass? [Y/n] ")
    if choice == 'Y':
        process = subprocess.Popen(install_ruby_sass.split(), stdout=null)
        output, error = process.communicate()
        print('Output: ', output, '\nError: ', error)
    else:
        print('Abort.')
