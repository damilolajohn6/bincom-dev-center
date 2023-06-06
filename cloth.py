from bs4 import BeautifulSoup
import statistics
import psycopg2

# HTML data from the template
html_data = """
<html>
<head>
<title>Our Python Class exam</title>
...
</html>
"""

# Parse the HTML
soup = BeautifulSoup(html_data, 'html.parser')

# Find the table body
table_body = soup.find('tbody')

# Extract color data from the table rows
colors = []
for row in table_body.find_all('tr'):
    data = row.find('td', text=True).get_text()
    colors.extend(data.split(', '))

# Calculate the mean color
mean_color = max(set(colors), key=colors.count)

# Calculate the most worn color
most_worn_color = max(set(colors), key=colors.count)

# Calculate the median color
median_color = statistics.median(colors)

# Calculate the variance of the colors
variance = statistics.variance(colors)

# Calculate the probability of choosing the color red
red_count = colors.count('RED')
total_colors = len(colors)
probability_red = red_count / total_colors

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password"
)

# Create a new table to store colors and frequencies
create_table_query = """
CREATE TABLE colors (
    color VARCHAR(50),
    frequency INTEGER
);
"""
with conn.cursor() as cursor:
    cursor.execute(create_table_query)

# Calculate the frequency of each color
color_frequencies = {}
for color in colors:
    if color in color_frequencies:
        color_frequencies[color] += 1
    else:
        color_frequencies[color] = 1

# Insert color data into the database
insert_query = "INSERT INTO colors (color, frequency) VALUES (%s, %s);"
with conn.cursor() as cursor:
    for color, frequency in color_frequencies.items():
        cursor.execute(insert_query, (color, frequency))

# Commit the changes and close the connection
conn.commit()
conn.close()

# Print the results
print("The mean color of the shirts is:", mean_color)
print("The most frequently worn color throughout the week is:", most_worn_color)
print("The median color of the shirts is:", median_color)
print("The variance of the colors is:", variance)
print("The probability of choosing the color red is:", probability_red)
