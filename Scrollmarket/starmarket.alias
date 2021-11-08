!alias starmarket multiline
<drac2>
if "&*&".lower() == "restock":
    gvar=load_json(get_gvar('e79851e7-c1dc-4dc5-b728-b89ee9cb00d0'))
    gvar2=load_json(get_gvar('fd9faa5e-4aa7-4fe6-b22d-6a19601bd903'))
    for key in gvar2.keys():
        if key not in gvar.keys():
            gvar[key] = []
        for i in gvar2[key]:
            gvar[key].append(i)
    level = [randchoice(gvar.get('0')),randchoice(gvar.get('1')),randchoice(gvar.get('2')),randchoice(gvar.get('3')),randchoice(gvar.get('4')),randchoice(gvar.get('5')),randchoice(gvar.get('6')),randchoice(gvar.get('7')),randchoice(gvar.get('8')),randchoice(gvar.get('9'))]
    price = [randint(10,25) + "gp   ",randint(35,60) + "gp   ",randint(350,550) + "gp   ",randint(400,600) + "gp   ",randint(850,1100) + "gp   ",randint(900,1150) + "gp   ",randint(8500,10500) + "gp   ",randint(9250,11000) + "gp   ",randint(9750,11750) + "gp   ",randint(53000,59000) + "gp   "]
    desc = "Restock successful!"
    return f"""!gvar edit 5aff7bfa-a4ad-4e9d-b4e1-d969ea1c729f {{"spells":["{level[0]}","{level[1]}","{level[2]}","{level[3]}","{level[4]}","{level[5]}","{level[6]}","{level[7]}","{level[8]}","{level[9]}"],"prices":["{price[0][0:7]}","{price[1][0:7]}","{price[2][0:7]}","{price[3][0:7]}","{price[4][0:7]}","{price[5][0:7]}","{price[6][0:7]}","{price[7][0:7]}","{price[8][0:7]}","{price[9][0:7]}"]}}"""
elif "&*&".split(' ')[0] == "remove":
    userinput = "&*&"
    gvar=load_json(get_gvar('5aff7bfa-a4ad-4e9d-b4e1-d969ea1c729f'))
    userinput = userinput.replace('remove ','')
    if userinput in gvar.spells:
        removed_item_location = gvar.spells.index(userinput)
    else:
        err("Item not found")
    gvar.spells[removed_item_location] = "*SOLD*"
    gvar.prices[removed_item_location] = "N/A    "
    gvar=dump_json(gvar)
    desc = f'{userinput} has been removed'
    return f"!gvar edit 5aff7bfa-a4ad-4e9d-b4e1-d969ea1c729f {gvar}"
else:
    gvar=load_json(get_gvar('5aff7bfa-a4ad-4e9d-b4e1-d969ea1c729f'))
    desc = f"""Available Spell Scrolls:\n`{gvar.prices[0]}` - **Cantrip:** *{gvar.spells[0]}*\n`{gvar.prices[1]}` - **Level 1:** *{gvar.spells[1]}*\n`{gvar.prices[2]}` - **Level 2:** *{gvar.spells[2]}*\n`{gvar.prices[3]}` - **Level 3:** *{gvar.spells[3]}*\n`{gvar.prices[4]}` - **Level 4:** *{gvar.spells[4]}*\n`{gvar.prices[5]}` - **Level 5:** *{gvar.spells[5]}*\n`{gvar.prices[6]}` - **Level 6:** *{gvar.spells[6]}*\n`{gvar.prices[7]}` - **Level 7:** *{gvar.spells[7]}*\n`{gvar.prices[8]}` - **Level 8:** *{gvar.spells[8]}*\n`{gvar.prices[9]}` - **Level 9:** *{gvar.spells[9]}*"""
</drac2>
!embed
-title "Stargazers Market"
-desc "{{desc}}"
-color "411c47"
