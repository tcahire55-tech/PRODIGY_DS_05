# =========================================
# Traffic Accident Analysis - RTA Dataset
# =========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# -------------------------------
# 1. Load Dataset
# -------------------------------
FILE_PATH = "RTA Dataset.csv"
df = pd.read_csv(FILE_PATH)

print("Dataset Loaded Successfully")
print(df.shape)
print(df.columns)

# -------------------------------
# 2. Basic Cleaning
# -------------------------------

# Drop rows with missing important values
df = df.dropna(subset=['Time', 'Weather_conditions', 'Road_surface_conditions'])

# Convert Time column to hour
df['Hour'] = pd.to_datetime(df['Time'], errors='coerce').dt.hour

# -------------------------------
# 3. Accidents by Time of Day
# -------------------------------

plt.figure(figsize=(10,5))
sns.countplot(x='Hour', data=df)
plt.title("Accidents by Time of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.savefig("accidents_by_hour.png")
plt.show()

# -------------------------------
# 4. Accidents by Weather
# -------------------------------

plt.figure(figsize=(10,6))
sns.countplot(y='Weather_conditions', data=df, order=df['Weather_conditions'].value_counts().index)
plt.title("Accidents by Weather Conditions")
plt.xlabel("Number of Accidents")
plt.ylabel("Weather Condition")
plt.tight_layout()
plt.savefig("accidents_by_weather.png")
plt.show()

# -------------------------------
# 5. Accidents by Road Condition
# -------------------------------

plt.figure(figsize=(10,6))
sns.countplot(y='Road_surface_conditions', data=df, order=df['Road_surface_conditions'].value_counts().index)
plt.title("Accidents by Road Surface Conditions")
plt.xlabel("Number of Accidents")
plt.ylabel("Road Surface Condition")
plt.tight_layout()
plt.savefig("accidents_by_road.png")
plt.show()

# -------------------------------
# 6. Severity Analysis
# -------------------------------

plt.figure(figsize=(8,5))
sns.countplot(x='Accident_severity', data=df)
plt.title("Accident Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("severity_distribution.png")
plt.show()

# -------------------------------
# 7. Cause of Accidents
# -------------------------------

plt.figure(figsize=(10,6))
sns.countplot(y='Cause_of_accident', data=df, order=df['Cause_of_accident'].value_counts().head(10).index)
plt.title("Top Causes of Accidents")
plt.xlabel("Number of Accidents")
plt.ylabel("Cause")
plt.tight_layout()
plt.savefig("top_causes.png")
plt.show()

# -------------------------------
# 8. Accident Hotspots (Map)
# -------------------------------

# Use Latitude & Longitude if present
if 'Latitude' in df.columns and 'Longitude' in df.columns:
    map_data = df[['Latitude', 'Longitude']].dropna().sample(1000)

    m = folium.Map(
        location=[map_data['Latitude'].mean(), map_data['Longitude'].mean()],
        zoom_start=10
    )

    HeatMap(map_data.values).add_to(m)
    m.save("accident_hotspots.html")
    print("Hotspot map saved as accident_hotspots.html")

# -------------------------------
# 9. Correlation Heatmap
# -------------------------------

plt.figure(figsize=(8,6))
sns.heatmap(pd.crosstab(df['Weather_conditions'], df['Accident_severity']), cmap="coolwarm")
plt.title("Weather vs Accident Severity")
plt.tight_layout()
plt.savefig("weather_vs_severity.png")
plt.show()

print("Analysis Completed Successfully!")
