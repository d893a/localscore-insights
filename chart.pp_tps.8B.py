import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Your data as a string (you can also read from a file)
data = """prompt_tps	accel_type
8479	GPU
8441	GPU
7398	GPU
7015	GPU
6657	GPU
6808	GPU
6307	GPU
5925	GPU
5202	GPU
5487	GPU
5328	GPU
4687	GPU
5065	GPU
4789	GPU
4682	GPU
4299	GPU
4428	GPU
4546	GPU
4461	GPU
4285	GPU
4120	GPU
4323	GPU
3991	GPU
3876	GPU
4014	GPU
3928	GPU
3571	GPU
4006	GPU
3739	GPU
3985	GPU
3641	GPU
3916	GPU
3834	GPU
3637	GPU
3552	GPU
3682	GPU
3447	GPU
3371	GPU
3270	GPU
3204	GPU
3140	GPU
3192	GPU
3028	GPU
2918	GPU
2792	GPU
2890	GPU
2862	GPU
2836	GPU
2817	GPU
2617	GPU
2601	GPU
2509	GPU
2484	GPU
2457	GPU
2427	GPU
2360	GPU
2184	GPU
2102	GPU
2145	GPU
2160	GPU
2034	GPU
2247	GPU
2267	GPU
2112	GPU
2217	GPU
2085	GPU
2130	GPU
1823	GPU
1974	GPU
2011	GPU
1962	GPU
1929	GPU
2056	GPU
1898	GPU
2013	GPU
1821	GPU
1861	GPU
1729	GPU
1748	GPU
1708	GPU
1515	GPU
1460	GPU
1487	GPU
1482	GPU
1400	GPU
1370	GPU
1328	GPU
1223	GPU
1677	GPU
1170	GPU
1050	GPU
1050	GPU
1468	GPU
885	GPU
1028	GPU
888	GPU
926	GPU
813	GPU
791	GPU
789	GPU
760	GPU
604	GPU
524	GPU
587	GPU
607	GPU
563	GPU
427	GPU
250	CPU
256	GPU
172	CPU
891	GPU
163	CPU
290	GPU
809	GPU
129	GPU
115	CPU
113	CPU
114	CPU
112	CPU
104	CPU
99	CPU
94	CPU
93	CPU
88	CPU
75	CPU
68	CPU
66	CPU
68	CPU
64	CPU
59	CPU
60	CPU
61	CPU
66	GPU
52	CPU
53	CPU
48	CPU
47	CPU
43	CPU
43	CPU
40	CPU
40	CPU
38	CPU
34	CPU
36	CPU
34	CPU
31	CPU
31	CPU
31	CPU
31	CPU
30	CPU
28	CPU
29	CPU
28	CPU
24	CPU
25	CPU
22	CPU
23	CPU
22	CPU
21	CPU
18	CPU
18	CPU
15	CPU
14	CPU
14	CPU
14	CPU
13	CPU
11	CPU
12	CPU
11	CPU
10	CPU
10	CPU
9	CPU
6	CPU
6	CPU
6	CPU
5	CPU
1	CPU
"""

# Read the data into a pandas DataFrame
df = pd.read_csv(StringIO(data), sep='\t')

# Create value indexes (0 to len(df)-1)
value_indexes = range(len(df))

# Create colors: green for GPU, red for CPU
colors = ['green' if accel == 'GPU' else 'red' for accel in df['accel_type']]

# Create the bar chart
plt.figure(figsize=(15, 8))
bars = plt.bar(value_indexes, df['prompt_tps'], color=colors, alpha=0.7)

# Customize the chart
plt.xlabel('Value Index')
plt.ylabel('Prompt processing [tokens/s]')
plt.yscale('log')
plt.title('8B Prompt Processing vs Value Index by Accelerator Type')
plt.grid(True, which='both', axis='both', alpha=0.3, ls="-")


# Create legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='green', alpha=0.7, label='GPU'),
                   Patch(facecolor='red', alpha=0.7, label='CPU')]
plt.legend(handles=legend_elements)


# Adjust layout and show
plt.tight_layout()
# plt.show()

#save result to png file
plt.savefig('pp_tps_vs_value_index.8B.png', dpi=300, bbox_inches='tight')
