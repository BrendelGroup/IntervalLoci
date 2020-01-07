# 4. *Arabidopsis thaliana*
Process the data as in 0Record

## Summary
```bash
singularity exec -e -B `pwd` aegean.simg fidibus-ilocus-summary.py --workdir=data/ --outfmt=tsv Att6 Atha At11
singularity exec -e -B `pwd` aegean.simg fidibus-pilocus-summary.py --workdir=data/ --outfmt=tsv Att6 Atha At11
singularity exec -e -B `pwd` aegean.simg fidibus-milocus-summary.py --workdir=data/ --outfmt=tsv Att6 Atha At11
```

## Compactness
```bash
singularity exec -e -B `pwd` aegean.simg fidibus-compact.py --workdir=data/ --length=1000000 --iqnt=0.95 Att6 Atha At11 > phisigma-Atha.tsv
```
