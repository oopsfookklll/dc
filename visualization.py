import matplotlib.pyplot as plt
from color_range import color_map, color_range

def visualize_data(data, canvas):
    fig, ax = plt.subplots()
    for i in range(len(data)):
        ax.bar(i, data[i], color=color_map(color_range, data[i]))
    ax.set_xlabel('Count')
    ax.set_ylabel('Frequency')
    ax.set_title('Count Field Value Distribution')
    plt.savefig(canvas)

def update_visualization(data, canvas):
    plt.clf()
    visualize_data(data, canvas)