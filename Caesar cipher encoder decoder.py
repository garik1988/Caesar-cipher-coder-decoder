def encoder(text,shift_ammount):
    
    shift_ammount=int(shift_ammount)
    
    encoded="" 

    charlist=list(map(chr, range(0, 1114111))) #generates a list with every printable unicode characters

    for char in text: #for loop that shifts the text characters by finding index of them in characters list and replace them with shifted character in list
       
        if charlist.index(char)+shift_ammount<len(charlist):
            
            encoded+=charlist[charlist.index(char)+shift_ammount]
        
        elif charlist.index(char)+shift_ammount>=len(charlist):
            
            encoded+=charlist[charlist.index(char)+shift_ammount-len(charlist)]
       
        else:
           
            encoded+=charlist[charlist.index(char)+shift_ammount]

    return encoded #returns string with encoded text

def decoder (text,shift_ammount):
    
    shift_ammount=int(shift_ammount)
   
    
    decoded=""
    
    charlist=list(map(chr, range(0, 1114111)))  #generates a list with every printable unicode characters
   
    for char in text: #for loop that shifts the text characters by finding index of them in characters list and replace them with shifted character in list

        if charlist.index(char)-shift_ammount>=0:

            decoded+=charlist[charlist.index(char)-shift_ammount]
            
        elif charlist.index(char)-shift_ammount<0:
            
            decoded+=charlist[charlist.index(char)-shift_ammount+len(charlist)]
       
    return decoded


def main (): #main menu
    print ("""                                                   _         _                   
                                                  (_)       | |                  
  ____   ____   ____   ___   ____   ____     ____  _  ____  | | _    ____   ____ 
 / ___) / _  | / _  ) /___) / _  | / ___)   / ___)| ||  _ \ | || \  / _  ) / ___)
( (___ ( ( | |( (/ / |___ |( ( | || |      ( (___ | || | | || | | |( (/ / | |    
 \____) \_||_| \____)(___/  \_||_||_|       \____)|_|| ||_/ |_| |_| \____)|_|    
                                                     |_|                         
  """)
    while True:
        
        task=input("Do you wish to:\n\t1)Encode\n\t2)Decode\n Enter task: ")
        
        if task == '1' or  task == '2' :
            break
            
        else:
            print("there is no such option please choose a correct option")
            
    while True:
       
        shift_ammount=input("type the shift_ammount number: ")
        
        if shift_ammount.isnumeric():
         
            break
        
        else:
        
            print ("wrong entry")

    
    if int(task) == 1:
       
        text=input("enter the text you want to encode: ")
        
        print(f"Your Encoded version of {text} is: {encoder(text,shift_ammount)} ")
       
    
    elif int(task) == 2:
        
        text=input("enter the text you want to decode")
        
        print(f"Your decoded version of {text} is:  {decoder(text,shift_ammount)} ")
    
    
    

main()