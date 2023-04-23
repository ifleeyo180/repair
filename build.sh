#!/bin/bash

pip install --upgrade pip

pip install -r requirements.txt

if [[ $CREATE_SUPERUSER ]];
then
  python world_champ_2022/manage.py createsuperuser --no-input
fi