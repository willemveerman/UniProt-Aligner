# -*- coding: utf-8 -*-


import urllib2
from Bio.Align.Applications import ClustalwCommandline
from Bio import Phylo
from Bio import AlignIO

def protein_aligner(query, id):
    methodcall = "http://www.uniprot.org/uniref/?query=uniprot%3a("+query+")+identity%3a"+id+"&force=yes&format=fasta"#query Uniprot with chosen parameters.
    handle2=urllib2.urlopen(methodcall).read()#pass results from url to handle
    f = open("D:\{}.fasta".format(query),"w")#create output file for results
    f.write(str(handle2))#write results to output file
    f.close()
    clustal_runner(query)
    print(aligner(query))
    tree(query)

clustalw_exe = r"D:\ClustalW2\clustalw2.exe"#Tell Python where ClustalW is located

def clustal_runner(q):#Runs clustal on fasta file and outputs alignment files
    clustalw_cline = ClustalwCommandline(clustalw_exe, infile="D:\{}.fasta".format(q), outfile="D:\{}.aln".format(q))
    return clustalw_cline()

def aligner(q):#Reads alignment files from Clustal and ouputs alignment
    align = AlignIO.read("D:\{}.aln".format(q), "clustal")
    return align

def tree(q):#Reads alignment files from Clustal and ouputs tree
    tree = Phylo.read("D:\{}.dnd".format(q), "newick")
    return Phylo.draw_ascii(tree)

print """Welcome to the protein aligner program.
Produce an abbreviated list of alignments and a tree using the function, 'protein_aligner'.

The function takes two string paramters; 
the name to be searched and the percentage sequence identity.

For example:

protein_aligner("opsd","0.9")

will ouput all proteins with the name 'opsd' which share a sequence identity of 90%."""