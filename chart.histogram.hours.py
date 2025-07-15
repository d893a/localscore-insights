import csv
from dateutil import parser
import matplotlib.pyplot as plt

filename = 'localscore_leaderboard.tsv'
hours = []

# Read the TSV file and extract the 'test_date' column
with open(filename, 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        test_date_str = row.get('test_date')
        if test_date_str:
            try:
                dt = parser.parse(test_date_str)
                hours.append(dt.hour)
            except Exception as e:
                print(f"Could not parse date: {test_date_str} ({e})")

# Plot the histogram
plt.hist(hours, bins=range(25), edgecolor='black', align='left')
plt.xlabel('Hour of Day')
plt.ylabel('Count')
plt.title('Histogram of Test Dates by Hour')
plt.xticks(range(24))
# plt.show()
plt.savefig('localscore_leaderboard.histogram.run_hours.png', dpi=300, bbox_inches='tight')
