#!/bin/bash

echo '=============================  Troubleshooter Output ==============\n'
echo '****************************** Original PYTHON PATH ***************'
echo $PYTHONPATH
echo
echo '\****************************** Orig LD_LIBRARY_PATH **************'
echo $LD_LIBRARY_PATH
echo '***************************** Orig .bashrc **********************'
cat ~/.bashrc
echo '***************************** Ubuntu Version ********************'
lsb_release -a
echo '***************************** python version ********************'
python -V
echo '***************************** python Shared Objects *************'
ls /usr/local/share/opencog/python/opencog
echo '***************************** spockbot eggs *********************'
ls /usr/local/lib/python2.7/dist-packages | grep 'mine\|spock'
echo '***************************** python sys.path *******************'
python -c 'import sys; print sys.path'
echo '***************************** Common Imports test ***************' 
python -c 'from opencog.spacetime import SpaceTimeAndAtomSpace; from opencog.spatial import get_near_free_point; from spockbot.plugins.base import pl_announce'

