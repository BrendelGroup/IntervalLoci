# Annotation/Assembly comparisons

We investigate the transition of iLoci between assembly and annotation versions for two genomes: Apis mellifera and Arabidopsis thaliana. To do this, we compute chain alignments using LASTZ and postprocess with some custom 
Python scripts. 

We begin by running the LASTZ as follows
```bash
lastz Amh3.iloci.fa[multiple] Amel.iloci.fa --match=1,9 --filter=identity:95 --chain \
		  format=general:name1,length1,size1,name2,length2,size2,identity,nmatch \
		  > entire.tsv
```
This generates a TSV file containing the query iLoci and all of the chains against the target, along with the attributes of both. We are mainly interested in the maximal chain lengths for each query. 

```bash
python3 make_hsp.py # This script creates the high scoring pairs (the map between iLoci)
python3 count_total.py # This script counts the number of iLoci that can be mapped
python3 count.py # This creates Table 6
```

See [comparisons_plot.ipynb](https://github.com/timlai4/IntervalLoci/blob/comparisons/compare/comparison_plots.ipynb) for visualizations of these data.
