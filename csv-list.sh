#!/bin/sh

ls ./*.csv | grep -e "[0-9]{3}_[pqrst]\.csv" | sed 's/\.\///g'
