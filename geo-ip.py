from prettytable import PrettyTable
import json5
import requests
from sys import argv

# Define the function which used for separate list by every n objects.
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

# The usage should be: python3 {python_script} {IP list file}
if len(argv) != 2:
    print("You must choose one IP list file.")
    exit(1)

# Load the specific IP list file into a variable.
#with open('shit.txt', 'r') as ips:
with open(argv[1], 'r') as ips:
    # Initial the empty list
    sample_list = []
    # Iterate variable line by line
    for line in ips:
        # Remove the breakline char by strip()
        sample_list.append(line.strip())
        # Eliminate duplicate elements
    temp_list = list(set(sample_list))

# Separate list by each 100 elements
new_list = list(chunks(temp_list, 100))

result = []
# Iterate list elements
for seq, value in enumerate(new_list):
    sample_list = []
    # Iterate list elements
    for sub_seq, sub_value in enumerate(value):
        # Sample dict for calling the API
        temp_dict = {"query": "{}".format(sub_value)}
        # Append the sample dict one by one
        sample_list.append(temp_dict)

    url = "http://ip-api.com/batch"
    # Query the Geo-location API for IP, Country code, Country Name
    querystring = {"fields": "query,countryCode,country"}
    payload = json5.dumps(sample_list)
    headers = {'Content-Type': "application/x-www-form-urlencoded"}

    try:
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            params=querystring
            ).json()
    except requests.exceptions.Timeout as error_timeout:
        print(error_timeout)
        exit(2)
    except requests.exceptions.TooManyRedirects as too_many_redirects:
        print(too_many_redirects)
        exit(3)
    except requests.exceptions.RequestException as request_fail:
        print(request_fail)
        exit(1)

    result += response

result_table = PrettyTable()
result_table.field_names = ["CountryCode","Country", "IP"]
result_table.align["CountryCode"] = "l"
result_table.align["Country"] = "l"
result_table.align["IP"] = "l"

# Sort the result record by the country code.
sorted_list = sorted(result, key=lambda k: k['countryCode'])

# Add all records into the PrettyTable
for list_key, list_value in enumerate(sorted_list):
    result_table.add_row([list_value['countryCode'], list_value['country'], list_value['query']])

print(result_table)
print(">>> This script will eliminate all duplicated IP from the source file.")