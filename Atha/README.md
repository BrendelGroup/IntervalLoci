# 4. *Arabidopsis thaliana*
Process the data as in 0Record

## Summary
'''bash
singularity exec -e -B `pwd` aegean.simg fidibus-ilocus-summary.py --workdir=data/ --outfmt=tsv Att6 Atha At11
singularity exec -e -B `pwd` aegean.simg fidibus-pilocus-summary.py --workdir=data/ --outfmt=tsv Att6 Atha At11
singularity exec -e -B `pwd` aegean.simg fidibus-milocus-summary.py --workdir=data/ --outfmt=tsv Att6 Atha At11
'''

## Clustering
'''bash
singularity exec -e -B `pwd` aegean.simg fidibus --workdir=data/ --local --label=At11 --gdna=ATgdna.fa --gff3=ATaraport11.gff3 --prot=Araport11_genes.201606.pep.fasta --refr=Att6,Atha cluster

./conserved.py --workdir=data/ fidibus.hiloci.tsv Att6 Atha At11 > At_hiloci-conserved.tsv

./breakdown.py --counts <(cat data/*/*.iloci.tsv) fidibus.hiloci.tsv At_hiloci-conserved.tsv > At_breakdown-counts.tsv
./breakdown.py <(cat data/*/*.iloci.tsv) fidibus.hiloci.tsv At_hiloci-conserved.tsv > At_breakdown-bp.tsv
'''
## Compactness
'''bash
singularity exec -e -B `pwd` aegean.simg fidibus-compact.py --workdir=data/ --length=1000000 --iqnt=0.95 --gqnt=0.05 Att6 Atha At11 >phisigma-Atha.tsv
'''