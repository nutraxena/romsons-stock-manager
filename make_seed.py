import ast,re,json,calendar,pathlib
source=pathlib.Path('/mnt/data/ROMSONS_Stock_App/app.py').read_text();tree=ast.parse(source)
names={'stockist_of','month_of','norm','num','parse_xlsx','group_name'}
ns={'re':re,'MONTHS':list(calendar.month_name)[1:]}
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names],type_ignores=[]),'x','exec'),ns)
rows=[];logs=[]
for p in pathlib.Path('/mnt/data/ROMSONS_Stock_App/data/uploads').glob('*'):
 if p.suffix.lower()!='.xlsx':continue
 s=ns['stockist_of'](p.name);m=ns['month_of'](p.name)
 try:
  parsed,skipped,warnings=ns['parse_xlsx'](p,s)
  if s=='Paramount Remedies' and m==8:
   import openpyxl
   w=openpyxl.load_workbook(p,read_only=True,data_only=True);sh=w.active
   parsed=[(str(r[1]).strip(),'',*[ns['num'](r[i]) for i in (4,6,8,5,7,9)]) for r in list(sh.values)[7:] if len(r)>9 and isinstance(r[1],str) and r[1].strip() and not r[1].lower().startswith('total')];w.close()
  rows.extend([[s,2026,m,name,code,*values] for name,code,*values in parsed]);logs.append([p.name,len(parsed),warnings])
 except Exception as e:logs.append([p.name,0,str(e)])
pathlib.Path('/mnt/data/romsons-pwa/public/seed.json').write_text(json.dumps(rows,ensure_ascii=False))
print('ROWS',len(rows));print(*logs,sep='\n')
