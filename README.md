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

** Data Source: ** ECAN Rainfall data

This dataset consists of rainfall measurements and details from different sites across the South Island of New Zealand. It's divided into two main regions:

** NORTH: ** Sites observing rainfall north of the Rakaia River
** NORTH_URL: ** https://data.ecan.govt.nz:443/data/51/Rainfall/Rainfall%20summary%20by%20area/JSON?Sites=NORTH&zip=1

** SOUTH: ** Sites observing rainfall south of the Rakaia River
** SOUTH_URL: ** https://data.ecan.govt.nz:443/data/51/Rainfall/Rainfall%20summary%20by%20area/JSON?Sites=SOUTH&zip=1

These data are refreshed hourly and contain the rainfall details for each site.

Host IP: 13.239.119.236
Operating System: AWS Ubuntu
Type: AWS EC2
RAM: 4 GB
Disk: 8 GB

Python should be installed on the host server along with the following packages/libraries: os, json, requests, zipfile, logging, datetime.

Additionally, install tmux to support session persistence and recovery even after disconnection.




