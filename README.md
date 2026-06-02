# *Lacticaseibacillus paracasei* SCA72564

This repository contains the data and analysis files for the *de novo* genome assembly of the *L. paracasei* strain SCA72564.

Raw Illumina paired-end sequencing reads are accessible at NCBI SRA under accession number [SRR35991900](https://www.ncbi.nlm.nih.gov/sra/SRR35991900).

## Repository Contents

Standard genomic and tabular formats (`.fna`, `.ffn`, `.faa`, `.tsv`, `.csv`) are provided throughout the repository. Any exceptions are explicitly stated within the respective subdirectory's README.

**Important Note on Assembly:** The downstream results located in the `assembly_validation`, `safety_analysis`, and `functional_analysis` directories are derived strictly from the SPAdes `--isolate -s` assembly.

## Tools and Databases

The raw data outputs included in this repository were generated using the following tools:

* **eggNOG-mapper v2.1.12** (Database: eggNOG v5.0.2, Mar. 2021)
* **PlasmidFinder v2.1.6** (Database: plasmidfinder_db v2.2.0, Nov. 2024)
* **Phigaro v2.4.0** (Database: Jan. 2024)
* **ISEScan v1.7.2.3** (Database: Apr. 2021)
* **BLASTX v2.16.0** (Database: PHI-base v4.16, May 2024)
* **BLASTN v2.16.0** (Database: VFDB, Dec. 2024)
* **AMRFinderPlus v4.0.3** (Database: Oct. 2024)
* **ResFinder v4.6.0** (Database: resfinder_db, Aug. 2024)
* **RGI v6.0.3** (Database: CARD Variants v4.0.2, Nov. 2023)
* **PlasmidHunter v1.4.5** (Database: May 2024)
* **mummer2circos v1.4.2** & **Circos v0.69-8**
* **antiSMASH v8.0.4**
* **gutSMASH v2.0.1**

## Excluded Data

Due to GitHub file size constraints, the intermediate trimmed reads (Trimmomatic output) are not hosted in this repository. You may replicate these specific results by retrieving the raw reads ([SRR35991900](https://www.ncbi.nlm.nih.gov/sra/SRR35991900)) and executing standard Trimmomatic paired-end filtering.
