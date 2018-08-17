
file_path  = open('D:/myPython.txt','w+')
input_txt = input('Enter the input for file : ')
file_path.write(input_txt)

num = file_path.__sizeof__()
file_path.seek(0,0)
read_file = file_path.read(num)
print('size of', num)
print('contain', read_file)
