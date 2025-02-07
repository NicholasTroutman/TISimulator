import csv
import os

# Define the directory containing the CSV files and the output directory
input_directory = 'Results'
output_directory = 'Stats'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Initialize a list to store the best rows
best_rows = []


##CAPACITY
capacity=5

text=f"Capacity_{capacity}"
# Iterate through each file in the input directory

for filename in os.listdir(input_directory):
    if filename.endswith('.csv') and text in filename:  # Check for CSV files with '5' in the name
        file_path = os.path.join(input_directory, filename)
        print(file_path)
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)  # Read the header
            
            max_score = float('-inf')  # Initialize max score to negative infinity
            best_row = None
            
            # Iterate through each row in the CSV
            for row in reader:
                # Assuming the score is in the 6th column (index 6)
                score = float(row[6])  # Adjust index based on your CSV structure
                
                # Check if this score is the highest we've seen
                if score > max_score:
                    max_score = score
                    best_row = row
            
            # Store the best row for this file if found
            if best_row is not None:
                best_rows.append(best_row)

# Define the output CSV file path
fn = f'Best_Scores_Capacity_{capacity}.csv'
output_file_path = os.path.join(output_directory, 'Best_Scores_Capacity_5.csv')

# Write the best rows to the new CSV file
with open(output_file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    # Write the header (you can customize this based on your data)
    writer.writerow(header)  # Write the same header as the input files
    writer.writerows(best_rows)  # Write the best rows

print(f"Best rows saved to {output_file_path}")
