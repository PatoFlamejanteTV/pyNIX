def make_directory(directory_path):
    import os
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Created directory: {directory_path}")
    except PermissionError:
        print(f"Error: Permission denied: {directory_path}")
    except Exception as e:
        print(f"Error: {str(e)}")