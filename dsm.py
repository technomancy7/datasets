import sys, os, argparse

#WIP

class Datasets:
    def __init__(self, base_dir):
        self.directory = base_dir
        if not self.directory.endswith("/"): self.directory = self.directory+"/"
        self.history = []

    def appendln(self, file, newln):
        text = ""
        with open(self.directory+file) as f:
            text = f.read()

        text = text.strip()+"\n"+newln
        with open(self.directory+file, 'w') as f:
            f.write(text)

    def pull(self):
        os.system(f"git clone https://gitlab.com/codedmind/datasets.git {self.directory}")

    def push(self):
        os.chdir(f"{self.directory}")
        os.system("git add .")
        os.system(f"git commit -m \"{' '.join(self.history)}\"")
        os.system("git push -u origin master")
    
    def purge(self):
        os.system(f"rm -r {self.directory}")

if __name__ == "__main__":
    args = sys.argv[2:]
    cmd = sys.argv[1]
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['push', 'pull', 'get', 'purge', 'append'])
    parser.add_argument("--index", help="index for inserting", type=int)
    parser.add_argument("--directory", help="directory to use", type=str, default=os.getcwd())
    parser.add_argument("--text", help="text to use for operation", type=str, default=os.getcwd())
    parser.add_argument("--file", help="file to apply operation on", type=str, default=os.getcwd())
    args = parser.parse_args()
    ds = Datasets(args.directory)

    match args.command:
        case "get" | "pull":
            ds.pull()
        case "purge":
            ds.purge()
        case "append":
            text = input("> ")
            ds.appendln("youtube.txt", text)