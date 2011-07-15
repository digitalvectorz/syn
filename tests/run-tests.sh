#!/bin/bash

TSTS=`ls test-cases | grep test`

echo "" > test.log

for x in $TSTS; do
	echo -n "$x"
	./test-cases/$x >> test.log
	ret=$?
	if [ $ret -ne 0 ]; then
		echo "	[ [31mFAIL![0m ]"
		FAIL_FLIP=Fsac
	else
		echo "	[ [34mOK[0m ]"
	fi
done 

rm *.testdb
rm -rf test-0.1

if [ "x$FAIL_FLIP" == "x" ]; then
	echo "No failures. Removing log."
	rm test.log
fi
