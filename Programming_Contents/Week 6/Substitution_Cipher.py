import string

relations = {}
data = ""

for i in range(len(string.ascii_letters)):
    relations[string.ascii_letters[i]]=string.ascii_letters[i-1]

output = open("message_encrypted.txt","w")
with open("message.txt","r") as message:
    while True:
        char = message.read(1)
        if not char:
            print ("\n--- End of file. ---")
            break
        if char in relations:
            data = relations[char]
        else:
            data = char
        output.write(data)
        print(data,end="")
output.close()