import os

def organize_files_by_extension(output_dir='file_lists'):
    # Get the current working directory
    current_dir = os.getcwd()
    
    # Dictionary to store file names by extension
    files_by_extension = {}
    
    # Walk through the directory
    for root, _, files in os.walk(current_dir):
        for file in files:
            # Extract the file extension
            file_extension = os.path.splitext(file)[1].lower()  # Get extension in lowercase
            if file_extension:  # Skip files with no extensions
                # Add the file to the appropriate extension list
                if file_extension not in files_by_extension:
                    files_by_extension[file_extension] = []
                files_by_extension[file_extension].append(file)
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Write files into separate .txt files for each extension
    for ext, files in files_by_extension.items():
        # Remove the leading dot in the extension for the filename
        ext_name = ext.lstrip('.')
        output_file = os.path.join(output_dir, f"{ext_name}_files.txt")
        
        with open(output_file, 'w') as f:
            for file_name in files:
                f.write(file_name + '\n')
    
    print(f"Organized files by extension. Results are stored in the '{output_dir}' directory.")

if __name__ == "__main__":
    organize_files_by_extension()
