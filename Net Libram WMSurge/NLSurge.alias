!alias nlsurge embed
{{g,c=load_json(get_gvar('df6f09d2-971a-4209-bb29-6f6c61831be5')),10}}{{r=roll(f"1d{c}-1")}}
{{h,v=load_json(get_gvar(g[r]['gvar'])),1000}}{{u=roll(f"1d{v}-1")}}
{{j,b=load_json(get_gvar('8b93320f-1b3f-43a7-9e53-73e70b9ff526')),100}}{{y=roll(f"1d{b}-1")}}
{{d=(j[y]['desc']) if '&*&'=='duration' else (h[u]['desc'])}}
{{t="Wild Magic Surge - Duration" if '&*&'=='duration' else "Wild Magic Surge!"}}
-title "{{t}}"
-desc "{{d}}"
-color <#dc143c>
