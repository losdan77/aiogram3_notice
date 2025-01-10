#!/bin/bash


sleep 15


alembic upgrade head

python main.py