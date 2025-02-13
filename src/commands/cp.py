def copy_file(source, destination):
    import os
    import shutil

    if not os.path.isfile(source):
        raise FileNotFoundError(f"The source file '{source}' does not exist.")
    
    try:
        shutil.copy2(source, destination)
    except Exception as e:
        raise Exception(f"Error copying file: {e}")