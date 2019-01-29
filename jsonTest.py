import json




# def writeToJSONFile(path, fileName, data):
#     filePathNameWExt = './' + path + '/' + fileName + '.json'
#     with open(filePathNameWExt, 'w') as fp:
#         json.dump(data, fp)


# # Example
# data = {}
# data['key'] = 'value'


# name = ['flor', 'Oscar', 'oscar', 'cesar']
# number = [1, 1, 4, 1]

# keys = ['flor', 'Oscar', 'oscar', 'cesar']
# values = [1, 1, 4, 1]
# dictionary = dict(zip(keys, values))
# print(dictionary)

# writeToJSONFile('./static/js/','test',dictionary)
# './' represents the current directory so the directory save-file.py is in
# 'test' is my file name

dict = {'one': 1, 'two': 2}
repr(dict)
#"{'two': 2, 'one': 1}"

#writing to a file is pretty standard stuff, like any other file write:

f = open( 'static/js/file.js', 'r+' )
text = f.read()
f.write('var numbers = ' + repr(dict))
f.close()