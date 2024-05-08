# import subprocess
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Function to run the program and capture output
# def run_program():
#     # Adjust the command if your executable requires different handling
#     result = subprocess.run(['./execute1'], capture_output=True, text=True)
#     return result.stdout

# # Main function to collect data
# def collect_data(runs=1000):
#     data = {'Hit': [], 'Miss': [], 'In': [], 'Out': []}
#     for _ in range(runs):
#         output = run_program()
#         # Example output parsing: "hit:91 miss:553 in:108 out:90"
#         hit_val = int(output.split('hit:')[1].split()[0])
#         miss_val = int(output.split('miss:')[1].split()[0])
#         in_val = int(output.split('in:')[1].split()[0])
#         out_val = int(output.split('out:')[1].split()[0])
#         data['Hit'].append(hit_val)
#         data['Miss'].append(miss_val)
#         data['In'].append(in_val)
#         data['Out'].append(out_val)
#     return pd.DataFrame(data)

# # Generate and plot data
# data = collect_data()

# # Creating multiple plots with a smaller figure size
# fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # Smaller figure size

# # Plotting histograms for each variable
# sns.histplot(data['Hit'], kde=False, bins=50, ax=axs[0, 0])
# axs[0, 0].set_title('Histogram of "Hit" Values')

# sns.histplot(data['Miss'], kde=False, bins=50, ax=axs[0, 1])
# axs[0, 1].set_title('Histogram of "Miss" Values')

# sns.histplot(data['In'], kde=False, bins=50, ax=axs[1, 0])
# axs[1, 0].set_title('Histogram of "In" Values')

# sns.histplot(data['Out'], kde=False, bins=50, ax=axs[1, 1])
# axs[1, 1].set_title('Histogram of "Out" Values')

# plt.tight_layout()
# plt.show()


import subprocess
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to run the program and capture output
def run_program():
    # Adjust the command if your executable requires different handling
    result = subprocess.run(['./execute1'], capture_output=True, text=True)
    return result.stdout

# Main function to collect data
def collect_data(runs=100):
    data = {'Hit': [], 'Miss': [], 'In': [], 'Out': []}
    for _ in range(runs):
        output = run_program()
        # Example output parsing: "hit:91 miss:553 in:108 out:90"
        hit_val = int(output.split('hit:')[1].split()[0])
        miss_val = int(output.split('miss:')[1].split()[0])
        in_val = int(output.split('in:')[1].split()[0])
        out_val = int(output.split('out:')[1].split()[0])
        data['Hit'].append(hit_val)
        data['Miss'].append(miss_val)
        data['In'].append(in_val)
        data['Out'].append(out_val)
    return pd.DataFrame(data)

# Generate and plot data
data = collect_data()

# Creating multiple plots with a smaller figure size
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # Smaller figure size

# Plotting histograms for each variable and annotating
for i, (ax, column) in enumerate(zip(axs.flatten(), data.columns)):
    sns.histplot(data[column], kde=False, bins=50, ax=ax)
    ax.set_title(f'')

    # Find the bin with the highest count
    max_height = 0
    max_bin_center = 0
    for patch in ax.patches:
        if patch.get_height() > max_height:
            max_height = patch.get_height()
            max_bin_center = patch.get_x() + patch.get_width() / 2

    # Annotate the highest bin with count and x-axis value
    annotation_text = f'Max count: {int(max_height)} at {max_bin_center:.2f}'
    ax.annotate(annotation_text, 
                xy=(max_bin_center, max_height), 
                xytext=(0, 10),  # 10 points vertical offset
                textcoords='offset points',
                ha='center', va='bottom')

plt.tight_layout()
plt.show()
