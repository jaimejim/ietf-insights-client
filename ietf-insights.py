import argparse
import requests

# Parse command line arguments
parser = argparse.ArgumentParser(description='Query the server.')
parser.add_argument('-m', '--meeting', type=str, help='The meeting to process.')
parser.add_argument('-n', '--name', type=str, help='The name to filter on.')
parser.add_argument('-c', '--company', type=str, help='The company to filter on.')
parser.add_argument('-g', '--group', type=str, help='The group to filter on.')
parser.add_argument('-s', '--stats', action='store_true', help='Display statistics.')
parser.add_argument('-H', '--historical-stats', action='store_true', help='Display historical statistics.')
parser.add_argument('--country', type=str, help='The country to filter on.')
parser.add_argument('--not-attending', type=str, help='The company to find non-attending groups for.')
args = parser.parse_args()

# Convert the arguments to a dictionary and remove None values
params = vars(args)
params = {k: v for k, v in params.items() if v is not None}

response = requests.get(f'http://ietf-participation-insights.onrender.com:80/query', params=params)

# Print the response text
print(response.text)