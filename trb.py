import json, shlex

def doit(file):
    out = {
        "name": "",
        "id": "",
        "notes": {},
        "variables": {}, 
        "pages": [] 
    } 
    print("Opening", file)
    with open(file+".txt") as f: 
        line = 0 
        for l in f.readlines(): 
            l = l.strip() 
            if line == 0: out['id'] = l.strip()
            elif line == 1: out['name'] = l.strip()
            else:  
                v = { 
                    "name": "", 
                    "chapter": "", 
                    "verse": "", 
                    "text": "" 
                } 
                #parts = l.split(" ") 
                parts = shlex.split(l)
                #print(parts)
                ind = 0
                for item in parts:
                    if ":" in item:
                        break
                    ind += 1

                v['name'] = " ".join( parts[:ind] )
                v['chapter'] = parts[ind].split(":")[0] 
                v['verse'] = parts[ind].split(":")[1] 
                v['text'] = " ".join(parts[ind+1:]) 
                out['pages'].append(v) 

            line += 1    
        with open(file+".json", "w+") as output:
            json.dump(out, output, indent=4)
            print("Done.")

doit("akjv")
doit("asv")
doit("erv")
doit("kjv")
doit("web")