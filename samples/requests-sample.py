"""
https://api.open.fec.gov/developers/

"""

import requests
import csv

base = "https://api.open.fec.gov/v1/"

endpoint = "/schedules/schedule_a/"

api_key = "3Cyct8saXOvD4WNkT3VTH51uNPCAOA1oMw9HMJ9K"

params = {
        "api_key": api_key,
        "contributor_employer": "Hamilton Place Strategies"
        }

url = f"{base}{endpoint}"
r = requests.get(url, params=params)
if r.status_code == 200:
    print("It worked!")
else:
    print(f"Error {r.status_code}")
j = r.json()
results = j["results"]


# once we have the first set of results, we want to continue getting results until there are none left
# to do so, we "paginate" using the defined structure of the data dictated by the API service
# for the FEC, this means each set of results includes a "pagination" key that includes a "last_indexes" key
# if the value of that key is None, there are no more pages, otherwise there will be two keys, the values of which
# need to be included in the parameters for the next request, or else it will return the same data as before
pagination = j["pagination"]
count = 1
while pagination["last_indexes"] is not None:
    params["last_index"] = pagination["last_indexes"]["last_index"]
    params["last_contribution_receipt_date"] = pagination["last_indexes"]["last_contribution_receipt_date"]
    r = requests.get(url, params=params)
    if r.status_code == 200:
        print("It worked!")
    else:
        print(f"Error {r.status_code}")
    j = r.json()
    results.extend(j["results"])
    pagination = j["pagination"]
    print(f"Running {count}, {pagination}")
    count += 1

# This code creates a new list, formatted_results, loops through the existing results
# and then adds objects to the list containing only the information we want
formated_results = []
for result in results:
    formated_results.append({
            "contributor_first_name": result["contributor_first_name"],
            "contributor_last_name": result["contributor_last_name"],
            "contributor_occupation": result["contributor_occupation"],
            "contributor_employer": result["contributor_employer"],
            "contribution_receipt_amount": result["contribution_receipt_amount"],
            "committee": result["committee"]["name"],
            "contribution_receipt_date": result["contribution_receipt_date"],
            "pdf_url": result["pdf_url"]
            })

# This code opens a new file (data.csv), and writes each row of data to it.
with open('data.csv', 'w') as d:
    csvwriter = csv.writer(d)
    count = 0
    for row in formated_results:
        if count == 0:
            header = row.keys()
            csvwriter.writerow(header)
            count += 1
        csvwriter.writerow(row.values())
