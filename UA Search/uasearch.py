!alias uasearch embed {{q,g='\n',load_json(get_gvar('3b937704-6825-48c7-bde0-9689f2cc06c1'))}}{{n=" ".join(&ARGS&).lower() if &ARGS& else ''}}{{s=[i for i in g if i.name.lower==n or all([x in i.name.lower() for x in n.split(' ')])]}}
{{s=s[0] if s and (len(s)==1 or s[0].name.lower()==n) else [x.name for x in g] if not n else [x.name for x in s]}}
{{raw=q.join(s)}}{{raw=raw[:1020]+'...' if len(raw)>1024 else raw}}
-title "Fight Club: Allowed UA"
{{(f' -title "{s.name}" -desc "" -f "Description|{s.desc}" -footer "Type: {s.type}"') if 'name' in s else f'-f "List of results containing {n}|{raw if s else "No Matches Found"}"' if n else '-desc "`!testua [search]` to look up something.\n[Source](https://bit.ly/3u73Iu7)"'}}
