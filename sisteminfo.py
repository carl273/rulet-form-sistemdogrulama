import subprocess

def write_to_file(content, filename='sistem_dogruklama.txt'):
    try:
        with open(filename, 'a') as file:
            file.write(content + '\n')
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")

def get_output(code):
    try:
        process = subprocess.Popen(code, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output, error = process.communicate()

        decoded_output = output.decode('utf-8', errors='replace')
        decoded_error = error.decode('utf-8', errors='replace')

        write_to_file(f"Command: {code}\nOutput: {decoded_output}\nError: {decoded_error}")
    except Exception as e:
        print(f"An error occurred while executing the command: {e}")

# Example usage:
get_output('ipconfig /all')
get_output('systeminfo')
