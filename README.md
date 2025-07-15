# LocalScore leaderboard analytics

LocalScore leaderboard: [LocalScore](https://www.localscore.ai/latest)

All benchmark results: [localscore_leaderboard.csv](localscore_leaderboard.csv) (Currently 1218 in total.)

## Time to first token

The performance is primarily determined by the memory bandwidth of the GPU/CPU. GPUs have an order of magnitude larger memory bandwidth. A few GPU's VRAM is almost as slow as CPUs' system RAM.

### 14 B parameter model

The figure below shows the benchmarks results for the 14 B parameter model, ordered by time-to-first-token values. GPUs: 146 to 2720 ms (~19x span). CPUs: 5560 to 298,080 ms (~54x span; 1 outlier removed from the data).  \
Data: [localscore_leaderboard.q4_k_med.14B.sorted_by_ttft.csv](localscore_leaderboard.q4_k_med.14B.sorted_by_ttft.csv)

![ttft_vs_value_index.14B.png](ttft_vs_value_index.14B.png)

## Prompt processing

Prompt processing is primarily determined by the processing units' tensor multiplication-and-add throughput. GPUs have more processing units -- especially dedicated tensor cores -- this contributes the most to the overall performance. CPUs in general do not have sufficient number of cores to parallelize the computation.

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

## Observations

The following are the best among the GPUs:

-   NVIDIA RTX PRO 6000 Blackwell Workstation Edition 95 GB
-   NVIDIA RTX 6000 Ada Generation 47 GB
-   NVIDIA GeForce RTX 5090 31 GB
-   NVIDIA GeForce RTX 4090 24 GB
-   NVIDIA GeForce RTX 4090 D 47 GB
-   NVIDIA RTX 6000 Ada Generation 48 GB

The following GPUs are good value, and perform really well:

-   NVIDIA GeForce RTX 5070 Ti 15 GB
-   NVIDIA GeForce RTX 4080 SUPER 16 GB
-   NVIDIA GeForce RTX 4070 Ti SUPER 16 GB
-   NVIDIA GeForce RTX 4070 Ti 12 GB
-   NVIDIA GeForce RTX 3090 Ti 24 GB
-   NVIDIA GeForce RTX 3090 24 GB
-   NVIDIA GeForce RTX 3080 Ti 12 GB

There are only a few AMD GPUs which show notabele performance in these benchmarks:

-   AMD Radeon RX 6900 XT 16 GB
-   AMD Radeon PRO V620 30 GB
-   AMD Radeon RX 7900 XTX 24 GB
-   AMD Radeon RX 6800 XT 16 GB
-   AMD Radeon RX 6700 XT 12 GB
-   AMD Radeon RX 6650 XT 8 GB
-   AMD Radeon RX 9070 XT 16 GB
-   AMD Radeon RX 7800 XT 16 GB
-   AMD Radeon RX 6600 8 GB

Some processors can approach the performance of weaker GPUs:

AMD Ryzen Threadripper PRO 7995WX (znver4)
AMD EPYC 9454P 48-Core Processor (znver4)
AMD Ryzen 9 9950X 16-Core Processor
AMD Ryzen 9 7950X3D 16-Core Processor (znver4)

AMD EPYC 9454P 48-Core Processor (znver4)
AMD EPYC 9135 16-Core Processor
AMD Ryzen 9 9950X3D 16-Core Processor
AMD Ryzen 9 7950X3D 16-Core Processor (znver4)


AMD Ryzen Threadripper PRO 7995WX (znver4)
AMD EPYC 9454P 48-Core Processor (znver4)
AMD Radeon RX 7600 XT
AMD Ryzen 9 9950X 16-Core Processor
AMD Ryzen 9 7950X3D 16-Core Processor (znver4)
AMD Ryzen 9 5950X 16-Core Processor (znver3)
AMD Ryzen 9 5950X 16-Core Processor (znver3)
