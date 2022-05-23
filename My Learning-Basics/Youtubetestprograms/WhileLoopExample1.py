paragraph = []
print(type(paragraph))
print ("Enter a Paragraph: ")

while True :
    line = input()
    if line:
        paragraph.append(line)
    else:
        break

print(paragraph)
output = '\n'.join(paragraph)
print(output)