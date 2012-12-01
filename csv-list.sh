#!/bin/sh

ls ./*.csv | egrep "[0-9]{3}_[pqrst]\.csv" | sed 's/\.\///g'
