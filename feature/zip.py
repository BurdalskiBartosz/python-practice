contents = ['text1', 'text2', 'text3']

filenames = ['text.txt', 'text2.txt', 'text3.txt']

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)
    file.close()