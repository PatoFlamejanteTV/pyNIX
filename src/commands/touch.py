def touch_file(file_path):
    import os
    try:
        with open(file_path, 'a'):
            os.utime(file_path, None)
        print(f"Created/updated file: {file_path}")
    except PermissionError:
        print(f"Error: Permission denied: {file_path}")
    except Exception as e:
        print(f"Error: {str(e)}")