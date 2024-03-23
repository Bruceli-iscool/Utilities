class tools:
    def editor(file):
        # Simple Text editor
        with open(file, "a") as file:
            while True:
                line = input()
                if line.startswith(":q"):
                    break
                else:
                    file.write(line+'\n')
