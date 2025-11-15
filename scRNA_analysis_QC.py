# Please view README

# Libraries
import scanpy as sc
import anndata as ad
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Lets load a single-cell expression matrix into an AnnData object
# We will use a bone marrow single-cell dataset available from the CZI CellxGene portal
!wget https://datasets.cellxgene.cziscience.com/497ab773-4fd5-4263-9fdf-7b42a68f1351.h5ad

# View our data
adata = sc.read("497ab773-4fd5-4263-9fdf-7b42a68f1351.h5ad")
adata

# view as data frame
adata.to_df()

# Save raw copy
adata.write("adata_raw.h5ad")

# Set and check gene names
adata.var_names = adata.var['feature_name']
genes = adata[0].var_names[adata[0].var_names.str.startswith("MT-")]
genes[:20]

#QC

#Create function for QC
#First remove duplications

#Then capture contaminats by searching for genes that contain their name tags
#These are usual unwanted sources of technical noise
#High mitochondrial gene expression means cell is stressed or dying
#compute pct_counts_MT and remove cells with >5–10% mitochondrial reads
#Ribosomes reflect protein synthesis activity and thus might not be needed
# Dominates expression
#Hemoglobin genes mean red blood cell contamination
#In bone marrow erythroid cluster is expected
#("^HB[^(P)]") means contains HB somewhere in the sequence

#QC function 
def qc(adata):
    # Convert categorical var_names to strings
    adata.var_names = adata.var_names.astype(str)

    # Ensure unique names
    adata.var_names_make_unique()
    adata.obs_names_make_unique()

    #Filter cells with low gene counts
    sc.pp.filter_cells(adata, min_genes=200)

    # Mark mitochondrial, ribosomal, and hemoglobin genes
    adata.var['MT'] = adata.var_names.str.startswith("MT-")
    adata.var['RIBO'] = adata.var_names.str.startswith(("RPS", "RPL"))
    adata.var['HB'] = adata.var_names.str.startswith("^HB[^(P)]", na=False)

    # Calculate QC metrics
    sc.pp.calculate_qc_metrics(
        adata, qc_vars=["MT", "RIBO", "HB"], inplace=True, percent_top=[20], log1p=True
    )

    # Remove extra columns from obs
    remove = [
        "total_counts_mt", "log1p_total_counts_mt",
        "total_counts_ribo", "log1p_total_counts_ribo",
        "total_counts_hb", "log1p_total_counts_hb"
    ]
    adata.obs = adata.obs[[x for x in adata.obs.columns if x not in remove]]

    print(f"✅ QC done for one AnnData: {adata.n_obs} cells, {adata.n_vars} genes.")
    return adata

# Run function
adata = qc(adata)

# Lets see QC results
mt_genes = adata.var[adata.var['MT']]
ribo_genes = adata.var[adata.var['RIBO']]
hemo_genes = adata.var[adata.var['HB']]

mt_genes
ribo_genes
hemo_gene

adata.obs.head()

# Lets graph QC results for better visualisation

# QC graph function
# value can be changed to:
# value = "pct_counts_in_top_20_genes"
# value = "pct_counts_MT"
# value = "n_genes"
# value = "n_counts"

def qc_plot(adata, value="pct_counts_in_top_20_genes"):
    # Convert to DataFrame for convenience
    df = adata.obs.copy()
    sns.set(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

    plt.figure(figsize=(8, 4))
    sns.kdeplot(data=df, x=value, fill=True, color="skyblue", linewidth=2, alpha=0.8)
    plt.axvline(df[value].median(), color="r", linestyle="--", label="Median")
    plt.title(f"Distribution of {value}", fontsize=12)
    plt.xlabel(value.replace("_", " ").title())
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

qc_plot(adata)


# For violin plots (one adata)

# Choose metrics to visualize
qc_metrics = [
    "total_counts",
    "n_genes_by_counts",
    "pct_counts_MT",
    "pct_counts_in_top_20_genes"
]

# Make violin plots
sc.pl.violin(
    adata,
    keys=qc_metrics,         # Metrics to plot
    groupby=None,            # Plot all cells together
    rotation=45,             # Rotate x-axis labels for readability
    jitter=0.4,              # Adds random noise to spread points
    stripplot=True,          # Show individual data points
    multi_panel=True,        # Make separate subplots for each metric
    size=1.5,                # Point size
)

plt.suptitle("Quality Control Metrics per Cell", fontsize=14, fontweight='bold')
plt.show()

# Visualise QC filtering

# This graph gives us the number of cells (x) vs number of total genes (y)
# Data points density = number of mitogenes
# Identify number of transcripts with high mito density (y value)
# Identify number of cells with high mitodensity (x value)
sc.pl.scatter(adata, "n_genes", "n_counts", color="pct_counts_MT")

# Filter out by removing low quality cells/empty droplets
# Keep cells expressing ≥ 1000 genes
sc.pp.filter_cells(adata, min_genes=800)

# Remove doublets easily
sc.pp.scrublet(adata)

# Save copy of the current expression matrix (adata.X) into a counts layer
adata.layers["counts"] = adata.X.copy()

# Save cleaned copy
adata.write("adata_qc.h5ad")

# Change variable name so raw data is untouched
adata.raw = adata

# Lets normalize and log-transform
sc.pp.normalize_total(adata)
sc.pp.log1p(adata)

# Feature selection of top 1000 genes that very the most across cells
sc.pp.highly_variable_genes(adata, n_top_genes= 1000)
# plot
sc.pl.highly_variable_genes(adata)

# Filter out non variable genes for dimensionality reduction + clustering
adata = adata[:, adata.var['highly_variable']]

# Save filtered copy
adata_hvg.write("adata_hvg.h5ad")


