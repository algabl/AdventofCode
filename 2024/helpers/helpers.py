def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
    
def get_current_day(file_path):
    return file_path.split('/')[-1].split(".")[0].replace("day", "")

def read_input(day, split_lines=True):
  path = f"./2024/inputs/input{day}.txt"
  input = read_file(path)
  return input.splitlines() if split_lines else input
 