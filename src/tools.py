
def editor(file):
        # Simple Text editor
        with open(file, "r+") as files:
                for line in files:
                    print(line)
                while True:
                    line = input()
                    if line.startswith(":q"):
                        break
                    else:
                        files.write(line+'\n')
