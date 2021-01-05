'''
Jaimeen Sharma
CS 100 2020F 033
HW 9, October 2, 2020.
'''

# Problem 1

def file_copy(in_file, out_file):
    in_file = open('created_equal.txt','r')
    out_file = open('copy.txt','w')
    for line in in_file:
        out_file.write(line)
    out_file.close()
    in_file.close()

file_copy('created_equal.txt','copy.txt')

# Problem 2

def file_stats(in_file):
    file = open('created_equal.txt','r')
    lines = file.readlines()
    file.close()

    file = open('created_equal.txt','r')
    words = file.read()
    file.close()
    wordsare = words.split()

    file = open('created_equal.txt','r')
    chars = file.read()
    file.close()

    return print(" lines",len(lines),'\n','Words' ,len(wordsare),'\n','characters',len(chars))

file_stats('created_equal.txt')

# Problem 3

def repeat_Words(in_file, out_file):
    import string
    new_content=""
    
    file = open(in_file,'r')
    content = file.read()
       
    for words in content:
        new_content += words.strip('!')
    new_content = new_content.lower().split()

    repeated_list = []

    for word in new_content:
        if new_content.count(word)>1:
            repeated_list.append(word)

    new_repeat_list = []
    
    for item in repeated_list:
       while item not in new_repeat_list:
          new_repeat_list.append(item)

    outfile = open(out_file,'w')
    for repeat in new_repeat_list:
        outfile.write(repeat + '\n')

    outfile.close()
    file.close()

repeat_Words('catInTheHat.txt','catRepWords.txt')



  
