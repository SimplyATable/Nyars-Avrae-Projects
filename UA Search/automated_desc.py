text = input("Your text here: ")
list = text.split('|')
finaltext = []
for x in list:
    finaltext.append(f"""\\n\\" -f \\"{x}""")
print(' '.join(str(i) for i in finaltext).replace('\n', ''))

# Must put | between sections of text. Must put | and \n in as needed after running
# CHECK RESULT AFTER USING
