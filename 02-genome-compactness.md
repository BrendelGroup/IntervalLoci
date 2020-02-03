# 2. Evaluation of genome compactness

We assessed the compactness of 10 references genomes on two related measures.

- φ (phi), the proportion of giLoci merged into miLoci
- σ (sigma), the proportion of the genome sequence occupied by miLoci

Because these measures are uninformative on small scales, (φ, σ) values were computed only for chromosome or scaffold sequences of at least 1 Mb in length.
Extremely long iiLoci (those in the top 5% of length for each species) were discarded as outliers prior to computing (φ, σ).

```bash
genhub-compact.py --workdir=data/ --length=1000000 \
                  --iqnt=0.95 --gqnt=0.05 \
                  Scer Cele Crei Mtru Agam Dmel Xtro Drer Mmus Hsap \
    > phisigma-refr.tsv
```

## Different values of δ

To evaluate the robustness of the (φ, σ) measures with respect to the δ (delta) parameter, we recomputed iLoci at δ=300 and δ=750 for comparison with the default δ=500.

```bash
fidibus --workdir=data-delta300/ \
        --numprocs=4 \
        --delta=300 \
        --refr=Scer,Cele,Crei,Mtru,Agam,Dmel,Xtro,Drer,Mmus,Hsap \
        download prep iloci breakdown stats

fidibus --workdir=data-delta750/ \
        --numprocs=4 \
        --delta=750 \
        --refr=Scer,Cele,Crei,Mtru,Agam,Dmel,Xtro,Drer,Mmus,Hsap \
        download prep iloci breakdown stats
```

Centroid (φ, σ) values were then computed for each value of δ for comparison.

```bash
genhub-compact.py --workdir=data/ --centroid=2.25 --length=1000000 \
                  --iqnt=0.95 --gqnt=0.05 \
                  Scer Cele Crei Mtru Agam Dmel Xtro Drer Mmus Hsap \
    > phisigma-refr-delta500.tsv

genhub-compact.py --workdir=data-delta300/ --centroid=2.25 --length=1000000 \
                  --iqnt=0.95 --gqnt=0.05 \
                  Scer Cele Crei Mtru Agam Dmel Xtro Drer Mmus Hsap \
    > phisigma-refr-delta300.tsv

genhub-compact.py --workdir=data-delta750/ --centroid=2.25 --length=1000000 \
                  --iqnt=0.95 --gqnt=0.05 \
                  Scer Cele Crei Mtru Agam Dmel Xtro Drer Mmus Hsap \
    > phisigma-refr-delta750.tsv
```

## Figures

See [02-genome-compactness.ipynb](02-genome-compactness.ipynb) for visualizations of these data.
