import pandas as pd
import matplotlib.pyplot as plt
from dataclasses import dataclass, field
from matplotlib.patches import Patch

models = [
    ("Llama 3.2 1B Instruct", "Q4_K - Medium", "1B"),
    ("Meta Llama 3.1 8B Instruct", "Q4_K - Medium", "8B"),
    ("Qwen2.5 14B Instruct", "Q4_K - Medium", "14B")]

metrics = [
    ("ttft", "Time to first token", "[ms]", "ascending", 3000),
    ("prompt_tps", "Prompt processing", "[tokens/s]", "descending", 0),
    ("gen_tps", "Token generation", "[tokens/s]", "descending", 0),
    ("localscore", "LocalScore", "", "descending", 0),
    ]

@dataclass
class ChartInfo:
    model_name: str = field(default="")
    model_quant: str = field(default="")
    model_size: str = field(default="")
    metric_name: str = field(default="")
    metric_label: str = field(default="")
    metric_unit: str = field(default="")
    metric_sort_dir: str = field(default="ascending")
    metric_threshold: int = field(default=0)

accel_group_colors = {
    "NVIDIA GPU":   "#76b900",
    "AMD GPU":      "#ed1c24",
    "Apple GPU":    "#000000",
    "Apple CPU":    "#555555",
    "AMD CPU":      "#f26522",
    "Intel CPU":    "#0068b5",
    "Other":        "#e0e0e0" }

def get_accel_group(accel_type, accel_name) -> str:
    """ Get the accelerator group based on type and name """
    if accel_type == 'GPU':
        if (accel_name.startswith('NVIDIA') or
            accel_name.startswith('Tesla') or
            accel_name.startswith('Quadro')):
            return 'NVIDIA GPU'
        elif (accel_name.startswith('AMD') or
              accel_name.startswith('Radeon')):
            return 'AMD GPU'
        elif accel_name.startswith('Apple'):
            return 'Apple GPU'
    elif accel_type == 'CPU':
        if accel_name.startswith('Apple'):
            return 'Apple CPU'
        elif accel_name.startswith('AMD'):
            return 'AMD CPU'
        elif accel_name.startswith('Intel'):
            return 'Intel CPU'
    return 'Other'

def create_chart(df_all, chart: ChartInfo):
    df_model = df_all[(df_all['model_name'] == chart.model_name) &
                      (df_all['model_quant'] == chart.model_quant)]
    df_model = df_model.sort_values(by=chart.metric_name,
                        ascending=chart.metric_sort_dir == "ascending")
    df = df_model[[chart.metric_name, 'accel_group']]
    df_model.to_csv(f'localscore.{chart.metric_name}.{chart.model_size}.tsv',
                    sep='\t', index=False)

    # Create the bar chart
    plt.figure(figsize=(15, 8))
    value_indexes = range(len(df))
    colors = [
        accel_group_colors.get(accel, accel_group_colors['Other'])
        for accel in df['accel_group']]
    bars = plt.bar(value_indexes, df[chart.metric_name], color=colors, alpha=0.7)

    # Customize the chart
    plt.xlabel('Value Index')
    plt.ylabel(f"{chart.metric_label} {chart.metric_unit}")
    plt.yscale('log')
    smaller_or_larger = "smaller" if chart.metric_sort_dir == "ascending" else "larger"
    plt.title(f'{chart.model_name} {chart.model_quant}: {chart.metric_label} '
              f'by accelerator type {smaller_or_larger} is better)')
    plt.grid(True, which='both', axis='both', alpha=0.3, ls="-")

    # add threshold line if applicable
    if chart.metric_threshold > 0:
        plt.axhline(y=chart.metric_threshold, color='red', linestyle='-', linewidth=0.5,
                    label=f'Threshold ({chart.metric_threshold})')

    # Create legend matching the accel_group_colors used in the plot
    used_groups = df['accel_group'].unique()
    legend_elements = [
        Patch(facecolor=accel_group_colors[group], alpha=0.7, label=group)
        for group in used_groups
    ]
    plt.legend(handles=legend_elements)

    plt.tight_layout()
    plt.savefig(f'localscore.{chart.metric_name}.{chart.model_size}.png',
                dpi=300, bbox_inches='tight')

if __name__ == "__main__":
    df_all = pd.read_csv("localscore_leaderboard.tsv", sep='\t', na_filter=False)
    df_all = df_all[df_all['ttft'] < 1_000_000] # remove outliers
    df_all['accel_group'] = df_all.apply(
        lambda row: get_accel_group(row['accel_type'], row['accel_name']), axis=1)

    charts = [
        ChartInfo(
            model_name=model[0],
            model_quant=model[1],
            model_size=model[2],
            metric_name=metric[0],
            metric_label=metric[1],
            metric_unit=metric[2],
            metric_sort_dir=metric[3],
            metric_threshold=metric[4])
        for model in models for metric in metrics]

    for chart in charts:
        create_chart(df_all, chart)

