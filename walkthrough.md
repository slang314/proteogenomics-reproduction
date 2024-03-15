# The purpose of this github repo is to demonstrate analysis and visualization of data from the 2016 Nature paper, Proteogenomics connects somatic mutations to signalling in breast cancer by Mertins et al

The data to be visualized are a proteomic dataset of iTRAQ ratios of 80 breast cancer and 3 healthy tissue mass spectrometry analysis. The data are visualized in a heatmap, volcano plot (fold change, breast cancer vs. healthy proteome expression), and principle component analysis. In particular the principle component analysis is used to visualize data post machine learning clustering (k-means).

First, a custom R script is utilized to import and clean the data, including reproducing the author's original methods of discarding genes with indeterminate measurements and whose standard deviations were less than 1.5.
