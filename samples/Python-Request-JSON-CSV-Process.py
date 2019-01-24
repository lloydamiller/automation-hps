import urllib.parse as parse
import requests
import pandas as pd

"""
LINKS:
Dashboard Page: https://fec.delvedc.com/committees/id/C00401224
FEC Page: https://www.fec.gov/data/committee/C00401224/?tab=filings
API Reference: https://api.open.fec.gov/developers/#/filings/get_committee__committee_id__filings_
"""

# DEFINE CONNECTION

committee_id = "C00401224"

endpoint = "https://api.open.fec.gov/v1/committee/" + committee_id + "/filings/?"

params = {
    "page": 1,
    "per_page": "20",
    "form_type": "F3X",
    "is_amended": "False",
    "sort": "-coverage_end_date",
    "api_key": "3Cyct8saXOvD4WNkT3VTH51uNPCAOA1oMw9HMJ9K"
}

# urlencode convers a dict object (params) into a URL query string
p = parse.urlencode(params)

url = endpoint + p

# Get Request And Validate Results

r = requests.get(url)

# always check for errors
if r.status_code != 200:
    print("[!] ERROR %i: %s" % (r.status_code, r.reason))

else:
    j = r.json()
    results = j["results"]
    print("[*] Total Results: %i" % len(results))

# Save Important Data As Structured CSV


def get_data(d):
    return {
        "csv_url": d["csv_url"],
        "document_description": d["document_description"],
        "receipt_date": d["receipt_date"],
        "pages": d["pages"],
        "report_type": d["report_type"],
        "coverage_end_date": d["coverage_end_date"],
        "coverage_start_date": d["coverage_start_date"]
    }


data = [get_data(x) for x in results if x]

df = pd.DataFrame.from_records(data)

df.to_csv("Formatted_Results.csv", index=False)
