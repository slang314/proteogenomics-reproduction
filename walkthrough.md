## The purpose of this github repo is to demonstrate analysis and visualization of data from the 2016 Nature paper, *Proteogenomics connects somatic mutations to signalling in breast cancer* by Mertins et al

The data to be visualized are a proteomic dataset of iTRAQ ratios of 80 breast cancer and 3 healthy tissue mass spectrometry analysis. The data are visualized in a heatmap, volcano plot (fold change, breast cancer vs. healthy proteome expression), and principle component analysis. In particular the principle component analysis is used to visualize data post machine learning clustering (k-means).

To begin, a new workbook containing the data we wish to work with was created from sheet Global-Proteome-G3 in "CPTAC_BC_SupplementaryTable03.xlsx". This new workbook was named "83_bc_prot.xlsx" and is the basis for the heatmap and volcano plots. In order to create a heatmap of all the genes, a custom R script "clean_data.R" is utilized. This script imports and cleans the data, including reproducing the author's original methods of discarding genes with indeterminate measurements and whose standard deviations were less than 1.5. 

Running "clean_data.R" on "83_bc_prot.xlsx" generates "cleaned_data.csv", which is subsequently utilized by a custom Python script "heatmap_script.py" to generate a heatmap. This script makes use of the *plotly* and *pandas* packages for data visualization. This python script also renames the samples to breast cancer and healthy before plotting. Running "heatmap_script.py" on "cleaned_data.csv" generates a heatmap:


![heatmap](https://github.com/slang314/proteogenomics-reproduction/assets/155842228/549c56bc-2f9b-4721-9b9d-ba335d34206f)


Next, another R script, "add_stats.R", was written to concatonate columns and add statistics between the two groups, such as foldchange, p-value (via student's t-test), and negative log_2 of the fold change. This allows us to create a https://en.wikipedia.org/wiki/Volcano_plot_(statistics), a common method of "quickly identify changes in large data sets composed of replicate data." Running "add_stats.R" on "83_bc_prot.xlsx" excel file produces "cleaned_data_plus_stats.csv", which is input into the Python script "volcano.py", producing the following interactive plot in an html window:

![volcano](https://github.com/slang314/proteogenomics-reproduction/assets/155842228/97100941-8c1d-426d-a7a9-0a67ed736b79)

Like the heatmap, the plot is interactive, and statistics and gene names appear upon hovering:

![image](https://github.com/slang314/proteogenomics-reproduction/assets/155842228/778648d8-9313-4773-99a2-f897a1355a9f)

In this manner, one can explore the data at their leisure. The original input can be mined via other scripts for the greatest foldchange and -log_2(p-value) statistics.

**Sources Cited:**

Mertins, P., Mani, D., Ruggles, K. et al. Proteogenomics connects somatic mutations to signalling in breast cancer. Nature 534, 55–62 (2016). https://doi.org/10.1038/nature18003
