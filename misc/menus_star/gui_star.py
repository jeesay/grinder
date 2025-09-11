def process_file(file_path):
    # Lists to store the results
    initialise_lines = []
    joboptions_lines_split = []

    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Check if the line contains 'initialise'
            if 'initialise' in line:
                init_tool = line.strip().split('(')[0]

            # Check if the line contains 'joboptions'
            if 'joboptions' in line:
                # Split the line into words separated by commas
                split_line = [init_tool] + line.strip().split(',')
                joboptions_lines_split.append(split_line)

    return joboptions_lines_split

# Example usage
file_path = 'pipeline_jobs.cpp'  # Replace with your file path
joboptions_lines_split = process_file(file_path)

print("\nLines containing 'joboptions' split by commas:")
for split_line in joboptions_lines_split:
    print(split_line)

