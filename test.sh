#!/bin/bash

#pip install -r requirements.txt
#python3 -m venv terrain_generator
cur_dir=$(dirname "$(realpath $0)")

export GZ_SIM_RESOURCE_PATH="$GZ_SIM_RESOURCE_PATH:$cur_dir/sample_worlds"
export GZ_SIM_RESOURCE_PATH="$GZ_SIM_RESOURCE_PATH:$cur_dir/output/gazebo_terrain/models"
export GZ_SIM_RESOURCE_PATH="$GZ_SIM_RESOURCE_PATH:$cur_dir/output/gazebo_terrain/worlds"

gz sim usa_ny_governors_island.sdf