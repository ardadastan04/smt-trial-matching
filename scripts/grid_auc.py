"""AUC over k=0..30 and paired-bootstrap CI vs the default for every policy log in runs/tune_v1_dev/<key>/.

Used to fill docs/tuning/v1_dev_grid.md (2,000 patient resamples, seed 0). Usage:
  python scripts/grid_auc.py gpt5_oracle
"""
import glob
import json
import os
import random
import sys

key=sys.argv[1]
with open('data/pairs.jsonl') as fh:
    gold = {json.loads(line)['pair']: json.loads(line)['gold'] for line in fh}
def per_patient(path):
    out={}
    with open(path) as fh:
        lines = fh.readlines()
    for l in lines:
        ep=json.loads(l); q=ep['qid']; n=len(ep['trials'])
        row=[]
        for k in range(31):
            v=ep['initial_verdicts'] if k==0 or not ep['turns'] else ep['turns'][min(k,len(ep['turns']))-1]['verdicts']
            row.append(sum(v[t]==gold[f'{q}__{t}'] for t in v))
        out[q]=(row,n)
    return out
pols={os.path.basename(p)[:-6]:per_patient(p) for p in glob.glob(f'runs/tune_v1_dev/{key}/*.jsonl')}
def acc(pp,qs,k): return sum(pp[q][0][k] for q in qs)/sum(pp[q][1] for q in qs)
def auc(pp,qs): return sum(acc(pp,qs,k) for k in range(31))/31
qs=sorted(next(iter(pols.values())))
ref=pols['a1_c0_3_n0_3']; rng=random.Random(0)
boots=[[rng.choice(qs) for _ in qs] for _ in range(2000)]
rows=[]
for name,pp in pols.items():
    d=[auc(pp,b)-auc(ref,b) for b in boots]; d.sort()
    rows.append((auc(pp,qs),name,acc(pp,qs,10),acc(pp,qs,30),auc(pp,qs)-auc(ref,qs),d[50],d[1949]))
for r in sorted(rows,reverse=True): print(f'{r[0]:.3f} {r[1]:<15} k10 {r[2]:.3f} k30 {r[3]:.3f} d {r[4]:+.3f} [{r[5]:+.3f},{r[6]:+.3f}]')
