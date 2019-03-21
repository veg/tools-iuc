import os

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


def parse_abayesqr_output(input_text, output_fasta):
    wd = os.path.join(os.getcwd())
    with open(os.path.join(wd, input_text)) as input_file:
        lines = input_file.readlines()
    records = []
    for i, line in enumerate(lines):
        if i % 2 == 0:
            freq = float(line.split()[-1])
            number = int(i/2)+1
            header = 'haplotype-%d_freq-%f' % (number, freq)
        else:
            seq = Seq(line.strip())
            record = SeqRecord(seq, id=header, description='')
            records.append(record)
    SeqIO.write(records, os.path.join(wd, output_fasta), 'fasta')


if __name__ == '__main__':
    parse_abayesqr_output("test_ViralSeq.txt", "haplotypes.fasta")

