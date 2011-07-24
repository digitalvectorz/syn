#!/bin/bash

shopt -s extglob

rm -rf bash-4.2/!(synd)
tar -zcvf bash-4.2.syn.tar.gz bash-4.2
