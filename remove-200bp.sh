awk '
BEGIN { RS=">"; ORS="" }
NR>1 {
    # Break entry into lines
    n = split($0, lines, "\n")

    # First line is header
    header = lines[1]

    # Remaining lines are sequence
    seq=""
    for(i=2; i<=n; i++){
        seq = seq lines[i]
    }

    # Check sequence length
    if (length(seq) >= 200) {
        print ">" header "\n" seq "\n"
    }
}
' Genome.fasta > Genome-filtered.fasta

