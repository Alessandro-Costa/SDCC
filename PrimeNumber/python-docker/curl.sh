#!/bin/sh
while getopts "n:s" opt; do
  case $opt in
    n) 
		echo "-n was triggere, Parameter: $OPTARG"   value=$OPTARG;;
  esac
done

exec curl -XPOST "http://localhost:9001/2015-03-31/functions/function/invocations" -d '{$value}'

