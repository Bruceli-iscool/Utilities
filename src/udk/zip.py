import shutil

def zip(file, dest):
    try:
        shutil.make_archive(file, 'zip', dest)
    except FileNotFoundError as e:
        print(e)