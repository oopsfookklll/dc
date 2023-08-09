import color_range
import data_processing
import visualization

def main():
    raw_data = open('count_values.txt', 'r').readlines()
    processed_data = data_processing.process_data(raw_data)
    color_map = color_range.color_map
    color_range_data = color_range.color_range
    visualization_data = visualization.visualize_data(processed_data, color_map, color_range_data)
    visualization.update_visualization('canvas', visualization_data)

if __name__ == "__main__":
    main()