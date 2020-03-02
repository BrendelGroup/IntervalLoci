# Annotation/Assembly comparisons

We investigate the transition of iLoci between assembly and annotation versions for two genomes: Apis mellifera and Arabidopsis thaliana. To do this, we compute chain alignments using LASTZ and postprocess with some custom 
Python scripts. 

We begin by calling LASTZ with a command such as:
```bash
lastz Amh3.iloci.fa[multiple] Amel.iloci.fa --match=1,9 --filter=identity:95 --chain \
		  format=general:name1,length1,size1,name2,length2,size2,identity,nmatch \
		  > entire.tsv
```
To run the entire analysis broken down by iLocus type, run the corresponding chain.sh script in each subdirectory. 
This generates a TSV file containing the query iLoci and all of the chains against the target, along with the attributes of both. We are mainly interested in the maximal chain lengths for each query. Additional python scripts 
then processes the TSV files and produces the relevant counts. These may be done by calling hsp.sh and then counts.sh

See [comparisons_plot.ipynb](https://github.com/timlai4/IntervalLoci/blob/comparisons/compare/comparison_plots.ipynb) for visualizations of these data.
