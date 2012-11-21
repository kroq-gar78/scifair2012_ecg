#!/bin/sh

ls ./*.csv | grep -e "[0-9][0-9][0-9]" | sed 's/\.\///g'
