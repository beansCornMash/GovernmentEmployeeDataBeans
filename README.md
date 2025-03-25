# SBA Federal Pay Data Scraper & Analyzer

This Python 3.6.8 script fetches salary data for employees of the **Small Business Administration (SBA)** from [FedsDataCenter.com](https://www.fedsdatacenter.com), loads it into a Pandas DataFrame, and allows live command-line analysis.

## Features

- Automatically paginates through all available SBA salary records via a public API
- Cleans and loads data into a Pandas DataFrame
- Calculates the average salary of all SBA employees
- Interactive prompt to analyze the dataset using any valid Pandas command

## Requirements

- Python 3.6.8
- `requests` library
- `pandas` library

You can install the dependencies with:

```bash
pip install pandas requests
```

# Usage
Run the script:
```bash
python sba_pay_scraper.py
```

You’ll see:
- The data being fetched in batches of 100
- A preview of the first few records
- The average salary of all SBA employees
- 
Then you'll enter an interactive shell where you can run commands like:
```python
df['Location'].value_counts()
df[df['Grade'] == '15']
df.groupby('Occupation')['Salary'].mean().sort_values(ascending=False)
```

To exit the prompt, type:
```text
Fetched 7925 records.
         Name Pay Plan Grade     Salary  ...    Location             Occupation  Year
0     A, MIN    NMN     14  139395.00  ...   WASHINGTON            STATISTICS  2024
1     AABY, KATHERINE  00  SES  220147.00  ...   WASHINGTON      PROGRAM MANAGEMENT  2024
...

Average SBA Salary: $98,765.43

Enter a pandas command to analyze the DataFrame (e.g., df['Location'].value_counts()) or 'exit':
>
```

# Notes
The script respects server load with a small delay (time.sleep(0.5)) between API requests.
Only the 'Salary' column is converted to numeric for analysis — other monetary columns (e.g., 'Bonus') can be handled similarly if needed.

# Inspiration
I saw an article from the USA Small Business Association that says that the average salary of an SBA employee is over $132,000.
I know government data is available, so I decided to look it up myself. I went to the federal data center, went to this
url in particular, https://www.fedsdatacenter.com/federal-pay-rates/index.php?y=2024&n=&l=&a=SMALL+BUSINESS+ADMINISTRATION&o=,
and then I got the underlying api GET request for the salary data. Then I used ChatGPT to write myself a python script
I can interact with. I also had it generate this README.
