import os

class FileOperationsUtil:

    def __init__(self):
        pass

    @staticmethod
    def change_directory(dir, curr_dir, repl_dir):
        dir = dir.replace(curr_dir, repl_dir)
        os.chdir(dir)

    @staticmethod
    def read_file(file_path):
        with open(file_path) as f:
            input_lines = f.readlines()

        # Remove trailing / leading special characters from input_lines list
        input_lines = list(map(str.strip, input_lines))

        return input_lines

    @staticmethod
    def write_file_multiple_dfs(file_path, df_list):
        with open(file_path, 'w') as f:
            for df in df_list:
                f.write(df.to_string())
                f.write('\n\n')