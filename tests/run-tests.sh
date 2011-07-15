#!/bin/bash

TSTS=`ls test-cases | grep test`

echo "" > test.log

for x in $TSTS; do
	echo $x
	./test-cases/$x >> test.log
	ret=$?
	if [ $ret -ne 0 ]; then
		echo "  FAIL!"
		FAIL_FLIP=Fsac
	else
		echo "  OK"
	fi
done 

rm *.testdb
rm -rf test-0.1

if [ "x$FAIL_FLIP" == "x" ]; then
	echo "No failures. Removing log."
	rm test.log
fi
