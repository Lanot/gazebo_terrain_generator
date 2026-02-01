#!/usr/bin/env python

import os
from utils.demTilesDownloader import download_dem_data
from utils.gazebo_world_generator import GazeboTerrianGenerator
from utils.maptile_utils import maptile_utiles
from utils.param import globalParam

if __name__ == '__main__':
    bounds = '-74.02862548828125,40.682720875945506,-74.01214599609375,40.695216613517154'
    outputDirectory = 'usa_ny_governors_island'
    outputFile = '{z}/{x}/{y}.png'
    zoom_level = 17
    timestamp = '1769886925501'
    bounds = list(map(float, bounds.split(",")))

    true_boundaries = maptile_utiles.get_true_boundaries(bounds, zoom_level)
    download_dem_data(true_boundaries, os.path.join(globalParam.OUTPUT_BASE_PATH, "dem"))
    orthodir_path = os.path.join(globalParam.OUTPUT_BASE_PATH, outputDirectory)
    terrian_generator = GazeboTerrianGenerator(orthodir_path, merge_ortho_column_tiles=globalParam.MERGE_ORTHO_COLUMN_TILES)
    terrian_generator.generate_gazebo_world()

    print("Gazebo world generation completed successfully.")
