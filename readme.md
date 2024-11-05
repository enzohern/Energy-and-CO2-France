# Energy Production and CO₂ Emissions Analysis - Power BI Dashboard

This repository contains a detailed analysis of energy production and CO₂ emissions based on production data from various energy types in France, sourced from the **éCO₂mix** platform by **RTE France**. Using Power BI and Python, an interactive dashboard is created to visualize and analyze the environmental impact of each energy source in terms of CO₂ emissions, covering data from the year 2000 to 2023.

## Table of Contents

- [Project Description](#project-description)
- [Data Source](#data-source)
- [Dashboard Features](#dashboard-features)
- [Requirements](#requirements)
- [Visualization Structure](#visualization-structure)
- [Emissions Reduction Simulation](#emissions-reduction-simulation)

## Project Description

This project aims to provide a detailed analysis of energy production and CO₂ emissions across different periods. Using Power BI, the production from various energy sources (wind, hydro, nuclear, solar, fossil thermal, and renewable thermal) is explored along with the resulting carbon emissions from each. This allows for visualizing and simulating how changes in the energy mix could impact CO₂ emission reductions.

## Data Source

The data is sourced from **éCO₂mix** by **RTE France** under the dataset "La production d'électricité par filière". The database includes detailed energy production information in France by energy type and corresponding emissions, covering the period from 2000 to 2023.

## Tools Used

- **Python**: For initial data processing, cleaning, and transformation.
- **Power BI**: For interactive data visualization and analysis.

## Dashboard Features

1. **Key Indicators**: Cards displaying total energy production, total CO₂ emissions, and carbon intensity.
2. **Energy Source Analysis**: Graphs highlighting production and emissions for each energy source over time.
3. **Emissions Reduction Simulation**: A simulation tool to show the potential impact of reducing non-renewable energy production and increasing renewable energy sources.
4. **Interactive Filters**: Time filters (year and month) and energy type filters to view specific data and adjust visualizations.

## Requirements

- **Power BI Desktop**: To open and customize the .pbix file.
- **Energy Production Dataset**: Dataset with the following columns:
  - `Date`: Date in year-month format (`yyyy-MM`).
  - `Filière`: Type of energy.
  - `Valeur (TWh)`: Production in Terawatt-hours.
  - `CO₂ Emissions`: Calculated in Mt CO₂.

## Visualization Structure

The dashboard consists of the following visualizations:

1. **Summary Cards**:
   - Total energy production.
   - Total CO₂ emissions.
   - Carbon intensity.
   
2. **Stacked Bar Chart**: Shows energy production by source and their relative contributions.
3. **Line Chart**: Visualizes the production trend by energy source over time.
4. **Pie Chart or Comparative Bars**: Shows CO₂ emissions by energy source.
5. **Emissions Reduction Simulation Chart**: Shows the impact of switching from non-renewable to renewable energy production.

## Emissions Reduction Simulation

The **Emissions Reduction Simulation** is an interactive feature that simulates the effect of reducing a percentage of non-renewable energy production (e.g., fossil thermal) and replacing it with renewable sources (e.g., solar or wind). This provides a projected view of how CO₂ emissions would vary under different scenarios.

1. Adjust the slider to set the percentage reduction in non-renewable production.
2. Observe how CO₂ emissions change in the visualizations.
