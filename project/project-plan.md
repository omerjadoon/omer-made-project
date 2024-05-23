# Project Plan

## Title
<!-- Give your project a short title. -->
Impact of Climate change on various species of trees in Frankfurt

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Coorelation of Planation year temperature with the crown diameter, trunk height etc of various species of trees?
2. How it varies across different species of plants?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->

Climate change impacts the growth of trees. So my aim is to find the impact of climate change especially increase in temprature on the growth of different plant species in Frankfurt

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: GovData Germany
* Metadata URL: https://data.europa.eu/data/datasets/73c5a6b3-c033-4dad-bb7d-8783427dd233?locale=en
* Data URL: https://offenedaten.frankfurt.de/dataset/73c5a6b3-c033-4dad-bb7d-8783427dd233/resource/257690bb-f40a-4e3a-93da-1310214f392f/download/baumauswahl.csv

* Data Type: CSV

Dataset provide the following information: Type and genus of the tree, tree number, object, plant year, crown diameter, coordinate (right and high value) in ETRS 89.

### Datasource2: Kaggle - Climate Change: Earth Surface Temperature Data
* Metadata URL: https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data
* Data URL:https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data

* Data Type: CSV

Dataset provide the following information: Type and genus of the tree, tree number, object, plant year, crown diameter, coordinate (right and high value) in ETRS 89.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Data Ingestion: Get all the relevant Data [#1][i1]
2. Data PreProcessing 
3. Generate Report

[i1]: https://github.com/jvalue/made-template/issues/1
