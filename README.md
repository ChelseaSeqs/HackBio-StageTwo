# Analysis of bone marrow single-cell dataset available from the CZI CellxGene portal

## Code
Available in this repository:

1) **Data preprocessing** → `scRNA_analysis_QC.py`  
   Create QC plots to preprocess data and select highly variable genes.  
   ![QC plots](images/qc_plots.png)

2) **Dimension Reduction and Annotation** → `scRNA_analysis_DR.py`  
   Create plots for biological insight.

   

## Findings
### Cell types
Data set contained 14,783 cells and 17,374 genes.

 **UMAP of cells annotated by predicted cell type**  
   ![UMAP](images/umap.png)

**Cell type description:**
* **B cells memory:** Long-lived lymphocytes that retain the specific antibody information from a previous infection, enabling faster and stronger antibody response upon re-exposure to the same pathogen.
* **B cells naive:** Mature but inexperienced B lymphocytes that have not yet encountered a specific antigen.
* **Erythroid-like and erythroid precursor cells:** Hematopoietic cells in the bone marrow that are on the path to becoming mature, oxygen-carrying red blood cells (erythrocytes).
* **Gamma delta T cells:** Unique subset of T cells that patrol epithelial and mucosal surfaces, acting as a bridge between the innate and adaptive immune systems.
* **NK cells (Natural Killer cells):** Innate lymphocytes that kill host cells lacking 'self' markers (MHC class I), making them crucial for early defense against viruses and cancer.
* **Neutrophils:** Most abundant white blood cell, for phagocytosing and killing invading bacteria.
* **Paneth cells:** Specialized epithelial cells located in the small intestine and secrete antimicrobial peptides to maintain the gut barrier.
* **Pericytes:** Mural cells embedded in the basement membrane of capillaries and venules and help with regulating blood-brain barrier integrity.
* **Plasma cells:** Fully differentiated B cell progeny that are dedicated antibody factories, secreting large amounts of a single type of antibody.
* **Platelets:** Small, anucleate cell fragments important for blood clotting and wound repair.
* **T cells:** Key lymphocytes of the adaptive immune system that differentiate into cytotoxic killers or helper cells.
* **Thymocytes:** Developing lymphocytes found in the thymus that undergo selection processes to mature into functional, self-tolerant T cells.


## How do cell types correlate with expected bone marrow lineage population
This dataset is highly consistent with a bone marrow sample. A bone marrow sample is the primary site of adult hematopoiesis, meaning it should contain all major blood cell lineages, including immature and mature stages. The UMAP plot successfully displays all of these expected lineages:
                    * **Myeloid	Monocytes:** *Neutrophils and Macrophages*
                    * **Lymphoid:** *B-cells, T-cells, NK cells, Plasma Cells*
                    * **Erythroid**
                    * **Progenitors/Stem Cells**

## Expected frequency distribution for a bone marrow

 **Dotplot of marker genes**  
   ![Dotplot](images/dotplot.png)

The dominance of Myeloid and B-cell lineages, along with the presence of immature populations, are the hallmarks of an active hematopoietic organ like the bone marrow, as opposed to peripheral blood mononuculear cells (PBMCs). With PBMCs, T-cells are typically the most abundant population. In bone marrow, T-cells and NK cells are present as mature immune cells or tissue-resident cells, but their frequency is surpassed by the developing B-cells and the heavily produced myeloid cells.



   **Dotplot of marker genes**  
   ![Dotplot](images/dotplot.png)

   **Stacked violin plot of marker genes**  
   ![Stacked Violin](images/stacked_violin.png)
Annotated cluster
![UMAP plot](images/final_umap.png)



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




