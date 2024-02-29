# Importing pandas:
import pandas as pd

# Reading the csv file:
df = pd.read_csv('data/raw/height_income_distributions/hrs_height_income.csv')

# Name of columns:
print(df.columns)

# Keeping useful variables:
useful_columns = ['age', 'height', 'hhincome', 'female']
df = df[useful_columns]

# Checking for missing values:
print(df.isnull().sum())

# Replace non-numeric values with NaN
df['height'] = pd.to_numeric(df['height'], errors='coerce')

# Converting height to float:
df['height'] = df['height'].astype(float)

# Summary statistics:
print(df.describe())

# Calculating average height for each age group and genders:

# Defining the age ranges
age_ranges = [
    (20, 29),
    (30, 39),
    (40, 49),
    (50, 59),
    (60, 69),
    (70, 79)

# Create a nested dictionary to store heights by age range and gender
for age_range in age_ranges:
  heights_by_age_range_gender[age_range] = {0: [], 1: []}
  
# Add the heights based on age range and gender to the dictionary
for index, row in df.iterrows():
    age = row['age']
    female = row['female']
    height = row['height']
    for age_range in age_ranges:
        if age_range[0] <= age <= age_range[1]:
            heights_by_age_range_gender[age_range][female].append(height)
            break

# Calculate average height for each age range and gender
average_heights_by_age_range_gender = {}
for age_range, gender_data in heights_by_age_range_gender.items():
    average_heights_by_age_range_gender[age_range] = {
        "Male": sum(gender_data[0]) / len(gender_data[0]) if gender_data[0] else None,
        "Female": sum(gender_data[1]) / len(gender_data[1]) if gender_data[1] else None
    }

# The results:
print("Average height by age range and gender:")
for age_range, gender_avg_heights in average_heights_by_age_range_gender.items():
    age_range_str = f"{age_range[0]}-{age_range[1]}"
    print(f"Age range {age_range_str}:")
    for gender, avg_height in gender_avg_heights.items():
        if avg_height is not None:
            print(f"  Gender: {'Female' if gender == 'Female' else 'Male'} - Average Height: {avg_height:.2f} cm")
        else:
            print(f"  Gender: {'Female' if gender == 'Female' else 'Male'} - No data available")



