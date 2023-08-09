1. "count_values": This is the data schema that will be shared across all files. It represents the range of Count field values that the user wants to color.

2. "color_map": This is a function that will be used in both "color_range.py" and "visualization.py". It takes a count value and returns a color from dark red to dark green.

3. "color_range": This is a variable that will be exported from "color_range.py" and used in "main.py" and "visualization.py". It represents the mapping from count values to colors.

4. "process_data": This is a function that will be used in both "data_processing.py" and "main.py". It takes raw data and returns it in a format that can be used by the color_map function.

5. "visualize_data": This is a function that will be used in both "visualization.py" and "main.py". It takes processed data and visualizes it with the appropriate colors.

6. "data": This is a variable that will be exported from "data_processing.py" and used in "main.py" and "visualization.py". It represents the processed data that is ready for visualization.

7. "canvas": This is the id name of the DOM element that the JavaScript functions will use to display the visualization.

8. "update_visualization": This is the message name that will be used to trigger the visualization update when the data changes.