import pandas

orientations = ['FF', 'RR', 'FR', 'RF']
for species in ['Scer', 'Cele', 'Crei', 'Mtru', 'Agam', 'Dmel', 'Xtro', 'Drer', 'Mmus', 'Hsap']:
    datafile = 'species/{}/{}.iloci.tsv'.format(species, species)
    data = pandas.read_table(datafile)
    iiloci = data.loc[data.LocusClass == 'iiLocus']
    short = iiloci.loc[iiloci.Length < 750]
    subsets = list()
    for orient in orientations:
        # subset = iiloci.loc[(iiloci.FlankGeneOrient == orient) & (iiloci.Length > 10000)]
        subset = iiloci.loc[(iiloci.FlankGeneOrient == orient)]
        shortsubset = short.loc[short.FlankGeneOrient == orient]
        print(species, orient, '{} / {}'.format(len(shortsubset), len(short)), '{:.4f}'.format(len(shortsubset) / len(short)))
        if orient in ['FR','RF']:
            shortsubset.to_csv('species/{}/{}.short{}iiloci.tsv'.format(species,species,orient),sep='\t',index=False)

