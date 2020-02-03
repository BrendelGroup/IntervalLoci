# 3a. *Polistes dominula*

## Summary

```bash
genhub-ilocus-summary.py --workdir=data/ --outfmt=tex Pdom
genhub-pilocus-summary.py --workdir=data/ --outfmt=tex Pdom
genhub-milocus-summary.py --workdir=data/ --outfmt=tex Pdom
```

## Compactness

```bash
fidibus --workdir=data/ \
        --numprocs=3 \
        --refr=Aech,Amh3,Nvit \
        download prep iloci breakdown stats
genhub-compact.py --workdir=data/ --length=2000000 \
                  --iqnt=0.95 --gqnt=0.05 \
                  Amh3 Agam Aech Dmel Pdom Nvit \
    > phisigma-pdom.tsv
```
