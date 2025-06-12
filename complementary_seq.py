sequence = "GGGCTCTTTATATATTCGXCGCGTT"

complement = ""
for i in range(0, len(sequence)):
    
    if sequence[i] == "A":
        complement += "T"
        
    elif sequence[i] == "T":
        complement += "A"

    elif sequence[i] == "C":
        complement += "G"

    elif sequence[i] == "G":
        complement += "C"

    else:
        print ("Not a valid nucleotide")
        complement += "_"

print (complement)
