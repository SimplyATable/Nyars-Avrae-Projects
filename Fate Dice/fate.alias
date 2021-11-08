!alias fate embed
<drac2>
if not "&*&":
        num = '4'
else:
        num = '&*&'
display = ['']
if int(num) > 1000:
        T = "**Invalid Equation**"
        D = "Maximum number of rollable fate dice is 1000"
        F = ""
        return f"{T} {D} {F}"
roll1 = [str(randint(-1,2)) for x in range(int(num))]
display.append("[" + "] [".join([str(x) for x in roll1]) + "]")
T = "Fate Roll!"
D = ''.join(display).replace('-1','-').replace('0','  ').replace('1','+')
To = sum(int(i) for i in roll1)
F=f"Total = {To} (dice rolled: {num})"
if len(D) > 300:
        B = roll1.count("0")
        P = roll1.count("1")
        M = roll1.count("-1")
        D = f"**[  ]:** {B}"
        return f""" -f "**[+]:** {P}" -f "**[-]:** {M}" """
</drac2>
-title "{{T}}"
-desc "{{D}}"
-footer "{{F}}"
