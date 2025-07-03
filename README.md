# Asia Weather Data 2025

This repository contains a Jupyter Notebook and a Python script that fetches, analyzes, and visualizes the current weather data for major cities in Asia in 2025.

## Features

- Fetches weather data from the OpenWeatherMap API.
- Saves the data to a CSV file.
- Analyzes and visualizes the data using `matplotlib` and `seaborn`.
- Uses a K-Means clustering model to group cities with similar weather conditions.

## Data

The weather data is fetched from OpenWeatherMap API and saved to a CSV file named `asia_weather_data_2025.csv`.

## Usage

To run the script or the notebook, you need to have Python and the following libraries installed:

```
pip install requests pandas matplotlib seaborn scikit-learn
```

### Set the API Key

This project uses the OpenWeatherMap API. You will need to get a free API key from their website and set it as an environment variable named `OPENWEATHER_API_KEY`.

**On Linux and macOS:**

```bash
export OPENWEATHER_API_KEY="your_api_key"
```

**On Windows:**

```powershell
$env:OPENWEATHER_API_KEY="your_api_key"
```

### Running the script

To fetch the latest weather data, run the following command:

```
python get_weather_data.py
```

### Using the Jupyter Notebook

Once you have set the API key, you can open and run the `weather_data.ipynb` notebook to see the data analysis, visualizations, and machine learning model.
