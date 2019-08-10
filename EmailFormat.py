import easygui

enteredText = easygui.enterbox("Please enter email body: ")
splitText = enteredText.split('to Stallion\n')[1]
inputText = splitText.split('\n')
outputText = []
for line in inputText:
    #print(line)
    start = line.find(' ')
    end = line.find('=')
    #line = line[:start] + '\t' + line[end + 2:]
    line = line[end + 2:]
    line = line.upper()
    print(line)
    outputText.append(line + '\n')

out = ''
del outputText[-1]
for line in outputText:
    out = out + line
easygui.msgbox(out)
