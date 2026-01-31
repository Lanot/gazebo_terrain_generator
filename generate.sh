#!/bin/bash

#pip install -r requirements.txt
#python3 -m venv terrain_generator
cur_dir=$(dirname "$(realpath $0)")

source terrain_generator/bin/activate
pip install -r requirements.txt

export GAZEBO_MODEL_PATH="$cur_dir/output/gazebo_terrain/models"
export GAZEBO_WORLD_PATH="$cur_dir/output/gazebo_terrain/worlds"
mkdir -p $GAZEBO_MODEL_PATH
mkdir -p $GAZEBO_WORLD_PATH

# Uncomment the line below and add your API KEY, or add the line to ~/.bashrc for permanent store
# export MAPBOX_API_KEY="Personal API Key"
export GAZEBO_WORLD_GENERATOR_MERGE_TERRAIN_TILES=0

python scripts/generate.py
