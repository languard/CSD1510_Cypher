
#globals
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#create and return an array of letters that is shifted by the given amount
def CreateCipher(shiftAmount):
    #makes no sense if shiftAmount is less than 1
    if shiftAmount < 1:
        print("Error! Shift amount must be at least 1!")
        return
    #blank array to hold the shifted letters
    result = []

    for i in range(26):
        #ti = target index
        #add the shift amount and then make sure it doesn't exceed 25. If it does, wrap it back around
        #to the beginning.
        ti = i + shiftAmount
        if ti > 25: ti -= 26
        result.append(alphabet[ti])

    #append punctuation to both. A bit of a brute force solution, but it works.
    alphabet.append(".")
    alphabet.append(",")
    alphabet.append("!")
    alphabet.append("?")
    alphabet.append("\"")
    alphabet.append(";")
    alphabet.append(":")
    alphabet.append("'")

    result.append(".")
    result.append(",")
    result.append("!")
    result.append("?")
    result.append("\"")
    result.append(";")
    result.append(":")
    result.append("'")

    return result

#using the provided key, encrypt the message
def EncryptMessage(sourceMessage, key):
    result = ""
    #converting everything to upper case to simplify
    sourceMessage = sourceMessage.upper()
    #look at every letter in the source string
    for chr in sourceMessage:
        #check for space
        if chr == " ":
            result += " "
        else:    
            #there are other ways to find the index of the letter, but
            #since we have the array might as well use it
            index = alphabet.index(chr)    
            #pull the shifted letter from the key
            result += key[index]

    return result
        
def DecryptMessage(sourceMessage, key):
    result = ""
    sourceMessage = sourceMessage.upper()
    for chr in sourceMessage:
        if chr == " ":
            result += " "
        else:
            #same logic as encrypting, just reversed
            index = key.index(chr)
            result += alphabet[index]
    return result

shift = 1
###Error corrected version
# try:
#     shift = int(input("How many shifts for the key?"))
# except:
#     print("Invalid input, setting shift to 1")
#     shift = 1
# finally:
#     pass

###Simple version
shift = int(input("How many shifts for the key?"))

ceaser = CreateCipher(shift)

answer = input("Enter E to encrypt or D to decrypt: ")

if answer.upper() == "E":
    theMessage = EncryptMessage(input("What to encrypt? "), ceaser)
    print(theMessage)
else:
    theMessage = DecryptMessage(input("What to decrypt? "), ceaser)
    print(theMessage)
