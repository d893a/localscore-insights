# LocalScore insights

LocalScore benchmark results: [LocalScore](https://www.localscore.ai/latest)

Benchmark results downloaded: [localscore_leaderboard.tsv](localscore_leaderboard.tsv) (Currently 1218 in total.) ([Code](localscore_download_leaderboard.bat))

The benchmark results are shown in the following charts. ([Code](create_charts.py))

## Time to first token

Performance is primarily determined by the memory bandwidth of the GPU/CPU. GPUs have an order of magnitude larger memory bandwidth. A few GPUs' VRAM is almost as slow as CPUs' system RAM.

In the charts a threshold of 3 seconds was chosen arbitrarily as an upper limit for good performance for creating the first token. (Indicated by a red line.)

### 14B parameter model: Qwen2.5 14B Instruct Q4_K - Medium

Data: [localscore.ttft.14B.tsv](localscore.ttft.14B.tsv)

![localscore.ttft.14B.png](localscore.ttft.14B.png)

The figure shows the time-to-first-token benchmark results for the 14 B parameter model.

-   NVIDIA GPUs (<span style="color:#76b900;">&#9632;</span>): 146 to 1830 ms, with older/less performant ones into the 8 s range.
-   Apple GPUs  (<span style="color:#000000;">&#9632;</span>): 2029 ms to 20 seconds, with a few into the 30 seconds range.
-   AMD GPUs    (<span style="color:#ed1c24;">&#9632;</span>): 2.4 to 5 seconds. (Plus a poorly performing outlier at 27 seconds.)
-   AMD CPUs    (<span style="color:#f26522;">&#9632;</span>): 8.3 to 78 seconds, with the majority above 20 seconds.
-   Intel CPUs  (<span style="color:#0068b5;">&#9632;</span>): 24 seconds to 7 minutes, with the majority above 1.5 minutes.
-   All other hardware performed poorly.

The Apple GPUs seem to aim to fill the gap between the performance of NVIDIA GPUs and AMD CPUs.

Best performing NVIDIA GPUs: `cat localscore.ttft.14B.tsv | grep "NVIDIA GPU" | awk -F"\t" "!seen[$12]++" | cut -f4,12`

-   Top performers (ttft < 500 ms):
    | ttft [ms] | accel_name                                         | VRAM [GB] |
    |-----------|----------------------------------------------------|-----------|
    | 245       | NVIDIA RTX PRO 6000 Blackwell Workstation Edition  | 95.0      |
    | 279       | NVIDIA GeForce RTX 5090                            | 31.0      |
    | 322       | NVIDIA GeForce RTX 4090                            | 24.0      |
    | 336       | NVIDIA GeForce RTX 4090 D                          | 47.0      |
    | 369       | NVIDIA RTX 6000 Ada Generation                     | 47.0      |
    | 417       | NVIDIA H100 PCIe                                   | 79.0      |
    | 475       | NVIDIA H100 80GB HBM3                              | 79.0      |
    | 488       | NVIDIA GeForce RTX 4080                            | 16.0      |
    | 488       | NVIDIA L40S                                        | 45.0      |

-   Mid-tier NVIDIA GPUs (500 ms <= ttft < 2 seconds):
    | ttft [ms] | accel_name                                   | VRAM [GB] |
    |-----------|----------------------------------------------|-----------|
    | 513       | NVIDIA L40                                   | 44.0      |
    | 521       | NVIDIA GeForce RTX 4070 Ti SUPER             | 16.0      |
    | 529       | NVIDIA H100 NVL                              | 93.0      |
    | 552       | NVIDIA GeForce RTX 3090 Ti                   | 24.0      |
    | 555       | NVIDIA GeForce RTX 4080 SUPER                | 16.0      |
    | 558       | NVIDIA GeForce RTX 5080                      | 15.0      |
    | 578       | NVIDIA GeForce RTX 3090                      | 24.0      |
    | 592       | NVIDIA A100-SXM4-80GB                        | 79.0      |
    | 609       | NVIDIA GeForce RTX 4070 Ti                   | 12.0      |
    | 617       | NVIDIA GeForce RTX 3080 Ti                   | 12.0      |
    | 665       | NVIDIA GeForce RTX 4070 SUPER                | 12.0      |
    | 692       | NVIDIA RTX A6000                             | 48.0      |
    | 713       | NVIDIA A40                                   | 44.0      |
    | 752       | NVIDIA GeForce RTX 4070                      | 12.0      |
    | 802       | NVIDIA GeForce RTX 3080                      | 10.0      |
    | 846       | NVIDIA RTX A5000                             | 24.0      |
    | 859       | NVIDIA GeForce RTX 5070 Ti                   | 15.0      |
    | 944       | NVIDIA GeForce RTX 5060 Ti                   | 15.0      |
    | 952       | NVIDIA RTX 4000 Ada Generation               | 20.0      |
    | 954       | NVIDIA A100 80GB PCIe                        | 79.0      |
    | 968       | NVIDIA RTX 3500 Ada Generation Laptop GPU    | 12.0      |
    | 979       | NVIDIA RTX A4500                             | 20.0      |
    | 1020      | Tesla V100-SXM2-32GB                         | 32.0      |
    | 1060      | Quadro RTX 8000                              | 47.0      |
    | 1070      | NVIDIA GeForce RTX 4060 Ti                   | 16.0      |
    | 1070      | NVIDIA GeForce RTX 5070                      | 12.0      |
    | 1070      | NVIDIA GeForce RTX 2080 Ti                   | 11.0      |
    | 1160      | NVIDIA A10                                   | 22.0      |
    | 1190      | NVIDIA RTX A4000                             | 16.0      |
    | 1210      | NVIDIA TITAN V                               | 12.0      |
    | 1210      | NVIDIA L4                                    | 22.0      |
    | 1340      | NVIDIA RTX 4000 SFF Ada Generation           | 20.0      |
    | 1520      | NVIDIA GeForce RTX 3080 Laptop GPU           | 16.0      |
    | 1550      | NVIDIA RTX A5000 Laptop GPU                  | 16.0      |
    | 1560      | NVIDIA GeForce RTX 3060                      | 12.0      |
    | 1790      | NVIDIA RTX 2000 Ada Generation               | 16.0      |

-   NVIDIA GPUs an par with other hardware:
    | ttft [ms] | accel_name                      | VRAM [GB] |
    |-----------|---------------------------------|-----------|
    | 2410      | NVIDIA RTX A2000 12GB           | 12.0      |
    | 2760      | Tesla T4                        | 15.0      |
    | 2820      | NVIDIA GeForce GTX 1080 Ti      | 11.0      |
    | 4280      | Quadro P5000                    | 16.0      |
    | 5550      | NVIDIA GeForce RTX 3060 Ti      | 8.0       |
    | 5710      | Tesla P100-SXM2-16GB            | 16.0      |
    | 8070      | NVIDIA GeForce RTX 3070         | 8.0       |




### 8B parameter model: Meta Llama 3.1 8B Instruct Q4_K - Medium

The figure below shows the time-to-first-token benchmark results for the 8 B parameter model.
Data: [localscore.ttft.8B.tsv](localscore.ttft.8B.tsv)

![localscore.ttft.8B.png](localscore.ttft.8B.png)

### 1B parameter model: Llama 3.2 1B Instruct Q4_K - Medium

The figure below shows the benchmark results for the 1B parameter model, ordered by time-to-first-token values.
Data: [localscore.ttft.1B.tsv](localscore.ttft.1B.tsv)

![localscore.ttft.1B.png](localscore.ttft.1B.png)


## Prompt processing

Prompt processing is primarily determined by the processing units' tensor multiplication-and-add throughput. GPUs have more processing units -- especially dedicated tensor cores -- this contributes the most to the overall performance. CPUs in general do not have sufficient number of cores to parallelize the computation.

### 14 B parameter model

Prompt processing throughput for the 14 B parameter model. GPUs: 5126 down to 204 tokens/s (~25x span). CPUs: 171 to 3 tokens/s (~57x span). \
Data: [localscore_leaderboard.q4_k_med.14B.sorted_by_pp_tps.tsv](localscore_leaderboard.q4_k_med.14B.sorted_by_pp_tps.tsv)

![pp_tps_vs_value_index.14B.png](pp_tps_vs_value_index.14B.png)

### 8 B parameter model

Prompt processing throughput for the 8 B parameter model. GPUs: 8479 down to 427 tokens/s (~20x span). CPUs: 250 to 1 token/s. \
Data: [localscore_leaderboard.q4_k_med.8B.llama3.1.sorted_by_pp_tps.tsv](localscore_leaderboard.q4_k_med.8B.llama3.1.sorted_by_pp_tps.tsv)

![pp_tps_vs_value_index.8B.png](pp_tps_vs_value_index.8B.png)

### 1.5 B parameter model

Prompt processing throughput for the 1.5 B parameter model. GPUs: 30,896 down to 1770 tokens/s (~20x span). CPUs: 1738 to 2 tokens/s. \
Data: [localscore_leaderboard.q4_k_med.1.5B.sorted_by_pp_tps.tsv](localscore_leaderboard.q4_k_med.1.5B.sorted_by_pp_tps.tsv)

![pp_tps_vs_value_index.1.5B.png](pp_tps_vs_value_index.1.5B.png)

## Observations

### GPUs

These are the best GPUs:

-   NVIDIA RTX PRO 6000 Blackwell Workstation Edition 95 GB
-   NVIDIA RTX 6000 Ada Generation 47 GB
-   NVIDIA GeForce RTX 5090 31 GB
-   NVIDIA GeForce RTX 4090 24 GB
-   NVIDIA GeForce RTX 4090 D 47 GB
-   NVIDIA RTX 6000 Ada Generation 48 GB

The following GPUs are good value and perform really well:

-   NVIDIA GeForce RTX 5070 Ti 15 GB
-   NVIDIA GeForce RTX 4080 SUPER 16 GB
-   NVIDIA GeForce RTX 4070 Ti SUPER 16 GB
-   NVIDIA GeForce RTX 4070 Ti 12 GB
-   NVIDIA GeForce RTX 3090 Ti 24 GB
-   NVIDIA GeForce RTX 3090 24 GB
-   NVIDIA GeForce RTX 3080 Ti 12 GB

There are only a few AMD GPUs which show notable performance in the current benchmarks:

-   AMD Radeon RX 6900 XT 16 GB
-   AMD Radeon PRO V620 30 GB
-   AMD Radeon RX 7900 XTX 24 GB
-   AMD Radeon RX 6800 XT 16 GB
-   AMD Radeon RX 6700 XT 12 GB
-   AMD Radeon RX 6650 XT 8 GB
-   AMD Radeon RX 9070 XT 16 GB
-   AMD Radeon RX 7800 XT 16 GB
-   AMD Radeon RX 6600 8 GB

### CPUs

Some processors can approach the performance of weaker GPUs:

-   AMD Ryzen Threadripper PRO 7995WX (znver4)
-   AMD EPYC 9454P 48-Core Processor (znver4)
-   AMD Ryzen 9 9950X 16-Core Processor
-   AMD Ryzen 9 7950X3D 16-Core Processor (znver4)
-   AMD Ryzen 9 9950X3D 16-Core Processor
-   AMD Ryzen 9 7950X 16-Core Processor (znver4)

Note that even these processors are an order of magnitude slower at prompt processing than the average GPU.

### Hybrid system

The benchmark results show a hybrid system, too. [Test #337](https://www.localscore.ai/result/337) features an AMD Ryzen 7 7800X3D 8-Core Processor (znver4) with 32 GB of system RAM, plus an NVIDIA GeForce RTX 4060 Ti with 8 GB VRAM. The model under test is *Qwen2.5 14B Instruct Q4_K - Medium* with 14.8B parameters. The file size is 8,988,110,976 bytes, which does not fit into the GPU memory.

The results are shown in the following table:

| TEST NAME      | PROMPT (tokens/s) | GENERATION (tokens/s) | TTFT       |
|----------------|------------------:|----------------------:|------------|
| pp1024+tg16    |               136 |                   3.9 | 7.82 sec   |
| pp4096+tg256   |                86 |                   2.9 | 47.96 sec  |
| pp2048+tg256   |               545 |                   3.6 | 4.03 sec   |
| pp2048+tg768   |               527 |                   3.4 | 4.17 sec   |
| pp1024+tg1024  |               538 |                   3.6 | 2.18 sec   |
| pp1280+tg3072  |               426 |                   3.0 | 3.33 sec   |
| pp384+tg1152   |               430 |                   3.7 | 1.22 sec   |
| pp64+tg1024    |               205 |                   3.8 | 578 ms     |
| pp16+tg1536    |                49 |                   3.6 | 606 ms     |

[Test #320](https://www.localscore.ai/result/320) runs the same model on the same system, but this time without the GPU. Only the CPU is used for prompt processing and token generation. The results are shown below:

| TEST NAME      | PROMPT (tokens/s) | GENERATION (tokens/s) | TTFT      |
|----------------|------------------:|----------------------:|-----------|
| pp1024+tg16    |               38  |                  5.8  | 27.08 sec |
| pp4096+tg256   |               34  |                  5.1  | 120.12 sec|
| pp2048+tg256   |               40  |                  5.6  | 52.01 sec |
| pp2048+tg768   |               39  |                  5.5  | 52.12 sec |
| pp1024+tg1024  |               41  |                  5.7  | 25.01 sec |
| pp1280+tg3072  |               39  |                  5.4  | 32.66 sec |
| pp384+tg1152   |               40  |                  5.8  | 9.74 sec  |
| pp64+tg1024    |               37  |                  5.9  | 1.87 sec  |
| pp16+tg1536    |               32  |                  5.8  | 670 ms    |

In the case of the hybrid GPU+CPU setup, the prompt processing throughput varies between 49 and 545 tokens/s, mostly around 200–500 tokens/s. The time to first token falls between 578 ms and 7.82 seconds -- the only exception is the simulated RAG operation (pp4096+tg256), in which case it takes 47.96 sec to generate the first token. The output is generated at a rate of 3–4 tokens/s.

In the CPU-only case, the prompt processing throughput is uniformly around 30–40 tokens/s. The time to get the first token depends on the length of the input, ranging from 670 ms to 52.12 seconds. Again, the notable exception is the (pp4096+tg256) case, which takes 120.12 seconds to produce the first token. The CPU-only method takes 8–12 times more time to generate the first token (with the exception of pp4096+tg256, which takes 2.5 times as long).

The situation is reversed for token generation. The CPU-only method produces output at a rate of 5-6 tokens/s -- around 1.6 faster than the GPU+CPU method.

The slow token generation of the GPU+CPU method may be attributed to the extra time needed to move the model weights from the system RAM into the VRAM again and again for each generated token. For prompt processing, the required time is determined by the size of the input prompt and dominated by the available computational power rather than the memory bandwidth.

In conclusion, a GPU with even a small amount of VRAM can contribute positively to the overall system performance.
