from pathlib import Path
import os
import sys
path = Path()

line_counter = 0
with open("test1", "r") as file1:
    for line in file1:
        line_counter += 1


input_filename = input("Pleae enter a file name\n")
paths = " ".join([str(p) for p in path.rglob("*") if str(p) in input_filename])
if input_filename != paths:
    new_file_name = input(
        "The file doesn't exist. Please enter a file name to write a new file\n")
    output_file = open(new_file_name, "w")
else:
    print("Please select one of the options:\n a: Read file\n b: Delete and start over\n c: Append file\n d: Replace line\n")
    while True:
        choices = input("")
        if choices.lower() == "a":
            with open(input_filename, "r") as file1:
                print(file1.read())
            break
        if choices.lower() == "b":
            os.remove(input_filename)
            file_name = input("Please enter a new file name\n")
            new_file = open(file_name, "w")
            break
        if choices.lower() == "c":
            with open(input_filename, "a") as file1:
                append_content = input(
                    "Please enter a new content to the file\n")
                file1.write(f"{append_content} \n")
            break
        if choices.lower() == "d":
            new_content = ""
            print("Please enter the line number you want to update (starting from 0)")
            while True:
                replacement_line = int(input(""))
                if replacement_line > line_counter:
                    print(
                        "Sorry, line number is out of range. Please enter a smaller value")
                else:
                    break
            replacement_string = input(
                "Please enter the text that should replace the line\n")
            with open("test1", "r") as file1:
                for line in enumerate(file1):
                    line_stripped = line[1].strip()
                    if line[0] == replacement_line:
                        new_content += line_stripped.replace(
                            line_stripped, replacement_string + "\n")
                    else:
                        new_content += line_stripped + "\n"

            with open("test1", "w") as file1:
                file1.write(new_content)
            break
        else:
            print("Please enter a valid option: a, b, c, d")
