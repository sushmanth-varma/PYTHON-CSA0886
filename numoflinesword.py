paragraph ="""This is a sample paragraph.
It consists of multiple lines.
Each line contains several words.
The program will count the number of words in each line.
It will also count the total number of lines in the paragraph."""

lines=paragraph.split("\n")
num_lines=len(lines)
total_words=0
for line in lines:
    words=line.split()
    num_words=len(words)
    total_words=total_words+num_words
    print("number of words in line:",num_words)
print("numbers of lines:",num_lines)
print("number of words:",total_words)
