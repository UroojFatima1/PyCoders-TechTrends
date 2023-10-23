import json
import csv

# Function to convert CSV data to JSONL format
def csv_to_jsonl(input_csv_file, output_jsonl_file, model_name):
    with open(input_csv_file, mode="r", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open(output_jsonl_file, "w") as jsonl_file:
            for row in csv_reader:
                api_request = {
                    "messages": [{"role": "system", "content": "You are a helpful assistant."},
                                 {"role": "user","content":"Extract only the top 5 technical skills etc from the following job description and return result in the form of comma separated values: "+row["description"]}],
                    "model":"text-davinci-002" # Replace with the actual column name in your CSV
                }
                json_line = json.dumps(api_request)
                jsonl_file.write(json_line + "\n")

# Define your input and output files
input_csv_file = "linkedinjobs5.csv"
output_jsonl_file = "linkedinjobs5.jsonl"
model_name = "text-generation-model"  # Replace with your model name
# text-davinci-002
# Convert CSV data to JSONL format
csv_to_jsonl(input_csv_file, output_jsonl_file, model_name)
