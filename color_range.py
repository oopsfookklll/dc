import matplotlib.pyplot as plt

def color_map(value):
    color_range = plt.get_cmap('RdYlGn')
    return color_range(value)

color_range = {i: color_map(i/100.0) for i in range(101)}