#!/bin/bash -e

BOOST_DIR=${HOME}/dev/lib/boost_1_33_1/
YASMIC_DIR=.

CCFILES="components.cc max_flow.cc orderings.cc searches.cc shortest_path.cc
spanning_trees.cc statistics.cc"
OFILES=`echo ${CCFILES} | sed -e 's/\.cc/\.o/g'`

CFLAGS="-O2 -c -I${BOOST_DIR} -I${YASMIC_DIR}"

function echocmd {
	echo $@
	$@
}

for file in ${CCFILES}; do
	echocmd g++-3.4 $CFLAGS $file
done

echocmd ar rc libmbgl-linux-32.a ${OFILES} 
	
echocmd rm ${OFILES}	
