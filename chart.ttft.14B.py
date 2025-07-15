import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Your data as a string (you can also read from a file)
data = """ttft	accel_type
146	GPU
161	GPU
180	GPU
189	GPU
190	GPU
199	GPU
207	GPU
229	GPU
236	GPU
252	GPU
262	GPU
263	GPU
274	GPU
274	GPU
282	GPU
289	GPU
289	GPU
291	GPU
301	GPU
305	GPU
310	GPU
315	GPU
326	GPU
329	GPU
330	GPU
331	GPU
336	GPU
341	GPU
343	GPU
345	GPU
347	GPU
350	GPU
352	GPU
352	GPU
358	GPU
370	GPU
378	GPU
382	GPU
401	GPU
409	GPU
415	GPU
421	GPU
441	GPU
445	GPU
448	GPU
452	GPU
518	GPU
519	GPU
520	GPU
522	GPU
540	GPU
557	GPU
578	GPU
595	GPU
601	GPU
609	GPU
611	GPU
612	GPU
614	GPU
617	GPU
621	GPU
629	GPU
645	GPU
647	GPU
651	GPU
656	GPU
657	GPU
665	GPU
669	GPU
683	GPU
689	GPU
694	GPU
696	GPU
767	GPU
772	GPU
793	GPU
869	GPU
874	GPU
880	GPU
885	GPU
888	GPU
933	GPU
995	GPU
1020	GPU
1040	GPU
1050	GPU
1050	GPU
1110	GPU
1120	GPU
1130	GPU
1150	GPU
1270	GPU
1370	GPU
1400	GPU
1400	GPU
1420	GPU
1430	GPU
1440	GPU
1570	GPU
1680	GPU
1700	GPU
2320	GPU
2340	GPU
2360	GPU
2400	GPU
2460	GPU
2480	GPU
2720	GPU
5560	CPU
5680	GPU
8050	CPU
8220	GPU
8510	CPU
8730	GPU
9090	GPU
11110	GPU
11640	CPU
12110	CPU
12160	CPU
12330	CPU
12420	CPU
12550	CPU
13040	CPU
13610	CPU
14500	CPU
14660	CPU
15240	CPU
15800	CPU
16079	CPU
16520	CPU
17730	CPU
18160	CPU
18910	CPU
20280	CPU
20420	CPU
20740	CPU
21820	CPU
21970	CPU
21980	CPU
22720	CPU
23070	CPU
23140	GPU
23510	CPU
24190	CPU
25670	CPU
26020	CPU
26600	CPU
29510	CPU
30960	CPU
32520	CPU
34110	CPU
35090	CPU
35560	CPU
39600	CPU
39870	CPU
41330	CPU
43330	CPU
44020	CPU
44660	CPU
45280	CPU
47630	CPU
49040	CPU
49220	CPU
49690	CPU
54600	CPU
56470	CPU
57040	CPU
61340	CPU
63160	CPU
67890	CPU
73940	CPU
76440	CPU
92910	CPU
98340	CPU
99050	CPU
105130	CPU
106670	CPU
116730	CPU
117860	CPU
130259	CPU
132500	CPU
140590	CPU
156940	CPU
186150	CPU
220700	CPU
221240	CPU
298080	CPU
"""

# Read the data into a pandas DataFrame
df = pd.read_csv(StringIO(data), sep='\t')

# Create value indexes (0 to len(df)-1)
value_indexes = range(len(df))

# Create colors: green for GPU, red for CPU
colors = ['green' if accel == 'GPU' else 'red' for accel in df['accel_type']]

# Create the bar chart
plt.figure(figsize=(15, 8))
bars = plt.bar(value_indexes, df['ttft'], color=colors, alpha=0.7)

# Customize the chart
plt.xlabel('Value Index')
plt.ylabel('Time to First Token [ms]')
plt.yscale('log')
plt.title('TTFT vs Value Index by Accelerator Type')
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
plt.savefig('ttft_vs_value_index.14B.png', dpi=300, bbox_inches='tight')
