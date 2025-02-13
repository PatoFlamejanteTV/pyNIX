def move_file(source, destination):
    import os
    import shutil

    if not os.path.exists(source):
        raise FileNotFoundError(f"The source file '{source}' does not exist.")
    
    if os.path.exists(destination):
        raise FileExistsError(f"The destination '{destination}' already exists.")

    shutil.move(source, destination)