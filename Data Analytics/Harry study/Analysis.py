import pandas as pd

# 물 품질 데이터
water_quality_data = pd.DataFrame({
    "Site ID": ["AV-1", "AV-2", "AV-3", "AV-1", "AV-2", "AV-3"],
    "Date": ["2023-10-25", "2023-10-25", "2023-10-25", "2023-11-15", "2023-11-15", "2023-11-15"],
    "Temperature (°C)": [15.2, 14.8, 13.6, 12.4, 11.9, 10.8],
    "pH": [7.8, 7.5, 7.3, 7.6, 7.4, 7.2],
    "Dissolved Oxygen (mg/L)": [8.5, 7.9, 6.8, 8.2, 7.7, 6.2]
})

# 물고기 개체군 데이터
fish_population_data = pd.DataFrame({
    "Site ID": ["AV-1", "AV-2", "AV-3", "AV-1", "AV-2", "AV-3"],
    "Date": ["2023-10-25", "2023-10-25", "2023-10-25", "2023-11-15", "2023-11-15", "2023-11-15"],
    "Species": ["Brown Trout", "Shortfin Eel", "Freshwater Shrimp", "Rainbow Trout", "Kokopu", "No fish observed"],
    "Count": [50, 75, 120, 35, 40, None],
    "Average Size (cm)": [32, 45, 2, 28, 18, None]
})

# 데이터 확인
print("Water Quality Data:")
print(water_quality_data)
print("\nFish Population Data:")
print(fish_population_data)
