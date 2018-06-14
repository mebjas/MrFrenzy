import sys
import json
import re

class Variables(Exception):
    def __init__(self, filename=None, verbose=False):
        if not filename:
            filename = "./schema.variables.json"

        self.classes = {}
        self.patterns = []
        self.verbose = verbose

        data = None
        with open(filename, "r") as ifp:
            data = json.load(ifp)

        if "patterns" not in data or "classes" not in data:
            raise Exception("Invalid schema: patterns or classes are a must")

        ## load all classes
        if verbose:
            print ("Loading Classes")

        for cls in data["classes"]:
            self.classes[cls["name"]] = cls

            if verbose:
                print ("\t Loaded {%s}" % cls["name"])
        
        ## validate the classes
        for cls, val in self.classes.items():
            if self.classes[cls]["parent"]:
                parent = self.classes[cls]["parent"]
                if not parent in self.classes:
                    raise Exception("%s has parent %s which is not found" % (cls, parent))

        ## load all the patterns
        if verbose:
            print ("Loading Patterns")

        for pattern in data["patterns"]:
            cls = pattern["class"]
            if cls not in self.classes:
                raise Exception("%s has class %s which is not found" % (pattern["r"], cls))

            ## indicates if full match is needed
            full = False
            if "full" in pattern and pattern["full"]:
                full = True

            if verbose:
                print ("\t Loading {%s} {Class: %s}" % (pattern["r"], cls))

            self.patterns.append({
                "r": re.compile(pattern["r"]),
                "class": cls,
                "f": full
            })

    ## TODO: add verbosity
    def Transform(self, text):
        if not text or text.strip() == "":
            raise Exception("ArgumentException text")

        tokens = text.split(" ")

        # for generating transformed data
        _tokens = []
        
        for token in tokens:
            for pattern in self.patterns:
                r = pattern["r"]
                matches = re.findall(r, token)
                if matches and len(matches) > 0:
                    if pattern["f"]:
                        if matches[0] == token:
                            token = token.replace(matches[0], "@" +pattern["class"])
                            break
                    else:
                        for match in matches:
                            token = token.replace(match, "@" +pattern["class"])

                        break

            _tokens.append(token)
        
        return " ".join(_tokens)

    def TransformAll(self, texts):
        return [self.Transform(text) for text in texts]