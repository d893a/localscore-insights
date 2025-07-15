import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Your data as a string (you can also read from a file)
data = """ttft	accel_type
245	GPU
279	GPU
281	GPU
322	GPU
335	GPU
336	GPU
369	GPU
417	GPU
429	GPU
471	GPU
473	GPU
475	GPU
488	GPU
488	GPU
502	GPU
513	GPU
521	GPU
521	GPU
529	GPU
550	GPU
552	GPU
555	GPU
558	GPU
565	GPU
578	GPU
592	GPU
592	GPU
601	GPU
605	GPU
609	GPU
610	GPU
613	GPU
617	GPU
619	GPU
631	GPU
632	GPU
640	GPU
641	GPU
641	GPU
651	GPU
657	GPU
658	GPU
665	GPU
676	GPU
680	GPU
692	GPU
700	GPU
713	GPU
718	GPU
719	GPU
723	GPU
738	GPU
752	GPU
754	GPU
798	GPU
802	GPU
846	GPU
859	GPU
944	GPU
945	GPU
952	GPU
954	GPU
968	GPU
976	GPU
979	GPU
1010	GPU
1020	GPU
1060	GPU
1070	GPU
1070	GPU
1070	GPU
1070	GPU
1080	GPU
1090	GPU
1090	GPU
1150	GPU
1160	GPU
1190	GPU
1200	GPU
1210	GPU
1210	GPU
1270	GPU
1340	GPU
1520	GPU
1550	GPU
1560	GPU
1580	GPU
1580	GPU
1610	GPU
1620	GPU
1630	GPU
1650	GPU
1660	GPU
1720	GPU
1730	GPU
1790	GPU
1830	GPU
2350	GPU
2400	GPU
2410	GPU
2460	GPU
2570	GPU
2570	GPU
2670	GPU
2760	GPU
2820	GPU
2880	GPU
2920	GPU
2960	GPU
3050	GPU
3110	GPU
3530	GPU
3580	GPU
4040	GPU
4160	GPU
4220	GPU
4280	GPU
4350	GPU
4940	GPU
5550	GPU
5600	GPU
5710	GPU
7990	GPU
8070	GPU
8170	CPU
10270	CPU
11600	CPU
15140	CPU
22240	CPU
23990	CPU
24120	CPU
26010	CPU
26300	CPU
27050	CPU
27080	GPU
29880	CPU
30790	CPU
33680	CPU
33990	CPU
34940	CPU
35240	CPU
35700	CPU
38420	CPU
38790	CPU
42830	CPU
44830	CPU
45420	CPU
45940	CPU
46610	CPU
47140	CPU
49800	CPU
58230	CPU
59670	CPU
61510	CPU
64220	CPU
64670	CPU
64879	CPU
65040	CPU
66600	CPU
70720	CPU
78020	CPU
81350	CPU
81740	CPU
84330	CPU
86830	CPU
87080	CPU
89140	CPU
94400	CPU
111060	CPU
116840	CPU
117370	CPU
117570	CPU
122840	CPU
126790	CPU
136080	CPU
145260	CPU
183560	CPU
185910	CPU
195980	CPU
206650	CPU
213280	CPU
242770	CPU
243740	CPU
308340	CPU
370380	CPU
423430	CPU"""

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
plt.savefig('ttft_vs_value_index.png', dpi=300, bbox_inches='tight')
