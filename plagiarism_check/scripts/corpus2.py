import json,re,sys,os,urllib.request,html,time
S=sys.argv[1]; P=f'{S}/plag'
lib=json.load(open(f'{S}/work/lib.json')); log={x['id']:x for x in json.load(open(f'{P}/corpus_log.json'))}
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36','Accept':'text/html'}
for it in lib:
    k=it['id']
    if log[k]['fulltext']: continue
    url=('https://doi.org/'+it['DOI']) if it.get('DOI') else it.get('URL')
    if not url: continue
    try:
        h=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read().decode('utf-8','ignore')
    except Exception as e:
        print(k,'ERR',str(e)[:60]); continue
    h=re.sub(r'(?s)<(script|style|nav|header|footer)[^>]*>.*?</\1>',' ',h)
    t=html.unescape(re.sub(r'<[^>]+>',' ',h)); t=re.sub(r'\s+',' ',t)
    if len(t)>3000 and not re.search(r'(?i)just a moment|access denied|captcha|verify you are human',t[:2000]):
        old=open(f'{P}/src/{k}.txt').read() if os.path.exists(f'{P}/src/{k}.txt') else ''
        open(f'{P}/src/{k}.txt','w').write(old+'\n'+t)
        log[k]['html']=len(t); print(k,'html',len(t))
    else: print(k,'blocked/short',len(t))
    time.sleep(1)
json.dump(list(log.values()),open(f'{P}/corpus_log.json','w'),indent=1)
