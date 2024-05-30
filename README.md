# Overview
Rainfall-Data is a repository that contains scripts and data for analyzing rainfall patterns. The project includes fetching, consolidating, and structuring rainfall data in JSON format using a Python Flask API, which can be used for further analysis.

## Table of Contents
1.	Dataset and Setup
2.	Configuration
3.	How to Use
4.	Project Structure
5.	Data Description
6.	Contributing
7.	Acknowledgements

## Dataset and Setup

**Data Source:** ECAN Rainfall data

This dataset consists of rainfall measurements and details from different sites across the South Island of New Zealand. It's divided into two main regions:

**NORTH:** Sites observing rainfall north of the Rakaia River
**NORTH_URL:** https://data.ecan.govt.nz:443/data/51/Rainfall/Rainfall%20summary%20by%20area/JSON?Sites=NORTH&zip=1

**SOUTH:** Sites observing rainfall south of the Rakaia River
**SOUTH_URL:** https://data.ecan.govt.nz:443/data/51/Rainfall/Rainfall%20summary%20by%20area/JSON?Sites=SOUTH&zip=1

These data are refreshed hourly and contain the rainfall details for each site.

**Host IP:** 13.239.119.236
**Operating System:** AWS Ubuntu
**Type:** AWS EC2
**RAM:** 4 GB
**Disk:** 8 GB

Python should be installed on the host server along with the following packages/libraries: os, json, requests, zipfile, logging, datetime.

Additionally, install tmux to support session persistence and recovery even after disconnection.

### util.py
Developed to streamline the process and set up the pipeline for fetching and structuring data.

Steps:

1.	Download and Extract Data:

* Fetch rainfall data from specified URLs (as zip format).
* Extract JSON files from downloaded ZIP archives.
*Remove the zip files after extracting.

2.	Load and Structure Data:

*Check for existing data and, if not found, create a new rainfall_data.json in the data directory.
*Load the content of these files if they exist.

3.	Check and Update Data:
*Compare newly downloaded data with existing data.
*Update existing entries or add new entries as necessary.
*Log the number of new and updated items into data_update.log.

4.	Save Updated Data:

*Write the updated data back to the JSON file (rainfall_data.json), preserving the format and structure.

5.	Create rainfall_metadata.json:
*This file contains metadata about the dataset, including the specification of the columns, which helps in understanding the dataset.
**DATA_FILE:** data/rainfall_data.json
**METADATA_FILE:** data/rainfall_metadata.json







