import sys
class ChangeDirectory():

    def change_directory(self, current, changed):
        if not changed:
            return current
        if changed[0] == "/":
            current = ""
       
        checkChanged=changed.split("/")
        if(len(checkChanged)==1 and (checkChanged[0]!="." and checkChanged[0]!=".." ) 
            and not checkChanged[0][0].isalnum() ):
            return "No Such Directory Exist."

        newDirectory = []
        
        for word in (current + "/" + changed).split("/"):
            if(word==""):
                continue
            if(word!="." and word!=".." 
            and not word[0].isalnum() ):
                return "No Such Directory Exist."
            if word == "..":
                if newDirectory:
                    newDirectory.pop()
            elif word and word != ".":
                newDirectory.append(word)

        return "/" + "/".join(newDirectory)
  

if __name__ =="__main__":
    current6 = sys.argv[1]
    change6 = sys.argv[2]
    cd = ChangeDirectory()
    output = cd.change_directory(current6, change6)
    print(output)