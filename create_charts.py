import pandas as pd
import matplotlib.pyplot as plt

models = [
    "Llama 3.2 1B Instruct",
    "Meta Llama 3.1 8B Instruct",
    "Qwen2.5 14B Instruct"]

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

def create_chart(model_name):
    # filter models[2]
    df_model = df_all[df_all['model_name'] == model_name]

    # filter 'prompt_tps', 'accel_group'
    df = df_model[['prompt_tps', 'accel_group']]

    # sort by 'prompt_tps'
    df = df.sort_values(by='prompt_tps', ascending=False)

    # Create value indexes (0 to len(df)-1)
    value_indexes = range(len(df))

    colors = [accel_group_colors.get(accel, 'lightgray') for accel in df['accel_group']]

    # Create the bar chart
    plt.figure(figsize=(15, 8))
    bars = plt.bar(value_indexes, df['prompt_tps'], color=colors, alpha=0.7)

    # Customize the chart
    plt.xlabel('Value Index')
    plt.ylabel('Prompt processing [tokens/s]')
    plt.yscale('log')
    plt.title('14B Prompt Processing vs Value Index by Accelerator Type')
    plt.grid(True, which='both', axis='both', alpha=0.3, ls="-")


    # Create legend matching the accel_group_colors used in the plot
    from matplotlib.patches import Patch
    used_groups = df['accel_group'].unique()
    legend_elements = [
        Patch(facecolor=accel_group_colors[group], alpha=0.7, label=group)
        for group in used_groups
    ]
    plt.legend(handles=legend_elements)


    # Adjust layout and show
    plt.tight_layout()
    # plt.show()

    #save result to png file
    plt.savefig('localscore.pp_tps.14B.png', dpi=300, bbox_inches='tight')

if __name__ == "__main__":
    # Read the data into a pandas DataFrame, empty cells will be ''
    df_all = pd.read_csv("localscore_leaderboard.tsv", sep='\t', na_filter=False)

    # add accelerator group
    df_all['accel_group'] = df_all.apply(
        lambda row: get_accel_group(row['accel_type'], row['accel_name']), axis=1)

    create_chart(models[2])  # Create chart for the 14B model

