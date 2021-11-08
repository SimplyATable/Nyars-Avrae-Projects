!alias xpcalc embed
<drac2>
x=load_json(get_gvar('e7d3aff0-5c1a-4f49-9595-1a3a2afc07c8'))
input = "&*&".split()
if not len(input) == 16:
  err("Count does not equal 16, double check your input")
f1name = input[0]
input.remove(f1name)
f2name = input[4]
input.remove(f2name)
input = [int(i) for i in input]
f1level = input[0]
f2level = input[4]
winner = input[13]
if f1level <= 4:
  f1rw = x.rw1
  f1rl = x.rl1
elif f1level >= 5 and f1level <= 8:
  f1rw = x.rw2
  f1rl = x.rl2
elif f1level >= 9 and f1level <= 12:
  f1rw = x.rw3
  f1rl = x.rl3
elif f1level >= 13 and f1level <= 16:
  f1rw = x.rw4
  f1rl = x.rl4
else:
  f1rw = x.rw5
  f1rl = x.rl5
if f2level <= 4:
  f2rw = x.rw1
  f2rl = x.rl1
elif f2level >= 5 and f2level <= 8:
  f2rw = x.rw2
  f2rl = x.rl2
elif f2level >= 9 and f2level <= 12:
  f2rw = x.rw3
  f2rl = x.rl3
elif f2level >= 13 and f2level <= 16:
  f2rw = x.rw4
  f2rl = x.rl4
else:
  f2rw = x.rw5
  f2rl = x.rl5
if winner == 1:
  f1rewards = (f1rw * f2level)+(x.winrebirth*input[7])
  f2rewards = (f2rl * f1level)+(x.loserebirth*input[3])
elif winner == 2:
  f1rewards = (f1rl * f2level)+(x.loserebirth*input[7])
  f2rewards = (f2rw * f1level)+(x.winrebirth*input[3])
else:
  err("Winner is not 1 or 2, double check your input")
avgfighterlevel = (f1level+f2level)/2
if avgfighterlevel <= 4:
  tbase = x.basetrap1
  txpper = x.xppertrap1
  tmaxxp = x.maxtrapxp1
  refxp = (avgfighterlevel*x.baseref1)
elif avgfighterlevel >= 5 and avgfighterlevel <= 8:
  tbase = x.basetrap2
  txpper = x.xppertrap2
  tmaxxp = x.maxtrapxp2
  refxp = (avgfighterlevel*x.baseref2)
elif avgfighterlevel >= 9 and avgfighterlevel <= 12:
  tbase = x.basetrap3
  txpper = x.xppertrap3
  tmaxxp = x.maxtrapxp3
  refxp = (avgfighterlevel*x.baseref3)
elif avgfighterlevel >= 13 and avgfighterlevel <= 16:
  tbase = x.basetrap4
  txpper = x.xppertrap4
  tmaxxp = x.maxtrapxp4
  refxp = (avgfighterlevel*x.baseref4)
else:
  tbase = x.basetrap5
  txpper = x.xppertrap5
  tmaxxp = x.maxtrapxp5
  refxp = (avgfighterlevel*x.baseref5)
if input[2]:
  f1rewards += x.daily
if input[6]:
  f2rewards += x.daily
if input[1]:
  f1rewards += x.rp
if input[5]:
  f2rewards += x.rp
if input[11] == 1:
  f1rewards += x.weather
  f2rewards += x.weather
  refxp += x.refweather
if input[11] == 2:
  f1rewards += x.supweather
  f2rewards += x.supweather
  refxp += x.refsupweather
f1rewards += (x.weatherrolls*input[12])
f2rewards += (x.weatherrolls*input[12])
refxp += (x.refweatherrolls*input[12])
xptraptotal = tbase+(txpper*input[10])
if xptraptotal > tmaxxp:
  xptraptotal = tmaxxp
refxp += (x.refxppertrap*input[10])
if input[8]:
  f1rewards += xptraptotal
  f2rewards += xptraptotal
f1reduction = 1-(x.reduction*input[3])
f2reduction = 1-(x.reduction*input[7])
if f1reduction < x.reductionmax:
  f1reduction = x.reductionmax
if f2reduction < x.reductionmax:
  f2reduction = x.reductionmax
f1xp = round(f1rewards*f1reduction)
f2xp = round(f2rewards*f2reduction)
if f1level <= 3 or f1level <= 3:
  refxp *= 2
refxp = round(refxp)
if winner == 1:
  T = f""" :crossed_swords: {f1name} Wins! :crossed_swords:" -f "{f1name} Gains:| {f1xp}XP - {f1rewards}GP" -f "{f2name} Gains:| {f2xp}XP - {f2rewards}GP """
if winner == 2:
  T = f""" :crossed_swords: {f2name} Wins! :crossed_swords:" -f "{f2name} Gains:| {f2xp}XP - {f2rewards}GP" -f "{f1name} Gains:| {f1xp}XP - {f1rewards}GP """
F = f"Ref gets {refxp}XP"
</drac2>
-title "{{T}}"
-footer "{{F}}"
-color ff0000
