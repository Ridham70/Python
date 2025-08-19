import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


input_filename = sys.argv[1]
output_filename = sys.argv[2]

if not input_filename.endswith(".csv") or not output_filename.endswith(".csv"):
    sys.exit("Both command-line arguments must be CSV files")

try:
    with open(input_filename, "r") as input_file, open(output_filename, "w", newline='') as output_file:
        reader = csv.DictReader(input_file)
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            full_name = row["name"]
            last, first = full_name.split(", ")
            writer.writerow({
                "first": first,
                "last": last,
                "house": row["house"]
            })

except FileNotFoundError:
    sys.exit("Input file does not exist")
