import os
# print(os.getcwd())

# fout = open('output.txt', 'a')
# line1 = "How many roads must a man walk down\n"
# fout.write(line1)
# line2 = "Before you call him a man?\n"
# fout.write(line2)
# fout.close()

# print(os.path.abspath(''))


# def walk(dirname):
#     """Prints the names of all files in 
#     dirname and its subdirectories.

#     dirname: string name of directory
#     """
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname, name)

#         if os.path.isfile(path):
#             print(path)
#         else:
#             walk(path)

# a = [1, 2, 3]
# try:
#     fin = open('notexisting.txt')
# except:
#     print('Something is wrong.')

# folder = os.getcwd()

# walk(folder)


import pickle

# t1 = [1, 2, 3]

# f = open('save.p', 'wb')
# s = pickle.dump(t1, f)
# f.close()

t2 = pickle.load(open('save.p', 'rb'))
print(t2)

