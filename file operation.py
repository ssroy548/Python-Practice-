#read
file = open("file.txt",'r')
# # rdline = file.readline()
#
# count = 0
# for l in file:
#     count += 1
# print(count)
# print(rdline)
# rdlines = file.readlines()
# print(rdlines)
# rdfile = file.read()
# print(rdfile)

# file = open("file2.txt","w")
# for number in range(11):
#     file.write(str(number)+'\n')
    # file.write("\n")


# num_words = 0
# fileref = "file.txt"
#
# with open(fileref, 'r') as file:
#     for line in file:
#         num_words += len(line.split())
#
# print("number of words : ", num_words)
count = 0
for line in file:
    count+=1
print(count)


