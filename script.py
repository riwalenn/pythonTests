# my_file = open('test.txt')

# print(my_file.read()) # lis le fichier
# my_file.seek(0)
# print(my_file.readline()) # lis ligne par ligne, il faut autant de readline que de ligne
# print(my_file.readline())
# print(my_file.readlines()) # lis toutes les lignes

# with open('test.txt', mode='r+') as my_file:  # r = read, r+ = read + write, w = write
#     text = my_file.write('hello there !')
#     print(text)
#     print(my_file.readlines())
#
#
# with open('app/sad.txt', mode='w') as my_file:  # r = read, r+ = read + write, w = write
#     text = my_file.write(':(')
#     print(text)

with open('./app/sad.txt', mode='r') as my_file:
    print(my_file.read())
