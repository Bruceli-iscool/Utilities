
def editor(file):
        # Simple Text editor
        with open(file, "a") as files:
            for line in files:
                print(line)
            while True:
                line = input()
                if line.startswith(":q"):
                    break
                else:
                    file.write(line+'\n')
editor("test.py")