import jwt,sys,os


## Get the full file path
## Reading the file as read only
filepath=os.path.join(sys.path[0], 'jwt-2.txt')
with open(filepath,'r') as f:
    
    ## Read the file content with splitlines, to remove newlines, otherwise will broke the decode process below
    fileC=f.read().splitlines()

    ## Create for loop to decode jwt while reading the file content line by line
    for line in fileC:
        
        ## Decode jwt token, without validation
        decoded = jwt.decode(line, options={'verify_signature': False})

        ## Check if the 'admin' value inside the dictionary (which was formed from the decode process)
        if 'admin' in decoded.values():

            ## Print out the jwt and decoded format
            print(line)
            print(decoded)
            break

f.close()
