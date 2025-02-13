def change_directory(path=None):
    import os
    
    if path is None:
        # change to home dir if no path specified
        path = os.path.expanduser("~")
    
    try:
        os.chdir(path)
        print(f"Changed directory to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Error: Directory not found: {path}")
    except PermissionError:
        print(f"Error: Permission denied: {path}")