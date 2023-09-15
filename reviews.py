import pandas as pd

# Read the data from the CSV file
reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

# Create a DataFrame to store the results
result_df = pd.DataFrame(reviews['country'].value_counts().reset_index())
result_df.columns = ['country', 'count']

# Calculate the average points per country
avg_points = reviews.groupby('country')['points'].mean().round(1).reset_index()
avg_points.columns = ['country', 'points']

# Merge the count and average points DataFrames
result_df = pd.merge(result_df, avg_points, on='country')

# Sort by the count of reviews in descending order
result_df = result_df.sort_values(by='count', ascending=False)

# Print the DataFrame without the index column
print(result_df.to_string(index=False))

# Save the results to a CSV file
result_df.to_csv('./data/reviews-per-country.csv', index=False)


