import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
      
    for filename in os.listdir("1"): 
        #print(filename)
        tmp = filename.split(' - Copy')
        if (len(tmp)>1):
                tmp1=tmp[0]+tmp[1]
        else:
                tmp1=filename
        print(tmp1)
        # rename() function will 
        # rename all the files
        src = '1/'+filename 
        dst = '1/'+tmp1
        os.rename(src, dst) 
        i += 1
        print(i)
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 