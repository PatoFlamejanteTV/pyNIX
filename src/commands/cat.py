def cat_file(*file_paths):
    if not file_paths:
        print("Error: No file specified")
        return
        
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as f:
                print(f.read(), end='')
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}")
        except PermissionError:
            print(f"Error: Permission denied: {file_path}")
        except Exception as e:
            print(f"Error reading {file_path}: {str(e)}")