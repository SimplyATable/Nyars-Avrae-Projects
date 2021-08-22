!alias homebrew embed
<drac2>
x = load_json(get_gvar('686ea5d1-7737-4d9b-ae9c-8ed6118f649c'))
if '&1&'.lower()=='help':
  H = x.hh
  C = "e1d4ab"
  return f""" -f "{x.hb}" -f "{x.hf}" """
elif '&1&'.lower()=='cofsa':
  H = x.ch
  C = "525252"
  return f""" -f "{x.cb}" -f "{x.cf}" """
else:
  H = x.dh
  C = "9fb9e3"
  return f""" -f "{x.db}" -f "{x.df}" """
</drac2>
-title "{{H}}"
-color {{C}}
