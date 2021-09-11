text = """"""
list = text.split('\n')
finaltext = []
for x in list:
    finaltext.append(f"""{{"level":"0","name":\"""" + x + """\"},""")
final = ''.join(str(i) for i in finaltext)
print (f"""{final}""")
