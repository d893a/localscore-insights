import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Your data as a string (you can also read from a file)
data = """prompt_tps	accel_type
5126	GPU
4787	GPU
4777	GPU
4758	GPU
4106	GPU
3905	GPU
3828	GPU
3552	GPU
3161	GPU
2973	GPU
2936	GPU
2868	GPU
2867	GPU
2713	GPU
2665	GPU
2663	GPU
2609	GPU
2526	GPU
2471	GPU
2451	GPU
2424	GPU
2382	GPU
2351	GPU
2317	GPU
2317	GPU
2291	GPU
2275	GPU
2224	GPU
2212	GPU
2189	GPU
2185	GPU
2131	GPU
2126	GPU
2106	GPU
2090	GPU
2069	GPU
2049	GPU
2034	GPU
2012	GPU
2010	GPU
2007	GPU
2005	GPU
1973	GPU
1969	GPU
1938	GPU
1917	GPU
1883	GPU
1876	GPU
1852	GPU
1837	GPU
1834	GPU
1816	GPU
1793	GPU
1752	GPU
1719	GPU
1642	GPU
1595	GPU
1524	GPU
1438	GPU
1419	GPU
1418	GPU
1408	GPU
1337	GPU
1330	GPU
1320	GPU
1307	GPU
1299	GPU
1266	GPU
1264	GPU
1260	GPU
1260	GPU
1241	GPU
1205	GPU
1178	GPU
1170	GPU
1166	GPU
1161	GPU
1133	GPU
1119	GPU
1100	GPU
1086	GPU
1072	GPU
1037	GPU
962	GPU
835	GPU
832	GPU
821	GPU
803	GPU
799	GPU
798	GPU
793	GPU
793	GPU
791	GPU
779	GPU
761	GPU
752	GPU
748	GPU
733	GPU
713	GPU
612	GPU
593	GPU
574	GPU
531	GPU
505	GPU
502	GPU
496	GPU
492	GPU
485	GPU
450	GPU
449	GPU
430	GPU
424	GPU
412	GPU
404	GPU
376	GPU
368	GPU
357	GPU
327	GPU
316	GPU
316	GPU
303	GPU
302	GPU
302	GPU
204	GPU
171	CPU
132	CPU
120	CPU
90	CPU
61	CPU
60	CPU
60	CPU
56	CPU
53	GPU
51	CPU
51	CPU
46	CPU
45	CPU
44	CPU
41	CPU
38	CPU
38	CPU
38	CPU
37	CPU
36	CPU
31	CPU
31	CPU
31	CPU
30	CPU
30	CPU
29	CPU
28	CPU
23	CPU
23	CPU
23	CPU
22	CPU
22	CPU
22	CPU
21	CPU
20	CPU
20	CPU
18	CPU
17	CPU
17	CPU
17	CPU
16	CPU
16	CPU
15	CPU
15	CPU
13	CPU
12	CPU
12	CPU
12	CPU
12	CPU
11	CPU
10	CPU
9	CPU
8	CPU
7	CPU
7	CPU
7	CPU
7	CPU
6	CPU
6	CPU
5	CPU
3	CPU
3	CPU
0	CPU
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
plt.title('14B Prompt Processing vs Value Index by Accelerator Type')
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
plt.savefig('pp_tps_vs_value_index.14B.png', dpi=300, bbox_inches='tight')
