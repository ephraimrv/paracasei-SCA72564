# *Lacticaseibacillus paracasei* subsp. *paracasei* SCA72564

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20723035.svg)](https://doi.org/10.5281/zenodo.20723035)

This repository contains the raw data outputs and analysis files supporting the
*de novo* genome assembly and functional genomic characterization of
*L. paracasei* strain SCA72564, isolated from *Dioscorea esculenta* tubers in
Ilocos Norte, Philippines.

Raw Illumina paired-end sequencing reads are deposited at NCBI SRA under
accession [SRR35991900](https://www.ncbi.nlm.nih.gov/sra/SRR35991900)
(BioProject [PRJNA1293312](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1293312);
BioSample [SAMN53139918](https://www.ncbi.nlm.nih.gov/biosample/SAMN53139918)).
The assembled genome is accessible under GenBank
[JBSNBU010000000](https://www.ncbi.nlm.nih.gov/nuccore/JBSNBU000000000.1)
(GCA\_053769915.1; RefSeq GCF\_053769915.1).

---

## Repository Structure

| Path | Contents |
|---|---|
| `fastQC/` | FastQC v0.12.1 quality reports for raw paired-end reads |
| `spades_careful_output/` | SPAdes v4.2.0 `--careful` assembly (42 contigs; used for MRA announcement) |
| `spades_isolate_output/` | SPAdes v4.2.0 `--isolate` assembly (41 contigs) |
| `spades--isolate-s-output/` | SPAdes v4.2.0 `--isolate -s` assembly — **definitive assembly used for all downstream analyses** (41 contigs; N50 = 404,174 bp) |
| `assembly_validation/` | QUAST v5.3.0 structural metrics; BUSCO v6.0.0 completeness; CheckM2 v1.1.0 quality estimates; FastANI v1.34 and Mash v2.3 ANI tables |
| `bakta_optimized_output/` | Bakta v1.12.0 structural annotation files (`.gff3`, `.gbff`, `.faa`, `.ffn`, `.fna`, `.tsv`) and circular genome map |
| `functional_analysis/` | eggNOG-mapper v2.1.12 COG/KEGG assignments; CAZy subfamily Z-score tables; ProbioMinServer2 enrichment outputs; `figure2_functional_enrichment.py` — custom Python script generating Figure 2 of the manuscript |
| `safety_analysis/` | RGI/CARD, ResFinder, AMRFinderPlus, VFDB (BLASTN), PHI-base (BLASTX), VirulenceFinder, PlasmidFinder, PlasmidHunter, Phigaro, ISEScan outputs |
| `remove-200bp.sh` | Bash script for filtering assembled contigs shorter than 200 bp prior to annotation |
| `LICENSE.md` | MIT License |

> **Note on assembly selection:** All results in `assembly_validation/`,
> `bakta_optimized_output/`, `functional_analysis/`, and `safety_analysis/`
> are derived strictly from the SPAdes `--isolate -s` assembly unless
> explicitly stated otherwise within a subdirectory README.

---

## Tools and Database Versions

### Assembly and Quality Control

| Tool | Version | Purpose |
|---|---|---|
| FastQC | v0.12.1 | Raw read quality assessment |
| Trimmomatic | v0.40 | Adapter removal and quality trimming |
| SPAdes | v4.2.0 | *De novo* genome assembly |
| QUAST | v5.3.0 | Assembly structural metrics |
| BUSCO | v6.0.0 (DB: *lactobacillaceae\_odb12*) | Genome completeness assessment |
| CheckM2 | v1.1.0 | Machine-learning genome quality estimation |
| FastANI | v1.34 | Average Nucleotide Identity (primary) |
| Mash | v2.3 (DB: NCBI type strains, Aug. 2023) | Average Nucleotide Identity (secondary) |

### Annotation and Functional Profiling

| Tool | Version | Purpose |
|---|---|---|
| Bakta | v1.12.0 | Structural genome annotation and circular map |
| eggNOG-mapper | v2.1.12 (DB: eggNOG v5.0.2, Mar. 2021) | COG and KEGG functional categories |
| ProbioMinServer2 | — | Integrated COG/KEGG/CAZy enrichment pipeline |
| antiSMASH | v8.0.4 | Secondary metabolite biosynthetic gene cluster mining |
| gutSMASH | v2.0.1 | Primary metabolic gene cluster mining |

### Safety and Mobile Genetic Elements

| Tool | Version / Database | Purpose |
|---|---|---|
| RGI | v6.0.3 (DB: CARD v4.0.2, Nov. 2023) | Acquired AMR gene detection |
| ResFinder | v4.6.0 (DB: resfinder\_db, Aug. 2024) | AMR gene detection |
| AMRFinderPlus | v4.0.3 (DB: Oct. 2024) | AMR gene detection |
| BLASTN | v2.16.0 (DB: VFDB, Dec. 2024) | Virulence factor screening |
| VirulenceFinder | v2.0.4 | Virulence factor detection |
| BLASTX | v2.16.0 (DB: PHI-base v4.16, May 2024) | Pathogenic marker detection |
| PlasmidFinder | v2.1.6 (DB: plasmidfinder\_db v2.2.0, Nov. 2024) | Plasmid replicon identification |
| PlasmidHunter | v1.4.5 (DB: May 2024) | Plasmid detection |
| Phigaro | v2.4.0 (DB: Jan. 2024) | Prophage mapping |
| ISEScan | v1.7.2.3 (DB: Apr. 2021) | Insertion sequence classification |

### Visualization

| Tool | Version | Purpose |
|---|---|---|
| Matplotlib | v3.10.9 | Custom enrichment plots (Figure 2; see `functional_analysis/`) |

---

## Excluded Data

Due to GitHub file size constraints, trimmed reads (Trimmomatic output) are not
hosted here. To reproduce the trimming step, retrieve the raw reads from SRA
([SRR35991900](https://www.ncbi.nlm.nih.gov/sra/SRR35991900)) and apply
standard Trimmomatic paired-end filtering with `SLIDINGWINDOW:4:20` and a
minimum Phred score of 20.

---

## Citation

If you use data or scripts from this repository, please cite:

> Vallente, J.E.R. (2026). *paracasei-SCA72564: Data and analysis files for
> the de novo genome assembly and \
> functional characterization of
> Lacticaseibacillus paracasei SCA72564* \
> (Version 1.0.0). Zenodo.
> https://doi.org/10.5281/zenodo.20723035


*(Replace the placeholder DOI with the Zenodo DOI once the repository release
is archived. See [zenodo.org](https://zenodo.org) — link your GitHub account
and create a release tagged `v1.0.0` to generate the DOI automatically.)*

---

## License

This repository is released under the MIT License. See `LICENSE.md` for details.
