def list_files():
    import os

    # get cur dir
    current_directory = os.getcwd()

    # list system
    files = os.listdir(current_directory)

    for file in files:
        print(file)