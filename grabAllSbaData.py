import requests
import pandas as pd
import time

# Constants
BASE_URL = "https://www.fedsdatacenter.com/federal-pay-rates/output.php"
HEADERS = {
    'User-Agent': 'Mozilla/5.0'
}

# Query parameters template
params_template = {
    'n': '',
    'a': 'SMALL BUSINESS ADMINISTRATION',
    'l': '',
    'o': '',
    'y': '2024',
    'sEcho': 3,
    'iColumns': 9,
    'sColumns': ',,,,,,,,',
    'iDisplayLength': 100,
    'mDataProp_0': 0,
    'bSortable_0': 'true',
    'mDataProp_1': 1,
    'bSortable_1': 'true',
    'mDataProp_2': 2,
    'bSortable_2': 'true',
    'mDataProp_3': 3,
    'bSortable_3': 'true',
    'mDataProp_4': 4,
    'bSortable_4': 'true',
    'mDataProp_5': 5,
    'bSortable_5': 'true',
    'mDataProp_6': 6,
    'bSortable_6': 'true',
    'mDataProp_7': 7,
    'bSortable_7': 'true',
    'mDataProp_8': 8,
    'bSortable_8': 'true',
    'iSortCol_0': 0,
    'sSortDir_0': 'asc',
    'iSortingCols': 1
}

def fetch_all_records():
    all_records = []
    start = 0
    total_records = None

    while True:
        params = params_template.copy()
        params['iDisplayStart'] = start
        print(f"Fetching records starting at {start}...")

        try:
            response = requests.get(BASE_URL, params=params, headers=HEADERS)
            response.raise_for_status()
            data = response.json()

            if total_records is None:
                total_records = int(data['iTotalDisplayRecords'])

            aa_data = data.get('aaData', [])
            if not aa_data:
                break

            all_records.extend(aa_data)
            start += params['iDisplayLength']

            # Optional: Pause to avoid overwhelming the server
            time.sleep(0.5)

            if start >= total_records:
                break
        except Exception as e:
            print(f"Error fetching data: {e}")
            break

    return all_records

def main():
    records = fetch_all_records()

    # Define column names based on known data structure
    columns = ['Name', 'Pay Plan', 'Grade', 'Salary', 'Bonus', 'Agency', 'Location', 'Occupation', 'Year']

    df = pd.DataFrame(records, columns=columns)

    print(f"\nFetched {len(df)} records.")
    print(df.head())

    # Optional: Live interaction
    while True:
        cmd = input("\nEnter a pandas command to analyze the DataFrame (e.g., df['Salary'].replace('[\$,]', '', regex=True).astype(float).mean() to get average salary of the USA SBA) or 'exit':\n> ")
        if cmd.strip().lower() == 'exit':
            break
        try:
            result = eval(cmd, {"df": df, "pd": pd})
            print(result)
        except Exception as e:
            print(f"Error executing command: {e}")

if __name__ == "__main__":
    main()
