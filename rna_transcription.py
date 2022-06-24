'''Program to tranlate DNA into RNA complement'''
def to_rna(dna_strand):
    rna = dna_strand.maketrans({'G':'C','C':'G','T':'A','A':'U'})
    return dna_strand.translate(rna)

if __name__=='__main__':
    print(to_rna(dna_strand='GCTA'))
