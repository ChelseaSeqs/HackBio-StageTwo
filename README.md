# Analysis of bone marrow single-cell dataset available from the CZI CellxGene portal

## Code
Available in this repository:
1) Data preprocessing --> scRNA_analysis_QC.py
2) Dimension Reduction --> scRNA_analysis_DR.py
3) Annotation and further analysis --> scRNA_analysis_Anno.py

## Findings
### Cell types
Data set contained 14,783 cells and 17,374 genes.

List each annotated cluster and UMAP

2. Explain the biological role of each cell type
For every annotated label, give a short explanation of what that cell type actually does in bone marrow or peripheral immunity.

Examples:

Neutrophils: short-lived phagocytes, first responders to infection

Plasma cells: antibody factories derived from B cells

Platelets: fragments of megakaryocytes, support clotting

Keep each explanation tight. You are not writing a review paper.

3. Is the tissue source really bone marrow? Justify your answer
Your job is to reason your way toward (or away from) that conclusion using:

expected vs. missing lineage populations

typical frequency distributions

presence or absence of progenitors

If you claim bone marrow, explain the flaws in your logic. Otherwise, justify it biologically. Hand-waving is a fail.

4. Based on the relative abundance of cell types, is the patient healthy or infected?
Use the cluster proportions to make a call.

Your job: defend your conclusion using deviations in:

neutrophils

monocytes

NK cell activation states

lymphocyte depletion or expansion

Do not just guess. Interpret the landscape like a scientist.




