# Exact phrase-overlap check: word 8-gram shingles (case/punctuation-normalised), merged into passages.
import re,glob,os,json,sys
P=sys.argv[1]; N=8
def toks(s): return re.findall(r"[a-z0-9]+(?:['’][a-z]+)?",s.lower())
src={}
for f in glob.glob(f'{P}/src/*.txt'):
    w=toks(open(f,errors='ignore').read()); k=os.path.basename(f)[:-4]
    for i in range(len(w)-N+1): src.setdefault(' '.join(w[i:i+N]),set()).add(k)
res=[]; total=0; flagged=0
for f in sorted(glob.glob(f'{P}/thesis/*.txt')):
    raw=open(f).read(); w=toks(raw); total+=len(w)
    hit=[False]*len(w); who={}
    for i in range(len(w)-N+1):
        g=' '.join(w[i:i+N])
        if g in src:
            for j in range(i,i+N): hit[j]=True
            who.setdefault(i,src[g])
    flagged+=sum(hit)
    i=0
    while i<len(w):
        if hit[i]:
            j=i
            while j<len(w) and hit[j]: j+=1
            srcs=set()
            for a in range(i,j):
                srcs|=who.get(a,set())
            res.append({'part':os.path.basename(f),'words':j-i,'text':' '.join(w[i:j]),'sources':sorted(srcs)})
            i=j
        else: i+=1
res.sort(key=lambda r:-r['words'])
json.dump({'total_words':total,'matched_words':flagged,'passages':res},open(f'{P}/overlap.json','w'),indent=1)
print('total words',total,'matched',flagged,'pct %.2f'%(100*flagged/total),'passages',len(res))
for r in res[:60]: print(r['words'],r['part'],r['sources'][:3],'|',r['text'][:220])
