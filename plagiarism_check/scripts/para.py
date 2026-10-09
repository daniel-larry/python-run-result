# Close-paraphrase check: TF-IDF cosine similarity between thesis sentences and source sentences.
import re,glob,os,json,sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
P=sys.argv[1]; TH=float(sys.argv[2]) if len(sys.argv)>2 else 0.6
def sents(t):
    t=re.sub(r'-\s*\n\s*','',t); t=re.sub(r'\s+',' ',t)
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z])',t) if 12<=len(s.split())<=80]
src=[];lab=[]
for f in glob.glob(f'{P}/src/*.txt'):
    for s in sents(open(f,errors='ignore').read()): src.append(s); lab.append(os.path.basename(f)[:-4])
th=[];tl=[]
for f in sorted(glob.glob(f'{P}/thesis/*.txt')):
    for s in sents(open(f).read()): th.append(s); tl.append(os.path.basename(f))
v=TfidfVectorizer(stop_words='english',ngram_range=(1,2),min_df=1,sublinear_tf=True).fit(src+th)
A=v.transform(th); B=v.transform(src)
out=[]
for i in range(0,A.shape[0],500):
    sim=cosine_similarity(A[i:i+500],B)
    for r in range(sim.shape[0]):
        j=sim[r].argmax(); s=sim[r,j]
        if s>=TH: out.append({'score':round(float(s),3),'part':tl[i+r],'thesis':th[i+r],'source':lab[j],'source_sentence':src[j]})
out.sort(key=lambda x:-x['score'])
json.dump({'thesis_sentences':len(th),'source_sentences':len(src),'flagged':out},open(f'{P}/paraphrase.json','w'),indent=1)
print('thesis sentences',len(th),'source sentences',len(src),'flagged',len(out))
for o in out[:40]: print(o['score'],o['part'],o['source'],'\n  T:',o['thesis'][:250],'\n  S:',o['source_sentence'][:250])
