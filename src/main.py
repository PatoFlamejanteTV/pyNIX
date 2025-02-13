def show_help():
    help_text = """
Available commands:
    ls              - List files in current directory
    cp src dst      - Copy file from source to destination
    mv src dst      - Move file from source to destination
    rm file         - Remove specified file
    touch file      - Create new file or update timestamp
    pwd             - Print working directory
    cd [dir]        - Change directory (defaults to home)
    cat file        - Display file contents
    mkdir dir       - Create a new directory
    echo [text]     - Display a line of text
    help            - Show this help message
    exit/quit       - Exit the program
    """
    print(help_text)

def main():
    import os
    import sys
    from commands.ls import list_files
    from commands.cp import copy_file
    from commands.mv import move_file
    from commands.rm import remove_file
    from commands.touch import touch_file
    from commands.pwd import print_working_directory
    from commands.cd import change_directory
    from commands.cat import cat_file
    from commands.mkdir import make_directory
    from commands.echo import echo

    commands = {
        'ls': list_files,
        'cp': copy_file,
        'mv': move_file,
        'rm': remove_file,
        'touch': touch_file,
        'pwd': print_working_directory,
        'cd': change_directory,
        'cat': cat_file,
        'mkdir': make_directory,
        'echo': echo,
        'help': show_help
    }

    print("Unix Clone - Type 'help' for available commands")
    while True:
        try:
            user_input = input("unix-clone> ").strip()
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0]
            args = parts[1:]

            if command in commands:
                try:
                    commands[command](*args)
                except TypeError as e:
                    print(f"Error: Invalid number of arguments for '{command}'")
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print(f"Command not found: {command}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\nTo exit, type 'exit' or 'quit'")
        except EOFError:
            print("\QUitting due EOFError!")
            break

if __name__ == "__main__":
    main()