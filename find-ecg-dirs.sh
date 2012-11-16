#!/bin/sh

find . -type d -maxdepth 1 |grep -e "[0-9][0-9][0-9]"|sed 's/\.\///g'|sort
