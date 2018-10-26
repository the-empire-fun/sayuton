#!/bin/bash

git clone https://github.com/habuka036/sayuton
cd sayuton/
git checkout develop
cd apps/
python manage.py runserver
