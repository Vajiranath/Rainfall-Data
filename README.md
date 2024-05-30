# Overview
Rainfall-Data is a repository that contains scripts and data for analyzing rainfall patterns. The project includes fetching, consolidating, and structuring rainfall data in JSON format using a Python Flask API, which can be used for further analysis.

## Table of Contents

Dataset and Setup
Configuration
How to Use
Project Structure
Data Description
Acknowledgement

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

**1.	Download and Extract Data:**
* Fetch rainfall data from specified URLs (as zip format).
* Extract JSON files from downloaded ZIP archives.
*Remove the zip files after extracting.

**2.	Load and Structure Data:**
* Check for existing data and, if not found, create a new rainfall_data.json in the data directory.
* Load the content of these files if they exist.

**3.	Check and Update Data:**
* Compare newly downloaded data with existing data.
* Update existing entries or add new entries as necessary.
* Log the number of new and updated items into data_update.log.
  
This how it looks the 
**data_update.log**

![image](https://github.com/Vajiranath/Rainfall-Data/assets/88283079/95b0b8ce-ceec-43a5-bc3a-b09896d4724e)


**4.	Save Updated Data:**
* Write the updated data back to the JSON file (rainfall_data.json), preserving the format and structure.

**5.	Create rainfall_metadata.json:**
* This file contains metadata about the dataset, including the specification of the columns, which helps in understanding the dataset.
  
**DATA_FILE:** data/rainfall_data.json

**METADATA_FILE:** data/rainfall_metadata.json


**app.py**

This Flask application provides API endpoints to retrieve and update rainfall data and its metadata. It integrates utility functions to handle data management, ensuring the data is current and accurate, with the app running on host 0.0.0.0 and port 5000.

**Steps:**

**1.	Initialize Flask Application:**
  * Create a Flask app instance to handle web requests.
  * Define API Endpoints:
    
**/vsu37/update_data:** Triggers fetching data from the datasource, updates the process, and returns a success message.

http://13.239.119.236:5000/vsu37/update_data

**/vsu37/rainfall_data:** Returns existing rainfall data in JSON format.

http://13.239.119.236:5000/vsu37/rainfall_data

**/vsu37/rainfall_metadata:** Returns metadata related to rainfall data.

http://13.239.119.236:5000/vsu37/rainfall_metadata

**2.	Integrate Data Handling Functions:**

  * Use utility functions (util.py) to load, check, update, and manage data within the API endpoints.

**3.	Run Application:**
   
  * Execute the Flask app on host 0.0.0.0 and port 5000, ensuring the data update function runs once at startup for initial setup.

## Configuration

In a tmux session, call the endpoint /vsu37/update_data using a cronjob to run it on an hourly basis. This ensures that the data in data/rainfall_data.json is updated every hour, providing the most recent rainfall data at any given time.

**Cronjob:**

`30 0-23 * * * /usr/bin/curl http://13.239.119.236:5000/vsu37/update_data`

## How to Use

**To get the rainfall information for the most recent hour:**

http://13.239.119.236:5000/vsu37/rainfall_data

**To get the metadata about the rainfall dataset:**

http://13.239.119.236:5000/vsu37/rainfall_metadata


## Project Structure

![image](https://github.com/Vajiranath/Rainfall-Data/assets/88283079/a4455b5e-0336-4ae8-9181-edefb70b5769)

## Data Description

The following fields are available in data/rainfall_data.json:

**Site_x0020_Name:** Name of the site used to observe the rainfall for the particular area.

**Last_x0020_Sample:** Date and time when the rainfall was measured (format YYYY-MM-DDTHH:MM
+12:00).

**Last_x0020_Hour:** Rainfall measured in millimeters (mm) for the last hour.

**RainToday:** Rainfall measured in millimeters (mm) for the current hour.

**_x002D_1_x0020_Day:** Rainfall measured in millimeters (mm) at the same hour, 1 day back.

**_x002D_2_x0020_Day:** Rainfall measured in millimeters (mm) at the same hour, 2 days back.

**_x002D_3_x0020_Day:** Rainfall measured in millimeters (mm) at the same hour, 3 days back.

**_x002D_4_x0020_Day:** Rainfall measured in millimeters (mm) at the same hour, 4 days back.

**_x002D_5_x0020_Day:** Rainfall measured in millimeters (mm) at the same hour, 5 days back.

**_x002D_6_x0020_Day:** Rainfall measured in millimeters (mm) at the same hour, 6 days back.

**_x002D_7_x0020_Day:** Rainfall measured in millimeters (mm) at the same hour, 7 days back.

**Total_x0020_Rainfall:** Total rainfall measured for the particular hour during the last 7 days, including the present day.

**SITE_NO:** Site number for the particular site which can be uniquely identified.

**ShortName:** Short name for the site.

**Sub_text:** Any other details, if any.

**SiteOwner:** Owner of the data source - Canterbury Regional Council.

**Location:** Dataset of the region (e.g., S-South, N-North based on the Rakaia River).

**WGS84_Longitude:** Longitude of the site.

**WGS84_Latitude:** Latitude of the site.

**OwnerLogo:** Logo information of the dataset owner, e.g., Canterbury Regional Council.

## Acknowledgement

This project was undertaken as part of the requirements for the course DATA472 in the master’s degree in applied data science at the University of Canterbury.

I would like to express my gratitude to our lecturer, Giulio Valentino Dalla Riva, for his extensive knowledge and guidance throughout the course. Additionally, I am grateful to all my colleagues who provided help and shared their knowledge, contributing significantly to the success of this project.

















