# 3d. *Manacus vitellinus*

## Data retrieval

```bash
# Manacus is not currently part of the default fidibus references. 
# We include the configuration file in yamldir/
fidibus --workdir=data/ \
        --refr=Mvit \
        -c=yamldir/
        download prep iloci breakdown stats
```

## Summary

```bash
genhub-ilocus-summary.py --workdir=data/ --outfmt=tex Mvit
genhub-pilocus-summary.py --workdir=data/ --outfmt=tex Mvit
genhub-milocus-summary.py --workdir=data/ --outfmt=tex Mvit
```

## Compactness

```bash
genhub-compact.py --workdir=data/ --length=1000000 \
                  --iqnt=0.95 --gqnt=0.05 Mvit Hsap Mmus \
    > phisigma-mvit.tsv
```
## Figures
See [03-d-mvit.ipynb](03-d-mvit.ipynb) for visualizations of these data.
