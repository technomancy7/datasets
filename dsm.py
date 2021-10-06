import sys, os, argparse

#WIP

class Datasets:
    def __init__(self, base_dir):
        self.directory = base_dir
        self.history = []

    def pull(self):
        os.system(f"git clone https://gitlab.com/codedmind/datasets.git {self.directory}/datasets")

    def push(self):
        os.chdir(f"{self.directory}/datasets")
        os.system("git add .")
        os.system(f"git commit -m \"{' '.join(self.history)}\"")
        os.system("git push -u origin master")
    
    def purge(self):
        os.system(f"rm -r {self.directory}/datasets")

if __name__ == "__main__":
    args = sys.argv[2:]
    cmd = sys.argv[1]
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['push', 'pull', 'get', 'purge'])
    parser.add_argument("--index", help="index for inserting", type=int)
    args = parser.parse_args()
    #print(args.command)
    #print(args.index, type(args.index))
    ds = Datasets(os.getcwd())
    #print(ds.directory)
    match args.command:
        #case "pull":
        case "get" | "pull":
            ds.pull()
        case "purge":
            ds.purge()