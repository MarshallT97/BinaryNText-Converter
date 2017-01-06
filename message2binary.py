import os

#message2binary function convert a message into binary
def message2binary(message):
    new_message = ''
    if('\n' in message):
        message = message.replace('\n','')
    for x in message:
        if(x != ' '):
            new_message += '{0:b}'.format(ord(x)) + ' '
        else:
            new_message += x
    new_message = new_message[:-1]
    return(new_message)

#binary2message function convert binary into a message
def binary2message(binary):
    binary_list = binary.split(' ')
    if('\n' in binary_list):
        binary_list.remove(binary_list[-1])
    for x in range(len(binary_list)):
        if(binary_list[x] != ''):
            binary_list[x] = chr(int(binary_list[x],2))
        else:
            binary_list[x] = ' '
    new_message = ''.join(binary_list)
    return(''.join(binary_list))

#m2bFile function convert a text file with text into binary
def m2bFile(textfilename,binaryfilename='TextConvertFile.txt'):
    textFile = open(textfilename,'r')
    if(os.path.exists(binaryfilename)):
        os.remove(binaryfilename)
    binaryFile = open(binaryfilename,'a')
    for line in textFile:
        binaryFile.write(message2binary(line) + '\n')
    textFile.close()
    binaryFile.close()

#b2mFile function convert a text file with binary into text
def b2mFile(binaryfileName,textfilename='BinaryConvertFile.txt'):
    binaryFile = open(binaryfileName,'r')
    if(os.path.exists(textfilename)):
        os.remove(textfilename)
    binary_text_File = open(textfilename,'a')
    for line in binaryFile:
        binary_text_File.write(binary2message(line) + '\n')
    binaryFile.close()
    binary_text_File.close()
