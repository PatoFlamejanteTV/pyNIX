def remove_file(file_path):
    import os

    try:
        os.remove(file_path)
        print(f"Removed file: {file_path}")
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except PermissionError:
        print(f"Error: Permission denied: {file_path}")
    except Exception as e:
        print(f"Error: {str(e)}")