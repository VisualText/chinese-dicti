import json, os
file = '/Users/wang/Downloads/word.json'
y = []
filename = 0

with open(file) as f:
    y = json.load(f)
    # for line in f.readlines():
    #     y += json.loads(line)
    
for word in y:
    filename+=1
    newFile = open(os.path.dirname(os.path.realpath(__file__)) + "/output2/" + str(filename) + ".txt", "a+")
    newFile.write("word: " + word['word'] + "\n")
    newFile.write("oldword: " + word['oldword'] + "\n")
    newFile.write("strokes: " + word['strokes'] + "\n")
    newFile.write("pinyin: "+word["pinyin"] + "\n")
    newFile.write("radicals: "+word['radicals'] + "\n")
    newFile.write("explanation: " + word['explanation'] + "\n")
    newFile.write("more:" + word['more'])
    newFile.close()