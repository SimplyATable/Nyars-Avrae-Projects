!alias markettest multiline
<drac2>
if "&*&".lower() == "restock":
    gvar=load_json(get_gvar('e79851e7-c1dc-4dc5-b728-b89ee9cb00d0'))
    level_0 = randchoice(gvar.get('0'))
    level_1 = randchoice(gvar.get('1'))
    level_2 = randchoice(gvar.get('2'))
    level_3 = randchoice(gvar.get('3'))
    level_4 = randchoice(gvar.get('4'))
    level_5 = randchoice(gvar.get('5'))
    level_6 = randchoice(gvar.get('6'))
    level_7 = randchoice(gvar.get('7'))
    level_8 = randchoice(gvar.get('8'))
    level_9 = randchoice(gvar.get('9'))
    price_0 = str(randint(10,25)) + "gp   "
    price_1 = randint(35,60) + "gp   "
    price_2 = randint(350,550) + "gp   "
    price_3 = randint(400,600) + "gp   "
    price_4 = randint(850,1100) + "gp   "
    price_5 = randint(900,1150) + "gp   "
    price_6 = randint(8500,10500) + "gp   "
    price_7 = randint(9250,11000) + "gp   "
    price_8 = randint(9750,11750) + "gp   "
    price_9 = randint(53000,59000) + "gp   "
    desc = "Restock successful!"
    return f"""!gvar edit 5aff7bfa-a4ad-4e9d-b4e1-d969ea1c729f {{"spells":["{level_0}","{level_1}","{level_2}","{level_3}","{level_4}","{level_5}","{level_6}","{level_7}","{level_8}","{level_9}"],"prices":["{price_0[0:7]}","{price_1[0:7]}","{price_2[0:7]}","{price_3[0:7]}","{price_4[0:7]}","{price_5[0:7]}","{price_6[0:7]}","{price_7[0:7]}","{price_8[0:7]}","{price_9[0:7]}"]}}"""
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
