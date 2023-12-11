import csv

input_file_path = "your_input_file.txt"
output_file_path = "duke_data.csv"

with open(input_file_path, "r", encoding="utf-8") as input_file:
    # Read the input file
    lines = input_file.readlines()

    # Extract header and data
    header = lines[0].strip().split(",")
    data = [line.strip().split(",") for line in lines[1:]]

with open(output_file_path, "w", newline="", encoding="utf-8") as output_file:
    # Write to the CSV file
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(header)
    csv_writer.writerows(data)

print(f"Conversion complete. CSV file saved at {output_file_path}")
