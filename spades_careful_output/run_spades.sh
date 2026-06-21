set -e
true
true
/home/ephraim/miniconda3/envs/spades/bin/spades-hammer /home/ephraim/spades_careful_output/corrected/configs/config.info
/home/ephraim/miniconda3/envs/spades/bin/python3 /home/ephraim/miniconda3/envs/spades/share/spades/spades_pipeline/scripts/compress_all.py --input_file /home/ephraim/spades_careful_output/corrected/corrected.yaml --ext_python_modules_home /home/ephraim/miniconda3/envs/spades/share/spades --max_threads 16 --output_dir /home/ephraim/spades_careful_output/corrected --gzip_output
true
true
/home/ephraim/miniconda3/envs/spades/bin/spades-core /home/ephraim/spades_careful_output/K21/configs/config.info /home/ephraim/spades_careful_output/K21/configs/careful_mode.info
/home/ephraim/miniconda3/envs/spades/bin/spades-core /home/ephraim/spades_careful_output/K33/configs/config.info /home/ephraim/spades_careful_output/K33/configs/careful_mode.info
/home/ephraim/miniconda3/envs/spades/bin/spades-core /home/ephraim/spades_careful_output/K55/configs/config.info /home/ephraim/spades_careful_output/K55/configs/careful_mode.info
/home/ephraim/miniconda3/envs/spades/bin/spades-core /home/ephraim/spades_careful_output/K77/configs/config.info /home/ephraim/spades_careful_output/K77/configs/careful_mode.info
/home/ephraim/miniconda3/envs/spades/bin/python3 /home/ephraim/miniconda3/envs/spades/share/spades/spades_pipeline/scripts/copy_files.py /home/ephraim/spades_careful_output/K77/before_rr.fasta /home/ephraim/spades_careful_output/before_rr.fasta /home/ephraim/spades_careful_output/K77/assembly_graph_after_simplification.gfa /home/ephraim/spades_careful_output/assembly_graph_after_simplification.gfa /home/ephraim/spades_careful_output/K77/final_contigs.fasta /home/ephraim/spades_careful_output/contigs.fasta /home/ephraim/spades_careful_output/K77/first_pe_contigs.fasta /home/ephraim/spades_careful_output/first_pe_contigs.fasta /home/ephraim/spades_careful_output/K77/strain_graph.gfa /home/ephraim/spades_careful_output/strain_graph.gfa /home/ephraim/spades_careful_output/K77/scaffolds.fasta /home/ephraim/spades_careful_output/scaffolds.fasta /home/ephraim/spades_careful_output/K77/scaffolds.paths /home/ephraim/spades_careful_output/scaffolds.paths /home/ephraim/spades_careful_output/K77/assembly_graph_with_scaffolds.gfa /home/ephraim/spades_careful_output/assembly_graph_with_scaffolds.gfa /home/ephraim/spades_careful_output/K77/assembly_graph.fastg /home/ephraim/spades_careful_output/assembly_graph.fastg /home/ephraim/spades_careful_output/K77/final_contigs.paths /home/ephraim/spades_careful_output/contigs.paths
true
true
/home/ephraim/miniconda3/envs/spades/bin/python3 /home/ephraim/miniconda3/envs/spades/share/spades/spades_pipeline/scripts/correction_iteration_script.py --corrected /home/ephraim/spades_careful_output/contigs.fasta --assembled /home/ephraim/spades_careful_output/misc/assembled_contigs.fasta --assembly_type contigs --output_dir /home/ephraim/spades_careful_output --bin_home /home/ephraim/miniconda3/envs/spades/bin
/home/ephraim/miniconda3/envs/spades/bin/python3 /home/ephraim/miniconda3/envs/spades/share/spades/spades_pipeline/scripts/correction_iteration_script.py --corrected /home/ephraim/spades_careful_output/scaffolds.fasta --assembled /home/ephraim/spades_careful_output/misc/assembled_scaffolds.fasta --assembly_type scaffolds --output_dir /home/ephraim/spades_careful_output --bin_home /home/ephraim/miniconda3/envs/spades/bin
true
/home/ephraim/miniconda3/envs/spades/bin/python3 /home/ephraim/miniconda3/envs/spades/share/spades/spades_pipeline/scripts/breaking_scaffolds_script.py --result_scaffolds_filename /home/ephraim/spades_careful_output/scaffolds.fasta --misc_dir /home/ephraim/spades_careful_output/misc --threshold_for_breaking_scaffolds 3
true
