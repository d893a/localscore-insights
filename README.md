# LocalScore leaderboard analytics

LocalScore leaderboard: [LocalScore](https://www.localscore.ai/latest)

All benchmark results: [localscore_leaderboard.csv](localscore_leaderboard.csv) (Currently 1218 in total.)

## Time to first token

The figure below shows the benchmarks results for the 14 B parameter model, ordered by time-to-first-token values. GPUs: 146 to 2720 ms (~19x span). CPUs: 5560 to 298,080 ms (~54x span; 1 outlier removed from the data). \
localscore_leaderboard.q4_k_med.14B.sorted_by_ttft.csvData [localscore_leaderboard.q4_k_med.14B.sorted_by_ttft.csv](localscore_leaderboard.q4_k_med.14B.sorted_by_ttft.csv)

![ttft_vs_value_index.14B.png](ttft_vs_value_index.14B.png)

## Prompt processing

### 14 B parameter model

Prompt processing throughput for the 14 B parameter model. GPUs: 5126 down to 204 tokens/s (~25x span). CPUs: 171 to 3 tokens/s (~57x span). \
Data: [localscore_leaderboard.q4_k_med.14B.sorted_by_pp_tps.csv](localscore_leaderboard.q4_k_med.14B.sorted_by_pp_tps.csv)

![pp_tps_vs_value_index.14B.png](pp_tps_vs_value_index.14B.png)

### 8 B parameter model

Prompt processing throughput for the 8 B parameter model. GPUs: 8479 down to 427 tokens/s (~20x span). CPUs: 250 to 1 token/s. \
Data: [localscore_leaderboard.q4_k_med.8B.llama3.1.sorted_by_pp_tps.csv](localscore_leaderboard.q4_k_med.8B.llama3.1.sorted_by_pp_tps.csv)

![pp_tps_vs_value_index.8B.png](pp_tps_vs_value_index.8B.png)

### 1.5 B parameter model

Prompt processing throughput for the 1.5 B parameter model. GPUs: 30,896 down to 1470 tokens/s (~20x span). CPUs: 1738 to 2 token/s. \
Data: [localscore_leaderboard.q4_k_med.1.5B.sorted_by_pp_tps.csv](localscore_leaderboard.q4_k_med.1.5B.sorted_by_pp_tps.csv)

![pp_tps_vs_value_index.1.5B.png](pp_tps_vs_value_index.1.5B.png)
