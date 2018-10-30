#!/bin/bash
echo "export GM_ANALYTICS=/usr/local/lib/python3.6/site-packages/gm_analytics/swagger/indexer.yaml" >> ~/.bashrc
pip3.6 install -r /usr/lib/python3.6/site-packages/gm_analytics-*-py3.6.egg-info/requires.txt
# export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.6/site-packages/
# connexion run $GM_ANALYTICS --verbose -p 8088
