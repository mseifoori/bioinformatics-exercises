from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


dmd_gene = SeqIO.read('/mnt/d/Bioinformatics/Seq Records & Files/11532.fasta', format='fasta')

dmd_rna = Seq.transcribe(Seq.reverse_complement(dmd_gene.seq))
dmd_aa_seq = Seq.translate(dmd_rna)

dmd_aa_rec = SeqRecord(seq=dmd_aa_seq,
                       id='P11532',
                       description='DMD Gene Post Translation Amino Acid Sequence')

SeqIO.write(dmd_aa_rec, '/mnt/d/Bioinformatics/Seq Records & Files/dmd_post_translation_aa_seq.fasta', format='fasta')
