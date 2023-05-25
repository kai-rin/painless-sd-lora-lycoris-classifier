import os
import json
import shutil

def organize_files():
    directory = os.getcwd()

    # Create dictionaries to store the file names for each type
    lora_files = {}
    lyco_files = {}

    # Create directories if they don't exist
    lora_dir = os.path.join(directory, 'Lora')
    lyco_dir = os.path.join(directory, 'LyCORIS')
    os.makedirs(lora_dir, exist_ok=True)
    os.makedirs(lyco_dir, exist_ok=True)

    # Iterate over all files in the directory
    for file_name in os.listdir(directory):
        # If the file is a .info file
        if file_name.endswith('.info'):
            # Get the root name of the file
            root_name = file_name.split('.')[0]
            # Open the file
            with open(os.path.join(directory, file_name), 'r') as file:
                # Load the json
                data = json.load(file)
                # Check the type and add the root name to the corresponding dictionary
                if data.get('model', {}).get('type') == 'LORA':
                    lora_files[root_name] = set(lora_files.get(root_name, [])) | {file_name}
                elif data.get('model', {}).get('type') == 'LoCon':
                    lyco_files[root_name] = set(lyco_files.get(root_name, [])) | {file_name}

    # Go over the directory again and add any file that matches the root name
    for file_name in os.listdir(directory):
        root_name = file_name.split('.')[0]
        if root_name in lora_files:
            lora_files[root_name] = lora_files.get(root_name) | {file_name}
        elif root_name in lyco_files:
            lyco_files[root_name] = lyco_files.get(root_name) | {file_name}

    # Move files to the appropriate directory
    for root_name, files in lora_files.items():
        for file_name in files:
            shutil.move(os.path.join(directory, file_name), os.path.join(lora_dir, file_name))

    for root_name, files in lyco_files.items():
        for file_name in files:
            shutil.move(os.path.join(directory, file_name), os.path.join(lyco_dir, file_name))

    # Generate the output
    output = 'LORA:\n'
    for files in lora_files.values():
        for file_name in sorted(files):
            output += '\t' + file_name + '\n'
    output += 'LyCORIS:\n'
    for files in lyco_files.values():
        for file_name in sorted(files):
            output += '\t' + file_name + '\n'

    # Write the output to the file
    with open('lora_lyco_classifier.log', 'w') as output_file:
        output_file.write(output)


if __name__ == "__main__":
    organize_files()
