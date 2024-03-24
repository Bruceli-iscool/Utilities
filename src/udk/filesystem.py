import shutil
import os
def mov(file, dest, error="An Error occured:"):
        # Move a file
        try:
            shutil.move(file, dest)
        except FileNotFoundError as e:
            print(error, e)
def rem(file, error="An Error occured:"):
        # Delete a file
        try:
            os.remove(file)
        except FileNotFoundError as e:
            print(error, e)
def see(file, error="An Error occured:"):
        # view a file
        try:
            with open(file) as file:
                for line in file:
                    print(line)
        except Exception as e:
            print(error, e)
def create(file, error="An Error occured:"):
        # create a file
        try:
            with open(file, "x") as file:
                file.close()
        except FileExistsError:
            print(error, FileExistsError)