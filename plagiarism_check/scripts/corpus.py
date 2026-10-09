import json,re,sys,os,urllib.request,urllib.parse,subprocess,time,html
S=sys.argv[1]; P=f'{S}/plag'
lib=json.load(open(f'{S}/work/lib.json')); raw=json.load(open(f'{S}/work/csl_raw.json'))
UA={'User-Agent':'Mozilla/5.0 (thesis plagiarism self-check; mailto:thesis-check@example.org)'}
def get(url,binary=False,timeout=60):
    for i in range(2):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=timeout)
            b=r.read(); return b if binary else b.decode('utf-8','ignore')
        except Exception as e: err=e; time.sleep(2)
    return None
log=[]
for it in lib:
    k=it['id']; doi=it.get('DOI'); urls=[]; abstract=''
    if doi:
        d=raw.get(doi) or next((v for kk,v in raw.items() if kk.lower()==doi.lower()),{})
        abstract=html.unescape(re.sub(r'<[^>]+>',' ',d.get('abstract','') or ''))
        u=get('https://api.unpaywall.org/v2/'+urllib.parse.quote(doi)+'?email=thesis-check@example.org')
        if u:
            try:
                j=json.loads(u)
                for loc in ([j.get('best_oa_location')] if j.get('best_oa_location') else [])+(j.get('oa_locations') or []):
                    if loc and loc.get('url_for_pdf'): urls.append(loc['url_for_pdf'])
            except Exception: pass
        if doi.lower().startswith('10.48550/arxiv.'): urls.insert(0,'https://arxiv.org/pdf/'+doi.split('arXiv.')[-1])
    if it.get('URL'):
        U=it['URL']
        if 'neurips.cc' in U: urls.append(U.replace('/paper/','/paper_files/paper/').replace('/hash/','/file/').replace('-Abstract.html','-Paper.pdf'))
        elif 'mlr.press' in U: urls.append(U.replace('.html','/'+U.split('/')[-1].replace('.html','.pdf')))
        elif 'jmlr.org' in U: urls.append('https://jmlr.org/papers/volume12/pedregosa11a/pedregosa11a.pdf')
    if k=='Wachter2018': urls.append('https://jolt.law.harvard.edu/assets/articlePDFs/v31/Counterfactual-Explanations-without-Opening-the-Black-Box-Sandra-Wachter-et-al.pdf')
    if k=='Gunasekara2024': urls.append('https://educationaldatamining.org/EDM2024/proceedings/2024.EDM-posters.104/2024.EDM-posters.104.pdf')
    if k=='DoshiVelez2017': urls.insert(0,'https://arxiv.org/pdf/1702.08608')
    full=''; got=None
    seen=set()
    for url in urls:
        if url in seen: continue
        seen.add(url)
        b=get(url,True,90)
        if b and b[:4]==b'%PDF':
            f=f'{P}/pdf/{k}.pdf'; open(f,'wb').write(b)
            t=subprocess.run(['pdftotext','-q',f,'-'],capture_output=True,text=True).stdout
            if len(t)>2000: full=t; got=url; break
    text=(abstract+'\n'+full).strip()
    if text: open(f'{P}/src/{k}.txt','w').write(text)
    log.append({'id':k,'abstract':len(abstract),'fulltext':len(full),'url':got})
    print(k,len(abstract),len(full),flush=True)
json.dump(log,open(f'{P}/corpus_log.json','w'),indent=1)
