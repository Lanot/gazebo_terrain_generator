#!/bin/bash

#pip install -r requirements.txt
#python3 -m venv terrain_generator
cur_dir=$(dirname "$(realpath $0)")

source terrain_generator/bin/activate
pip install -r requirements.txt


export GAZEBO_WORLD_PATH="$cur_dir/gazebo/worlds"
export GAZEBO_MODEL_PATH="$cur_dir/gazebo/worlds/models"

mkdir -p $GAZEBO_WORLD_PATH
mkdir -p $GAZEBO_MODEL_PATH

# export MAPBOX_API_KEY=""

python scripts/server.py
