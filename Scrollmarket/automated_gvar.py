text = """"""
list = text.split('\n')
finaltext = []
for x in list:
    finaltext.append(f"""{{"level":"9","name":\"""" + x + """\"},""")
final = ''.join(str('\n'+i) for i in finaltext)
print (f"""{final}""")
