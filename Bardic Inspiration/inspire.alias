!alias inspire embed

<drac2>
cc = "Bardic Inspiration"
if not get('level'):
  T = f"{ctx.author} uses {cc}!"
  D = "You can use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a **d6**. You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain any expended uses when you finish a long rest."
  F = f"Your Bardic Inspiration die changes when you reach certain levels in this class. The die becomes a **d8** at 5th level, a **d10** at 10th level, and a **d12** at 15th level."
  return f"{T} {D} {F}"
desc = "You can use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a "
rest = "You can’t use this feature again until you finish a long rest."
noCC = "Wait a minute, you're no bard!"
ch=character()
lvl = ch.levels.get("Bard",0)
if lvl:
    ch.create_cc_nx(cc, 0, charismaMod, "short", None, None, None, cc, desc+" "+rest)
if lvl < 5:
    die = 6
elif lvl < 10:
    die = 8
elif lvl < 15:
    die = 10
else:
    die = 12
desc = f"You can use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a **d{die}**"
rest = "You can’t use this feature again until you finish a long rest."
noCC = "Wait a minute, you're no bard!"
succ = "tries to use"
if ch.cc_exists(cc) and ch.get_cc(cc):
    succ = "uses"
    D = desc
    ch.mod_cc(cc, -1)
elif ch.cc_exists(cc):
    D = rest
else:
    D = noCC
T = f"{name} {succ} {cc}!"
F = f"{cc}|{ch.cc_str(cc) if ch.cc_exists(cc) else '*None*'}"
</drac2>

-title "{{T}}"
-desc "{{D}}"
-f "{{F}}"
-color <color>
-thumb <image>
