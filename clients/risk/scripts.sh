#!/bin/bash
# A script file for Google Colaboratory


:'
Setting-up
'
rm -rf data
rm -rf warehouse
rm -rf logs
mkdir data
mkdir warehouse
mkdir logs


: '
https://linux.die.net/man/1/wget
NOTE: This section is particular to a model being assessed
'
# Developed Model (and its trace series)
wget -q -P data https://github.com/exhypotheses/intermediaries/raw/develop/clients/risk/risk.zip


:'
Packages
'
pip install yellowbrick==1.3.post1 &> logs/yellow.log
pip install pymc3==3.11.2 &> logs/pymc3.log
pip install cloudpickle==1.6.0 &> logs/cloudpickle.log
pip install dask[complete]==2.30.0 &> logs/dask.log
pip install scikit-learn==0.24.2 &> logs/learn.log
pip install imbalanced-learn==0.8.0 >> logs/learn.log


:'
https://linux.die.net/man/1/unzip
'
rm -rf risk
unzip -u -q risk.zip
rm -rf risk.zip
