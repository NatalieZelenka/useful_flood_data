# Developer Guide

## Overview: how the map works

<!--TODO: rename master branch to main-->
<!--TODO: rename `docs` folder in this documentation and the directory itself to `map_site` -->

The map is built on [`folium`](http://python-visualization.github.io/folium/) - a Python package that lets you create leaflet.js maps (leaflet is a JavaScript package for creating maps) in Python.

The main code exists in a Python script (`create_map.py`) that creates html code for the map.
To make sure that we can change exactly what's on the map later (for example, based on feedback from the survey), `create_map.py` decides which data to read in using what we'll call the *data control* file `data_control.csv`.
The data control file contains information directing where within the folder structure of this project the `create_map.py` script should look for data files (such as icons or shape files), and how they should be displayed on the map (in terms of colour or size for example).

After reading in the information in the data control file and all the other data that it points to, `create_map.py` creates the map html. 
The map html is in `docs/index.html`: because this code has been generated from a Python script, it's not too nice to look at as code, but you can also look at it in your browser to check that it looks how you want it to.
After generating this html, we "host" it (i.e. make it available on the internet) using GitHub pages: GitHub pages makes everything that exists in a certain branch and/or folder of a GitHub repository available online.

### Directory structure

The directory structure needed to run the script (including files not tracked by git, i.e. large data files), is as follows:
.
├── [`.gitignore`](.gitignore) - tells git what not to track.
├── [`README.md`](README.md) - project info.
├── `CONTRIBUTING.md` - (you are here!) instructions for humans about how to run and edit this code.
├── [`LICENSE.md`](LICENSE.md) - software license.
├── _ `scripts/` 
│   ├── `process_flood_risk.py` - Was used to pre-process flood risk data (save risk levels as separate files).
│   ├── `create_map.py` - __Run this to create map html.__
│   └── `tif_to_geojson.py` - Experimental: not recommended (very slow).
├── _`data/`
│   ├── `data_control.csv` - __Tells `create_map.py` what data to use__: other data is untracked by git (too big).
│   ├── _ `flood_hazard/` - flood hazard information (geopackage and tif files)
│   │   ├── `flood_binary/` 
│   │   ├── `flood_depth/`
│   │   └── `flood_risk/`
│   └── _`humanitarian/` - locations of humanitarian resources (shapefiles)
│       ├── `airports/`
│       ├── `city/`
│       ├── `airports/`
│       └── etc 
├── _ `docs/` - Contains anything to display on website
│   ├── `index.html` - generated map html
│   └── `pngs/` - converted from tif files
│   └── `icons/` - humanitarian icons .svg files
└── `images/` - misc images (e.g. project image)


### Data control file structure

The structure of the data control file (i.e. the meanings of the headings) is as follows:

The first row is a header row containing column names, while the second row contains column descriptions.
They are also here for ease:

|Column name | Column Description |
|--|--|
| file_path | The path to the file, from the root of the ""Flood User"" google drive |
| data_name | As short as possible identifier for the data, to show in the key (where you select/deselect the layer) and the colour bar label |
| description | A short sentence describing the data, which may, for example be used in a tool tip |
| data_type | E.g. Integer, continuous, binary, Vector Point, etc. |
| info_type | The way in which the information will be displayed on the map, e.g. marker, polygon, line | 
| units | Units of the data_type, e.g. metres, use a full stop for unitless | 
| data_label| To show on colourbar ticks | 
| icon | Path to icon file, e.g. `icons/city-15.svg` | 
| colour| in hex code | 
| colour_description | | 
| thickness| line thickness in points | 
| info| additional notes (for humans only, not used by script) | 


## How-tos

<!--TODO: write setup-->
<!--
### Setup

1. Clone GitHub
2. Download Data 
3. 
-->

### How-to generate the map html

To generate the map html, you must run the `create_map.py` script.
You can do this from the terminal, by typing:

```bash
python3 create_map.py
```

To check the map that you've created, open the created index file in a browser:
```bash
open docs/index.html
```

## Uploading the map html to GitHub pages
<!-- TODO: set up a more sensible way of doing this and update instructions.-->
Only after you are happy with the created map, it's time to upload it to GitHub pages so that other people can see the version that you have created. 

Everything that is in the `docs` folder of the main branch will be live on the site. 
Submit a Pull Request to the repository, and it will be merged.
Images that are shown on the map must be included in the `docs` folder (such as icons or pngs). 
Otherwise the website will not be able to find them.

<!-- TODO: write how to add new features.-->
<!--
## How to add new features to the map

### Editing an icon colour

### Editing a line colour

### New feature, but similar to existing features
1. Edit the data control file
2. Edit the data control dictionary file 

### Completely new feature
-->