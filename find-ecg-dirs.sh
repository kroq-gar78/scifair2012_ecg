#!/bin/sh

find . -maxdepth 1 -type d |grep -e "[0-9][0-9][0-9]"|sed 's/\.\///g'|sort
