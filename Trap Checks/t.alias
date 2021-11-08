!alias t embed
<drac2>
x = load_json(get_gvar('096fb548-6a06-4c99-9261-cbf29eda04db'))
DC = &*&
R = roll("1d100")
T = f"Trap Roll! (DC {DC})"
D = ["Roll: 1d100 ("]
if R >= DC:
  F = "Safe!"
else:
  F = "Trap!"
D.append(R + ") = `" + R + "`")
if R == 69:
  D.append(f"{x.n}")
if R == 100:
  D.append(f"{x.ma}")
if R == 1:
  D.append(f"{x.mi}")
if R == DC:
  D.append(f"{x.p}")
if R == 42:
  D.append(f"{x.l}")
D = ''.join(D)
</drac2>
-title "{{T}}"
-desc "{{D}}"
-footer "{{F}}"
-footer "{{F}}"
