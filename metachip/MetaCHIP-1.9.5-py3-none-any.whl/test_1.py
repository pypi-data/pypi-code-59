from __future__ import division
#!/usr/bin/env python

# Copyright (C) 2017, Weizhi Song, Torsten Thomas.
# songwz03@gmail.com or t.thomas@unsw.edu.au

# MetaCHIP is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# MetaCHIP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import re
import sys
import copy
import glob
import shutil
import platform
import warnings
import argparse
import itertools
import subprocess
import numpy as np
import multiprocessing as mp
from time import sleep
from ete3 import Tree
from Bio import SeqIO, AlignIO, Align, Phylo
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio.Graphics import GenomeDiagram
from Bio.SeqFeature import FeatureLocation
from Bio.Graphics.GenomeDiagram import CrossLink
from reportlab.lib import colors
from reportlab.lib.units import cm
from datetime import datetime
from string import ascii_uppercase
from scipy.stats import gaussian_kde
from distutils.spawn import find_executable
from MetaCHIP.MetaCHIP_config import config_dict

rank_abbre_dict_plural = {'d': 'domains', 'p': 'phyla', 'c': 'classes', 'o': 'orders', 'f': 'families', 'g': 'genera',
                          's': 'species', 'x': 'specified groups'}


def force_create_folder(folder_to_create):
    if os.path.isdir(folder_to_create):
        shutil.rmtree(folder_to_create, ignore_errors=True)
        if os.path.isdir(folder_to_create):
            shutil.rmtree(folder_to_create, ignore_errors=True)
            if os.path.isdir(folder_to_create):
                shutil.rmtree(folder_to_create, ignore_errors=True)
                if os.path.isdir(folder_to_create):
                    shutil.rmtree(folder_to_create, ignore_errors=True)
    os.mkdir(folder_to_create)


def subset_tree(tree_file_in, leaf_node_list, tree_file_out):
    tree_in = Tree(tree_file_in, format=0)
    tree_in.prune(leaf_node_list, preserve_branch_length=True)
    tree_in.write(format=0, outfile=tree_file_out)


def extract_gene_tree_seq_worker(argument_list):

    each_to_process =               argument_list[0]
    pwd_tree_folder =               argument_list[1]
    pwd_combined_faa_file_subset =  argument_list[2]
    pwd_blastp_exe =                argument_list[3]
    pwd_mafft_exe =                 argument_list[4]
    pwd_fasttree_exe =              argument_list[5]
    genome_to_group_dict =          argument_list[6]
    genome_name_list =              argument_list[7]
    HGT_query_to_subjects_dict =    argument_list[8]
    pwd_SCG_tree_all =              argument_list[9]

    gene_1 = each_to_process[0]
    gene_2 = each_to_process[1]
    HGT_genome_1 = '_'.join(gene_1.split('_')[:-1])
    HGT_genome_2 = '_'.join(gene_2.split('_')[:-1])
    paired_groups = [genome_to_group_dict[HGT_genome_1], genome_to_group_dict[HGT_genome_2]]


    each_to_process_concate = '___'.join(each_to_process)
    blast_output =            '%s/%s___%s_gene_tree_blast.tab'        % (pwd_tree_folder, gene_1, gene_2)
    blast_output_sorted =     '%s/%s___%s_gene_tree_blast_sorted.tab' % (pwd_tree_folder, gene_1, gene_2)
    gene_tree_seq =           '%s/%s___%s_gene_tree.seq'              % (pwd_tree_folder, gene_1, gene_2)
    gene_tree_seq_uniq =      '%s/%s___%s_gene_tree_uniq.seq'         % (pwd_tree_folder, gene_1, gene_2)
    self_seq =                '%s/%s___%s_gene_tree_selfseq.seq'      % (pwd_tree_folder, gene_1, gene_2)
    non_self_seq =            '%s/%s___%s_gene_tree_nonselfseq.seq'   % (pwd_tree_folder, gene_1, gene_2)
    pwd_seq_file_1st_aln =    '%s/%s___%s_gene_tree.1.aln'            % (pwd_tree_folder, gene_1, gene_2)
    pwd_seq_file_2nd_aln =    '%s/%s___%s_gene_tree.2.aln'            % (pwd_tree_folder, gene_1, gene_2)
    pwd_gene_tree_newick =    '%s/%s___%s_gene_tree.newick'           % (pwd_tree_folder, gene_1, gene_2)
    pwd_species_tree_newick = '%s/%s___%s_species_tree.newick'        % (pwd_tree_folder, gene_1, gene_2)

    ################################################## Get gene tree ###################################################

    current_gene_member_BM = set()
    current_gene_member_BM.add(gene_1)
    current_gene_member_BM.add(gene_2)

    if gene_1 in HGT_query_to_subjects_dict:
        for gene_1_subject in HGT_query_to_subjects_dict[gene_1]:
            current_gene_member_BM.add(gene_1_subject)
    if gene_2 in HGT_query_to_subjects_dict:
        for gene_2_subject in HGT_query_to_subjects_dict[gene_2]:
            current_gene_member_BM.add(gene_2_subject)

    current_gene_member_grouped = []
    for gene_member in current_gene_member_BM:
        gene_member_genome = '_'.join(gene_member.split('_')[:-1])
        if gene_member_genome in genome_name_list:
            current_gene_member_grouped.append(gene_member)

    current_gene_member_grouped_from_paired_group = []
    for gene_member in current_gene_member_grouped:
        current_gene_genome = '_'.join(gene_member.split('_')[:-1])
        current_genome_group = genome_to_group_dict[current_gene_genome]
        if current_genome_group in paired_groups:
            current_gene_member_grouped_from_paired_group.append(gene_member)

    # genes to extract
    if len(current_gene_member_grouped_from_paired_group) < 3:
        genes_to_extract_list = current_gene_member_grouped
    else:
        genes_to_extract_list = current_gene_member_grouped_from_paired_group

    # get sequences of othorlog group to build gene tree
    output_handle = open(gene_tree_seq, "w")
    extracted_gene_set = set()
    for seq_record in SeqIO.parse(pwd_combined_faa_file_subset, 'fasta'):
        # if seq_record.id in current_gene_member:
        if seq_record.id in genes_to_extract_list:
            output_handle.write('>%s\n' % seq_record.id)
            output_handle.write('%s\n' % str(seq_record.seq))
            extracted_gene_set.add(seq_record.id)
    output_handle.close()

    if (gene_1 in extracted_gene_set) and (gene_2 in extracted_gene_set):
        self_seq_handle = open(self_seq, 'w')
        non_self_seq_handle = open(non_self_seq, 'w')
        non_self_seq_num = 0
        for each_seq in SeqIO.parse(gene_tree_seq, 'fasta'):
            each_seq_genome_id = '_'.join(each_seq.id.split('_')[:-1])
            if each_seq.id in each_to_process:
                SeqIO.write(each_seq, self_seq_handle, 'fasta')
            elif each_seq_genome_id not in [HGT_genome_1, HGT_genome_2]:
                SeqIO.write(each_seq, non_self_seq_handle, 'fasta')
                non_self_seq_num += 1
        self_seq_handle.close()
        non_self_seq_handle.close()


        # run blast
        genome_subset = set()
        if non_self_seq_num > 0:
            os.system('%s -query %s -subject %s -outfmt 6 -out %s' % (pwd_blastp_exe, self_seq, non_self_seq, blast_output))
            os.system('cat %s | sort > %s' % (blast_output, blast_output_sorted))

            # get best match from each genome
            current_query_subject_genome = ''
            current_bit_score = 0
            current_best_match = ''
            best_match_list = []
            for each_hit in open(blast_output_sorted):
                each_hit_split = each_hit.strip().split('\t')
                query = each_hit_split[0]
                subject = each_hit_split[1]
                subject_genome = '_'.join(subject.split('_')[:-1])
                query_subject_genome = '%s___%s' % (query, subject_genome)
                bit_score = float(each_hit_split[11])
                if current_query_subject_genome == '':
                    current_query_subject_genome = query_subject_genome
                    current_bit_score = bit_score
                    current_best_match = subject
                elif current_query_subject_genome == query_subject_genome:
                    if bit_score > current_bit_score:
                        current_bit_score = bit_score
                        current_best_match = subject
                elif current_query_subject_genome != query_subject_genome:
                    best_match_list.append(current_best_match)
                    current_query_subject_genome = query_subject_genome
                    current_bit_score = bit_score
                    current_best_match = subject
            best_match_list.append(current_best_match)

            # export sequences
            gene_tree_seq_all = best_match_list + each_to_process
            gene_tree_seq_uniq_handle = open(gene_tree_seq_uniq, 'w')
            for each_seq2 in SeqIO.parse(gene_tree_seq, 'fasta'):
                if each_seq2.id in gene_tree_seq_all:
                    gene_tree_seq_uniq_handle.write('>%s\n' % each_seq2.id)
                    gene_tree_seq_uniq_handle.write('%s\n' % str(each_seq2.seq))
            gene_tree_seq_uniq_handle.close()

            cmd_mafft = '%s --quiet %s > %s' % (pwd_mafft_exe, gene_tree_seq_uniq, pwd_seq_file_1st_aln)
            for each_gene in SeqIO.parse(gene_tree_seq_uniq, 'fasta'):
                each_gene_genome = '_'.join(str(each_gene.id).split('_')[:-1])
                genome_subset.add(each_gene_genome)
        else:
            cmd_mafft = '%s --quiet %s > %s' % (pwd_mafft_exe, gene_tree_seq, pwd_seq_file_1st_aln)
            for each_gene in SeqIO.parse(gene_tree_seq, 'fasta'):
                each_gene_genome = '_'.join(str(each_gene.id).split('_')[:-1])
                genome_subset.add(each_gene_genome)

        # run mafft
        os.system(cmd_mafft)

        # run fasttree
        # cmd_fasttree = '%s -quiet %s > %s 2>/dev/null' % (pwd_fasttree_exe, pwd_seq_file_2nd_aln, pwd_gene_tree_newick)
        cmd_fasttree = '%s -quiet %s > %s 2>/dev/null' % (pwd_fasttree_exe, pwd_seq_file_1st_aln, pwd_gene_tree_newick)
        os.system(cmd_fasttree)

        # Get species tree
        subset_tree(pwd_SCG_tree_all, genome_subset, pwd_species_tree_newick)

        # remove temp files
        os.remove(self_seq)
        os.remove(gene_tree_seq)
        if non_self_seq_num > 0:
            os.remove(non_self_seq)
            os.remove(blast_output)
            os.remove(blast_output_sorted)
            os.remove(gene_tree_seq_uniq)


def remove_hyphen_from_branch_length(tree_in, tree_out, tree_format):
    tree_in = Phylo.parse(tree_in, tree_format)
    Phylo.write(tree_in, tree_out, tree_format)


def Ranger_worker(argument_list):
    each_paired_tree = argument_list[0]
    pwd_ranger_inputs_folder = argument_list[1]
    pwd_tree_folder = argument_list[2]
    pwd_ranger_exe = argument_list[3]
    pwd_ranger_outputs_folder = argument_list[4]

    # define Ranger-DTL input file name
    each_paired_tree_concate = '___'.join(each_paired_tree)
    pwd_species_tree_newick                                 = '%s/%s_species_tree.newick'                               % (pwd_tree_folder, each_paired_tree_concate)
    pwd_gene_tree_newick                                    = '%s/%s_gene_tree.newick'                                  % (pwd_tree_folder, each_paired_tree_concate)
    pwd_species_tree_newick_no_hyphen_in_branch_length      = '%s/%s_species_tree_no_hyphen_in_branch_length.newick'    % (pwd_tree_folder, each_paired_tree_concate)
    pwd_gene_tree_newick_no_hyphen_in_branch_length         = '%s/%s_gene_tree_no_hyphen_in_branch_length.newick'       % (pwd_tree_folder, each_paired_tree_concate)

    # each_paired_tree_concate_short = '%s___%s' % (each_paired_tree[0].split('_')[-1], each_paired_tree[1].split('_')[-1])

    if (os.path.isfile(pwd_species_tree_newick) is True) and (os.path.isfile(pwd_gene_tree_newick) is True):

        ranger_inputs_file_name = each_paired_tree_concate + '.txt'
        ranger_outputs_file_name = each_paired_tree_concate + '_ranger_output.txt'

        pwd_ranger_inputs = '%s/%s' % (pwd_ranger_inputs_folder, ranger_inputs_file_name)
        pwd_ranger_outputs = '%s/%s' % (pwd_ranger_outputs_folder, ranger_outputs_file_name)


        # remove hyphen from branch length
        remove_hyphen_from_branch_length(pwd_species_tree_newick, pwd_species_tree_newick_no_hyphen_in_branch_length, 'newick')
        remove_hyphen_from_branch_length(pwd_gene_tree_newick, pwd_gene_tree_newick_no_hyphen_in_branch_length, 'newick')

        # read in species tree
        species_tree = Tree(pwd_species_tree_newick_no_hyphen_in_branch_length, format=0)
        species_tree.resolve_polytomy(recursive=True)  # solving multifurcations
        species_tree.convert_to_ultrametric()  # for dated mode

        # read in gene tree
        gene_tree = Tree(pwd_gene_tree_newick_no_hyphen_in_branch_length, format=0)
        gene_tree.resolve_polytomy(recursive=True)  # solving multifurcations

        ################################################################################################################

        # change species tree leaf name for Ranger-DTL2, replace "_" with "XXXXX", then, replace "." with "SSSSS", then replace "-" with "ZZZZZ"
        for each_st_leaf in species_tree:
            each_st_leaf_name = each_st_leaf.name

            # replace '_' with 'XXXXX'
            if '_' in each_st_leaf_name:
                each_st_leaf_name_no_Underline = 'XXAXX'.join(each_st_leaf_name.split('_'))
            else:
                each_st_leaf_name_no_Underline = each_st_leaf_name

            # replace '.' with 'SSSSS'
            if '.' in each_st_leaf_name_no_Underline:
                each_st_leaf_name_no_Underline_no_dot = 'SSASS'.join(each_st_leaf_name_no_Underline.split('.'))
            else:
                each_st_leaf_name_no_Underline_no_dot = each_st_leaf_name_no_Underline

            # replace '-' with 'ZZZZZ'
            if '-' in each_st_leaf_name_no_Underline_no_dot:
                each_st_leaf_name_no_Underline_no_dot_no_hyphen = 'ZZAZZ'.join(each_st_leaf_name_no_Underline_no_dot.split('-'))
            else:
                each_st_leaf_name_no_Underline_no_dot_no_hyphen = each_st_leaf_name_no_Underline_no_dot

            # rename species tree leaf name
            each_st_leaf.name = each_st_leaf_name_no_Underline_no_dot_no_hyphen

        # change gene tree leaf name for Ranger-DTL2, replace "_" with "XXXXX", then, replace "." with "SSSSS"
        for each_gt_leaf in gene_tree:
            each_gt_leaf_name = each_gt_leaf.name

            # replace '_' with 'XXXXX'
            if '_' in each_gt_leaf_name:
                each_gt_leaf_name_no_Underline = 'XXAXX'.join(each_gt_leaf_name.split('_')[:-1])
            else:
                each_gt_leaf_name_no_Underline = each_gt_leaf_name

            # replace '.' with 'SSSSS'
            if '.' in each_gt_leaf_name_no_Underline:
                each_gt_leaf_name_no_Underline_no_dot = 'SSASS'.join(each_gt_leaf_name_no_Underline.split('.'))
            else:
                each_gt_leaf_name_no_Underline_no_dot = each_gt_leaf_name_no_Underline

            # replace '-' with 'ZZZZZ'
            if '-' in each_gt_leaf_name_no_Underline_no_dot:
                each_gt_leaf_name_no_Underline_no_dot_no_hyphen = 'ZZAZZ'.join(each_gt_leaf_name_no_Underline_no_dot.split('-'))
            else:
                each_gt_leaf_name_no_Underline_no_dot_no_hyphen = each_gt_leaf_name_no_Underline_no_dot

            # rename gene tree leaf name
            each_gt_leaf.name = each_gt_leaf_name_no_Underline_no_dot_no_hyphen

        ################################################################################################################

        # write species tree and gene tree to Ranger-DTL input file
        ranger_inputs_file = open(pwd_ranger_inputs, 'w')

        # dated mode
        ranger_inputs_file.write('%s\n%s\n' % (species_tree.write(format=5), gene_tree.write(format=5)))
        ranger_inputs_file.close()

        # check if pwd_ranger_inputs is blank
        ranger_input_file_size = os.stat(pwd_ranger_inputs).st_size

        if ranger_input_file_size > 1:

            hyphen_detected = 'No'
            for line in open(pwd_ranger_inputs):
                if '-' in line:
                    hyphen_detected = 'Yes'

            # run Ranger-DTL
            if hyphen_detected == 'No':
                ranger_parameters = '-q -D 2 -T 3 -L 1'
                ranger_cmd = '%s %s -i %s -o %s' % (pwd_ranger_exe, ranger_parameters, pwd_ranger_inputs, pwd_ranger_outputs)
                os.system(ranger_cmd)


def extract_donor_recipient_sequences(pwd_combined_ffn, recipient_gene_list, donor_gene_list, pwd_recipient_gene_seq_ffn, pwd_recipient_gene_seq_faa, pwd_donor_gene_seq_ffn, pwd_donor_gene_seq_faa):

    pwd_recipient_gene_seq_ffn_handle = open(pwd_recipient_gene_seq_ffn, 'w')
    pwd_recipient_gene_seq_faa_handle = open(pwd_recipient_gene_seq_faa, 'w')
    pwd_donor_gene_seq_ffn_handle = open(pwd_donor_gene_seq_ffn, 'w')
    pwd_donor_gene_seq_faa_handle = open(pwd_donor_gene_seq_faa, 'w')

    for each_seq in SeqIO.parse(pwd_combined_ffn, 'fasta'):

        if str(each_seq.id) in recipient_gene_list:
            # write out nc sequences
            SeqIO.write(each_seq, pwd_recipient_gene_seq_ffn_handle, 'fasta')

            # write out aa sequences
            each_seq_aa = copy.deepcopy(each_seq)
            each_seq_aa.seq = each_seq_aa.seq.translate()
            SeqIO.write(each_seq_aa, pwd_recipient_gene_seq_faa_handle, 'fasta')

        if str(each_seq.id) in donor_gene_list:
            # write out nc sequences
            SeqIO.write(each_seq, pwd_donor_gene_seq_ffn_handle, 'fasta')

            # write out aa sequences
            each_seq_aa = copy.deepcopy(each_seq)
            each_seq_aa.seq = each_seq_aa.seq.translate()
            SeqIO.write(each_seq_aa, pwd_donor_gene_seq_faa_handle, 'fasta')

    pwd_recipient_gene_seq_ffn_handle.close()
    pwd_recipient_gene_seq_faa_handle.close()
    pwd_donor_gene_seq_ffn_handle.close()
    pwd_donor_gene_seq_faa_handle.close()


def Get_circlize_plot(multi_level_detection, output_prefix, pwd_candidates_file_PG_normal_txt, genome_to_taxon_dict, circos_HGT_R, pwd_plot_circos, taxon_rank, taxon_rank_num, pwd_MetaCHIP_op_folder):

    rank_abbre_dict_plural      = {'d': 'domains', 'p': 'phyla', 'c': 'classes', 'o': 'orders', 'f': 'families', 'g': 'genera', 's': 'species', 'x': 'specified groups'}

    pwd_cir_plot_t1 =              '%s/%s_HGTs_among_%s_t1.txt'              % (pwd_MetaCHIP_op_folder, output_prefix, rank_abbre_dict_plural[taxon_rank])
    pwd_cir_plot_t1_sorted =       '%s/%s_HGTs_among_%s_t1_sorted.txt'       % (pwd_MetaCHIP_op_folder, output_prefix, rank_abbre_dict_plural[taxon_rank])
    pwd_cir_plot_t1_sorted_count = '%s/%s_HGTs_among_%s_sorted_count.txt'    % (pwd_MetaCHIP_op_folder, output_prefix, rank_abbre_dict_plural[taxon_rank])
    pwd_cir_plot_matrix_filename = '%s/%s_HGTs_among_%s.txt'                 % (pwd_MetaCHIP_op_folder, output_prefix, rank_abbre_dict_plural[taxon_rank])


    name2taxon_dict = {}
    transfers = []
    for each in open(pwd_candidates_file_PG_normal_txt):
        if not each.startswith('Gene_1'):
            each_split = each.strip().split('\t')
            Gene_1 = each_split[0]
            Gene_2 = each_split[1]
            Genome_1 = '_'.join(Gene_1.split('_')[:-1])
            Genome_2 = '_'.join(Gene_2.split('_')[:-1])

            if Genome_1 in genome_to_taxon_dict:
                Genome_1_taxon = '_'.join(genome_to_taxon_dict[Genome_1].split(' '))
            else:
                Genome_1_taxon = '%s_' % taxon_rank

            if Genome_2 in genome_to_taxon_dict:
                Genome_2_taxon = '_'.join(genome_to_taxon_dict[Genome_2].split(' '))
            else:
                Genome_2_taxon = '%s_' % taxon_rank

            Direction = each_split[5]
            if multi_level_detection == True:
                Direction = each_split[6]

            if '%)' in Direction:
                Direction = Direction.split('(')[0]

            if Genome_1 not in name2taxon_dict:
                name2taxon_dict[Genome_1] = Genome_1_taxon
            if Genome_2 not in name2taxon_dict:
                name2taxon_dict[Genome_2] = Genome_2_taxon
            transfers.append(Direction)


    tmp1 = open(pwd_cir_plot_t1, 'w')
    all_group_id = []
    for each_t in transfers:
        each_t_split = each_t.split('-->')
        donor = each_t_split[0]
        recipient = each_t_split[1]
        donor_id = name2taxon_dict[donor]
        recipient_id = name2taxon_dict[recipient]
        if donor_id not in all_group_id:
            all_group_id.append(donor_id)
        if recipient_id not in all_group_id:
            all_group_id.append(recipient_id)
        tmp1.write('%s,%s\n' % (donor_id, recipient_id))

    tmp1.close()

    os.system('cat %s | sort > %s' % (pwd_cir_plot_t1, pwd_cir_plot_t1_sorted))

    current_t = ''
    count = 0
    tmp2 = open(pwd_cir_plot_t1_sorted_count, 'w')
    for each_t2 in open(pwd_cir_plot_t1_sorted):
        each_t2 = each_t2.strip()
        if current_t == '':
            current_t = each_t2
            count += 1
        elif current_t == each_t2:
            count += 1
        elif current_t != each_t2:
            tmp2.write('%s,%s\n' % (current_t, count))
            current_t = each_t2
            count = 1
    tmp2.write('%s,%s\n' % (current_t, count))
    tmp2.close()

    # read in count as dict
    transfer_count = {}
    for each_3 in open(pwd_cir_plot_t1_sorted_count):
        each_3_split = each_3.strip().split(',')
        key = '%s,%s' % (each_3_split[0], each_3_split[1])
        value = each_3_split[2]
        transfer_count[key] = value

    all_group_id = sorted(all_group_id)

    matrix_file = open(pwd_cir_plot_matrix_filename, 'w')
    matrix_file.write('\t' + '\t'.join(all_group_id) + '\n')
    for each_1 in all_group_id:
        row = [each_1]
        for each_2 in all_group_id:
            current_key = '%s,%s' % (each_2, each_1)
            if current_key not in transfer_count:
                row.append('0')
            else:
                row.append(transfer_count[current_key])
        matrix_file.write('\t'.join(row) + '\n')
    matrix_file.close()

    # get plot with R
    if len(all_group_id) == 1:
        print('Too less group (1), plot skipped')
    elif 1 < len(all_group_id) <= 200:
        os.system('Rscript %s -m %s -p %s' % (circos_HGT_R, pwd_cir_plot_matrix_filename, pwd_plot_circos))
    else:
        print('Too many groups (>200), plot skipped')

    # rm tmp files
    os.system('rm %s' % pwd_cir_plot_t1)
    os.system('rm %s' % pwd_cir_plot_t1_sorted)
    os.system('rm %s' % pwd_cir_plot_t1_sorted_count)


def Get_circlize_plot_customized_grouping(multi_level_detection, output_prefix, pwd_candidates_file_PG_normal_txt, genome_to_group_dict, circos_HGT_R, pwd_plot_circos, pwd_MetaCHIP_op_folder):

    pwd_cir_plot_t1 =              '%s/%s_cir_plot_t1.txt'              % (pwd_MetaCHIP_op_folder, output_prefix)
    pwd_cir_plot_t1_sorted =       '%s/%s_cir_plot_t1_sorted.txt'       % (pwd_MetaCHIP_op_folder, output_prefix)
    pwd_cir_plot_t1_sorted_count = '%s/%s_cir_plot_t1_sorted_count.txt' % (pwd_MetaCHIP_op_folder, output_prefix)
    pwd_cir_plot_matrix_filename = '%s/%s_cir_plot_matrix.csv'          % (pwd_MetaCHIP_op_folder, output_prefix)

    transfers = []
    for each in open(pwd_candidates_file_PG_normal_txt):
        if not each.startswith('Gene_1'):
            each_split = each.strip().split('\t')
            Gene_1 = each_split[0]
            Gene_2 = each_split[1]

            Direction = each_split[5]
            if multi_level_detection == True:
                Direction = each_split[6]

            if '%)' in Direction:
                Direction = Direction.split('(')[0]

            transfers.append(Direction)


    tmp1 = open(pwd_cir_plot_t1, 'w')
    all_group_id = []
    for each_t in transfers:
        each_t_split = each_t.split('-->')
        donor = each_t_split[0]
        recipient = each_t_split[1]
        donor_group = genome_to_group_dict[donor]
        recipient_group = genome_to_group_dict[recipient]
        if donor_group not in all_group_id:
            all_group_id.append(donor_group)
        if recipient_group not in all_group_id:
            all_group_id.append(recipient_group)
        tmp1.write('%s,%s\n' % (donor_group, recipient_group))

    tmp1.close()

    os.system('cat %s | sort > %s' % (pwd_cir_plot_t1, pwd_cir_plot_t1_sorted))

    current_t = ''
    count = 0
    tmp2 = open(pwd_cir_plot_t1_sorted_count, 'w')
    for each_t2 in open(pwd_cir_plot_t1_sorted):
        each_t2 = each_t2.strip()
        if current_t == '':
            current_t = each_t2
            count += 1
        elif current_t == each_t2:
            count += 1
        elif current_t != each_t2:
            tmp2.write('%s,%s\n' % (current_t, count))
            current_t = each_t2
            count = 1
    tmp2.write('%s,%s\n' % (current_t, count))
    tmp2.close()

    # read in count as dict
    transfer_count = {}
    for each_3 in open(pwd_cir_plot_t1_sorted_count):
        each_3_split = each_3.strip().split(',')
        key = '%s,%s' % (each_3_split[0], each_3_split[1])
        value = each_3_split[2]
        transfer_count[key] = value

    all_group_id = sorted(all_group_id)

    matrix_file = open(pwd_cir_plot_matrix_filename, 'w')
    matrix_file.write('\t' + '\t'.join(all_group_id) + '\n')
    for each_1 in all_group_id:
        row = [each_1]
        for each_2 in all_group_id:
            current_key = '%s,%s' % (each_2, each_1)
            if current_key not in transfer_count:
                row.append('0')
            else:
                row.append(transfer_count[current_key])
        matrix_file.write('\t'.join(row) + '\n')
    matrix_file.close()

    # get plot with R
    if len(all_group_id) > 1:
        os.system('Rscript %s -m %s -p %s' % (circos_HGT_R, pwd_cir_plot_matrix_filename, pwd_plot_circos))

    # rm tmp files
    os.system('rm %s' % pwd_cir_plot_t1)
    os.system('rm %s' % pwd_cir_plot_t1_sorted)
    os.system('rm %s' % pwd_cir_plot_t1_sorted_count)


def unique_list_elements(list_input):

    list_output = []
    for each_element in list_input:
        if each_element not in list_output:
            list_output.append(each_element)

    return list_output


def combine_PG_output(PG_output_file_list_with_path, output_prefix, detection_ranks, combined_PG_output_normal):

    HGT_identity_dict = {}
    HGT_end_match_dict = {}
    HGT_full_length_match_dict = {}
    HGT_direction_dict = {}
    HGT_occurence_dict = {}
    HGT_concatenated_list = []
    for pwd_PG_output_file in PG_output_file_list_with_path:
        file_path, file_name = os.path.split(pwd_PG_output_file)
        taxon_rank = file_name[len(output_prefix) + 1]
        if taxon_rank in detection_ranks:
            for PG_HGT in open(pwd_PG_output_file):
                if not PG_HGT.startswith('Gene_1'):
                    PG_HGT_split = PG_HGT.strip().split('\t')

                    gene_1 = PG_HGT_split[0]
                    gene_2 = PG_HGT_split[1]
                    identity = float(PG_HGT_split[4])
                    end_match = PG_HGT_split[5]
                    full_length_match = PG_HGT_split[6]
                    direction = PG_HGT_split[7]
                    concatenated = '%s___%s' % (gene_1, gene_2)

                    if concatenated not in HGT_concatenated_list:
                        HGT_concatenated_list.append(concatenated)

                    # store in dict
                    if concatenated not in HGT_identity_dict:
                        HGT_identity_dict[concatenated] = identity

                    if concatenated not in HGT_end_match_dict:
                        HGT_end_match_dict[concatenated] = end_match

                    if concatenated not in HGT_full_length_match_dict:
                        HGT_full_length_match_dict[concatenated] = full_length_match

                    if direction != 'NA':
                        if concatenated not in HGT_direction_dict:
                            HGT_direction_dict[concatenated] = [direction]
                        else:
                            HGT_direction_dict[concatenated].append(direction)

                    if direction != 'NA':
                        if concatenated not in HGT_occurence_dict:
                            HGT_occurence_dict[concatenated] = [taxon_rank]
                        else:
                            HGT_occurence_dict[concatenated].append(taxon_rank)


    detection_ranks_all = ['d', 'p', 'c', 'o', 'f', 'g', 's']
    detection_ranks_list = []
    for each_rank in detection_ranks_all:
        if each_rank in detection_ranks:
            detection_ranks_list.append(each_rank)


    HGT_occurence_dict_0_1_format = {}
    for each_HGT in HGT_occurence_dict:
        occurence_str = ''
        for each_level in detection_ranks_list:
            if each_level in HGT_occurence_dict[each_HGT]:
                occurence_str += '1'
            else:
                occurence_str += '0'
        HGT_occurence_dict_0_1_format[each_HGT] = occurence_str


    combined_output_handle_normal = open(combined_PG_output_normal, 'w')

    combined_output_handle_normal.write('Gene_1\tGene_2\tIdentity\toccurence(%s)\tend_match\tfull_length_match\tdirection\n' % detection_ranks)

    for concatenated_HGT in sorted(HGT_concatenated_list):
        concatenated_HGT_split = concatenated_HGT.split('___')

        concatenated_HGT_direction = 'NA'
        if concatenated_HGT in HGT_direction_dict:

            concatenated_HGT_direction_list = HGT_direction_dict[concatenated_HGT]
            concatenated_HGT_direction_list_uniq = unique_list_elements(concatenated_HGT_direction_list)

            if len(concatenated_HGT_direction_list_uniq) == 1:
                concatenated_HGT_direction = concatenated_HGT_direction_list[0]
            else:
                concatenated_HGT_direction = 'both'
                for HGT_direction in concatenated_HGT_direction_list_uniq:
                    HGT_direction_freq = (concatenated_HGT_direction_list.count(HGT_direction)) * 100 / float(len(concatenated_HGT_direction_list))
                    if HGT_direction_freq > 50:
                        concatenated_HGT_direction = HGT_direction + '(' + str(float("{0:.2f}".format(HGT_direction_freq))) + '%)'

        if concatenated_HGT in HGT_occurence_dict_0_1_format:
            occurence_formatted = HGT_occurence_dict_0_1_format[concatenated_HGT]
        else:
            occurence_formatted = '0'*len(detection_ranks_list)

        for_out = '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (concatenated_HGT_split[0],
                                                    concatenated_HGT_split[1],
                                                    HGT_identity_dict[concatenated_HGT],
                                                    occurence_formatted,
                                                    HGT_end_match_dict[concatenated_HGT],
                                                    HGT_full_length_match_dict[concatenated_HGT],
                                                    concatenated_HGT_direction)

        if (HGT_end_match_dict[concatenated_HGT] == 'no') and (HGT_full_length_match_dict[concatenated_HGT] == 'no') and (concatenated_HGT_direction != 'NA') and (concatenated_HGT_direction != 'both'):
            combined_output_handle_normal.write(for_out)

    combined_output_handle_normal.close()


def BP(args, config_dict):

    output_prefix =             args['p']
    grouping_file =             args['g']
    grouping_levels =           args['r']
    cover_cutoff =              args['cov']
    align_len_cutoff =          args['al']
    flanking_length_kbp =       args['flk']
    identity_percentile =       args['ip']
    end_match_identity_cutoff = args['ei']
    num_threads =               args['t']
    No_Eb_Check =               args['NoEbCheck']
    keep_quiet =                args['quiet']
    keep_temp =                 args['tmp']


    # get path to current script
    flanking_length = flanking_length_kbp * 1000
    warnings.filterwarnings("ignore")
    rank_abbre_dict             = {'d': 'domain', 'p': 'phylum', 'c': 'class', 'o': 'order', 'f': 'family', 'g': 'genus', 's': 'species', 'x': 'specified group'}
    rank_abbre_dict_plural      = {'d': 'domains', 'p': 'phyla', 'c': 'classes', 'o': 'orders', 'f': 'families', 'g': 'genera', 's': 'species', 'x': 'specified groups'}
    rank_to_position_dict       = {'d': 0, 'p': 1, 'c': 2, 'o': 3, 'f': 4, 'g': 5, 's': 6}

    # check whether executables exist
    pwd_blastn_exe = config_dict['blastn']
    pwd_blastp_exe =    config_dict['blastp']
    pwd_mafft_exe =     config_dict['mafft']
    pwd_fasttree_exe =  config_dict['fasttree']
    circos_HGT_R =      config_dict['circos_HGT_R']
    pwd_ranger_exe = config_dict['ranger_linux']
    if platform.system() == 'Darwin':
        pwd_ranger_exe = config_dict['ranger_mac']

    program_list = [pwd_blastn_exe, pwd_ranger_exe, pwd_mafft_exe, pwd_fasttree_exe, pwd_blastp_exe]
    not_detected_programs = []
    for needed_program in program_list:
        if find_executable(needed_program) is None:
            not_detected_programs.append(needed_program)
    if not_detected_programs != []:
        print('%s not detected, program exited!' % ','.join(not_detected_programs))
        exit()


    #################################### find matched grouping file if not provided  ###################################

    if grouping_levels is None:
        grouping_levels = 'x'

    ############################################# define file/folder names #############################################

    MetaCHIP_wd                         = '%s_MetaCHIP_wd'                              % output_prefix
    pwd_log_folder                      = '%s/%s_%s_log_files'                          % (MetaCHIP_wd, output_prefix, grouping_levels)
    pwd_flk_plots_folder                = '%s/%s_%s_flk_plots'                          % (MetaCHIP_wd, output_prefix, grouping_levels)
    pwd_log_file                        = '%s/%s_%s_BP_%s.log'                          % (pwd_log_folder, output_prefix, grouping_levels, datetime.now().strftime('%Y-%m-%d_%Hh-%Mm-%Ss_%f'))
    pwd_ignored_taxonomic_rank_file     = '%s/ignored_taxonomic_rank.txt'               % MetaCHIP_wd
    prodigal_output_folder              = '%s_%s_prodigal_output'                       % (output_prefix, grouping_levels)
    blast_db_folder                     = '%s_%s_blastdb'                               % (output_prefix, grouping_levels)
    blast_cmd_file                      = '%s_%s_blastn_commands.txt'                   % (output_prefix, grouping_levels)
    blast_result_folder                 = '%s_%s_blastn_results'                        % (output_prefix, grouping_levels)
    blast_result_filtered_folder        = '%s_%s_blastn_results_filtered_al%sbp_c%s'    % (output_prefix, grouping_levels, align_len_cutoff, cover_cutoff)
    pwd_prodigal_output_folder          = '%s/%s'                                       % (MetaCHIP_wd, prodigal_output_folder)
    pwd_blast_result_folder             = '%s/%s'                                       % (MetaCHIP_wd, blast_result_folder)
    pwd_blast_result_filtered_folder    = '%s/%s'                                       % (MetaCHIP_wd, blast_result_filtered_folder)
    combined_ffn_file                   = '%s_%s_combined_ffn.fasta'                    % (output_prefix, grouping_levels)
    pwd_combined_ffn_file               = '%s/%s/%s'                                    % (MetaCHIP_wd, blast_db_folder, combined_ffn_file)


    ############################################### filter blastn results ##############################################

    # check whether blast results exist
    blast_result_file_re                = '%s/*.tab' % pwd_blast_result_folder
    blast_result_file_list              = [os.path.basename(file_name) for file_name in glob.glob(blast_result_file_re)]
    blast_result_file_list_basename     = [i.split('_blastn.tab')[0] for i in blast_result_file_list]

    # exit if no blast result was found
    if len(blast_result_file_list) == 0:
        exit()

    # exit if missing blast results were found
    ffn_file_re = '%s/*.ffn' % pwd_prodigal_output_folder
    ffn_file_list = [os.path.basename(file_name) for file_name in glob.glob(ffn_file_re)]
    ffn_file_list_basename = [i.split('.ffn')[0] for i in ffn_file_list]

    # exit if the sizes of blast result files are all empty
    blast_result_file_list_empty = []
    blast_result_file_list_not_empty = []
    for blast_result_file in blast_result_file_list:
        pwd_blast_result_file = '%s/%s' % (pwd_blast_result_folder, blast_result_file)
        blast_result_file_size = os.stat(pwd_blast_result_file).st_size
        if blast_result_file_size == 0:
            blast_result_file_list_empty.append(blast_result_file)
        if blast_result_file_size > 0:
            blast_result_file_list_not_empty.append(blast_result_file)

    empty_file_percentage = float("{0:.2f}".format(len(blast_result_file_list_empty)*100/len(ffn_file_list)))

    # check whether filtered blast results already exist
    filtered_blast_results_found = False
    if os.path.isdir(pwd_blast_result_filtered_folder) is True:
        blast_result_filtered_file_re = '%s/*_filtered.tab' % pwd_blast_result_filtered_folder
        blast_result_filtered_file_list = glob.glob(blast_result_filtered_file_re)

        if len(blast_result_filtered_file_list) == len(ffn_file_list):
            filtered_blast_results_found = True


        # filter blastn results with multiprocessing
        list_for_multiple_arguments_filter_blast_results = []
        for blast_result_file in blast_result_file_list:
            pwd_blast_result_file = '%s/%s' % (pwd_blast_result_folder, blast_result_file)
            blast_result_filtered_file = '%s_filtered.tab' % ('.'.join(blast_result_file.split('.')[:-1]))
            pwd_blast_result_filtered_file = '%s/%s' % (pwd_blast_result_filtered_folder, blast_result_filtered_file)
            list_for_multiple_arguments_filter_blast_results.append([pwd_blast_result_file, align_len_cutoff, cover_cutoff, pwd_blast_result_filtered_file])


    ############################################## perform HGT detection ###############################################

    # get ignored rank list
    ignored_rank_list = []
    if os.path.isfile(pwd_ignored_taxonomic_rank_file) is True:
        for ignored_rank in open(pwd_ignored_taxonomic_rank_file):
            ignored_rank_list.append(ignored_rank.strip())



    ####################################################################################################################
    ########################################### combine BM and PG predictions ##########################################
    ####################################################################################################################

    if grouping_file is not None:

        multi_level_detection = False
        pwd_MetaCHIP_op_folder_re = '%s_MetaCHIP_wd/%s_x*_HGTs_ip%s_al%sbp_c%s_ei%s_f%skbp' % (output_prefix, output_prefix, str(identity_percentile), str(align_len_cutoff), str(cover_cutoff), str(end_match_identity_cutoff), flanking_length_kbp)
        MetaCHIP_op_folder = [os.path.basename(file_name) for file_name in glob.glob(pwd_MetaCHIP_op_folder_re)][0]
        group_num = int(MetaCHIP_op_folder[len(output_prefix) + 1:].split('_')[0][1:])

        pwd_MetaCHIP_op_folder =        '%s_MetaCHIP_wd/%s' % (output_prefix, MetaCHIP_op_folder)
        pwd_detected_HGT_PG_txt =       '%s/%s_x%s_HGTs_PG.txt'                      % (pwd_MetaCHIP_op_folder, output_prefix, group_num)
        pwd_flanking_plot_folder =      '%s/%s_x%s_Flanking_region_plots'            % (pwd_MetaCHIP_op_folder, output_prefix, group_num)
        pwd_detected_HGT_txt =          '%s/%s_x_detected_HGTs.txt'                   % (pwd_MetaCHIP_op_folder, output_prefix)
        pwd_recipient_gene_seq_ffn =    '%s/%s_x_detected_HGTs_recipient_genes.ffn'   % (pwd_MetaCHIP_op_folder, output_prefix)
        pwd_recipient_gene_seq_faa =    '%s/%s_x_detected_HGTs_recipient_genes.faa'   % (pwd_MetaCHIP_op_folder, output_prefix)
        pwd_donor_gene_seq_ffn =        '%s/%s_x_detected_HGTs_donor_genes.ffn'       % (pwd_MetaCHIP_op_folder, output_prefix)
        pwd_donor_gene_seq_faa =        '%s/%s_x_detected_HGTs_donor_genes.faa'       % (pwd_MetaCHIP_op_folder, output_prefix)

        pwd_detected_HGT_txt_handle = open(pwd_detected_HGT_txt, 'w')
        pwd_detected_HGT_txt_handle.write('Gene_1\tGene_2\tIdentity\tend_match\tfull_length_match\tdirection\n')
        recipient_gene_list = set()
        donor_gene_list = set()
        flanking_plot_file_list = set()
        for each_HGT in open(pwd_detected_HGT_PG_txt):

            if not each_HGT.startswith('Gene_1'):

                each_HGT_split = each_HGT.strip().split('\t')
                gene_1 = each_HGT_split[0]
                gene_2 = each_HGT_split[1]
                gene_1_genome = '_'.join(gene_1.split('_')[:-1])
                gene_2_genome = '_'.join(gene_2.split('_')[:-1])
                identity = float(each_HGT_split[4])
                end_match = each_HGT_split[5]
                full_length_match = each_HGT_split[6]
                direction = each_HGT_split[7]

                if direction != 'NA':
                    pwd_detected_HGT_txt_handle.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (
                    gene_1, gene_2, identity, end_match, full_length_match, direction))

                    recipient_genome = direction.split('-->')[1]
                    if gene_1_genome == recipient_genome:
                        recipient_gene_list.add(gene_1)
                        donor_gene_list.add(gene_2)
                    if gene_2_genome == recipient_genome:
                        recipient_gene_list.add(gene_2)
                        donor_gene_list.add(gene_1)

                    flanking_plot_file_list.add('%s___%s.SVG' % (gene_1, gene_2))

        pwd_detected_HGT_txt_handle.close()

        extract_donor_recipient_sequences(pwd_combined_ffn_file, recipient_gene_list, donor_gene_list,
                                          pwd_recipient_gene_seq_ffn, pwd_recipient_gene_seq_faa,
                                          pwd_donor_gene_seq_ffn, pwd_donor_gene_seq_faa)

        for each_flk_plot in flanking_plot_file_list:
            pwd_each_flk_plot = '%s/%s_x%s_Flanking_region_plots/1_Plots_normal/%s' % (pwd_MetaCHIP_op_folder, output_prefix, group_num, each_flk_plot)
            os.system('mv %s %s/%s_x%s_Flanking_region_plots/' % (pwd_each_flk_plot, pwd_MetaCHIP_op_folder, output_prefix, group_num))

        ###################################### Get_circlize_plot #######################################

        pwd_plot_circos =               '%s/%s_x%s_HGT_circos.png'                   % (pwd_MetaCHIP_op_folder, output_prefix, group_num)

        # get genome to group dict
        genome_to_group_dict = {}
        for genome in open(grouping_file):
            group_id2 = genome.strip().split(',')[0]
            genome_name = genome.strip().split(',')[1]
            genome_to_group_dict[genome_name] = group_id2

        Get_circlize_plot_customized_grouping(multi_level_detection, output_prefix, pwd_detected_HGT_txt, genome_to_group_dict, circos_HGT_R, pwd_plot_circos, pwd_MetaCHIP_op_folder)

        # remove tmp files
        os.remove(pwd_detected_HGT_PG_txt)
        os.system('rm -r %s/%s_x%s_Flanking_region_plots/1_Plots_normal'            % (pwd_MetaCHIP_op_folder, output_prefix, group_num))
        os.system('rm -r %s/%s_x%s_Flanking_region_plots/2_Plots_end_match'         % (pwd_MetaCHIP_op_folder, output_prefix, group_num))
        os.system('rm -r %s/%s_x%s_Flanking_region_plots/3_Plots_full_length_match' % (pwd_MetaCHIP_op_folder, output_prefix, group_num))

    else:
        detection_rank_list = args['r']

        # for single level detection
        if len(detection_rank_list) == 1:

            multi_level_detection = False
            pwd_MetaCHIP_op_folder_re = '%s_MetaCHIP_wd/%s_%s*_HGTs_ip%s_al%sbp_c%s_ei%s_f%skbp' % (output_prefix, output_prefix, detection_rank_list, str(identity_percentile), str(align_len_cutoff), str(cover_cutoff), str(end_match_identity_cutoff), flanking_length_kbp)
            MetaCHIP_op_folder = [os.path.basename(file_name) for file_name in glob.glob(pwd_MetaCHIP_op_folder_re)][0]
            group_num = int(MetaCHIP_op_folder[len(output_prefix) + 1:].split('_')[0][1:])

            pwd_MetaCHIP_op_folder =        '%s_MetaCHIP_wd/%s'                             % (output_prefix, MetaCHIP_op_folder)
            pwd_detected_HGT_PG_txt =       '%s/%s_%s%s_HGTs_PG.txt'                        % (pwd_MetaCHIP_op_folder, output_prefix, detection_rank_list, group_num)
            pwd_flanking_plot_folder =      '%s/%s_%s%s_Flanking_region_plots'              % (pwd_MetaCHIP_op_folder, output_prefix, detection_rank_list, group_num)
            pwd_detected_HGT_txt =          '%s/%s_%s_detected_HGTs.txt'                    % (pwd_MetaCHIP_op_folder, output_prefix, detection_rank_list)
            pwd_recipient_gene_seq_ffn =    '%s/%s_%s_detected_HGTs_recipient_genes.ffn'    % (pwd_MetaCHIP_op_folder, output_prefix, detection_rank_list)
            pwd_recipient_gene_seq_faa =    '%s/%s_%s_detected_HGTs_recipient_genes.faa'    % (pwd_MetaCHIP_op_folder, output_prefix, detection_rank_list)
            pwd_donor_gene_seq_ffn =        '%s/%s_%s_detected_HGTs_donor_genes.ffn'        % (pwd_MetaCHIP_op_folder, output_prefix, detection_rank_list)
            pwd_donor_gene_seq_faa =        '%s/%s_%s_detected_HGTs_donor_genes.faa'        % (pwd_MetaCHIP_op_folder, output_prefix, detection_rank_list)

            pwd_detected_HGT_txt_handle = open(pwd_detected_HGT_txt, 'w')
            pwd_detected_HGT_txt_handle.write('Gene_1\tGene_2\tIdentity\tend_match\tfull_length_match\tdirection\n')
            recipient_gene_list = set()
            donor_gene_list = set()
            flanking_plot_file_list = set()
            for each_HGT in open(pwd_detected_HGT_PG_txt):

                if not each_HGT.startswith('Gene_1'):

                    each_HGT_split = each_HGT.strip().split('\t')
                    gene_1 = each_HGT_split[0]
                    gene_2 = each_HGT_split[1]
                    gene_1_genome = '_'.join(gene_1.split('_')[:-1])
                    gene_2_genome = '_'.join(gene_2.split('_')[:-1])
                    identity = float(each_HGT_split[4])
                    end_match = each_HGT_split[5]
                    full_length_match = each_HGT_split[6]
                    direction = each_HGT_split[7]

                    if direction != 'NA':
                        pwd_detected_HGT_txt_handle.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (gene_1, gene_2, identity, end_match, full_length_match, direction))

                        recipient_genome = direction.split('-->')[1]
                        if gene_1_genome == recipient_genome:
                            recipient_gene_list.add(gene_1)
                            donor_gene_list.add(gene_2)
                        if gene_2_genome == recipient_genome:
                            recipient_gene_list.add(gene_2)
                            donor_gene_list.add(gene_1)

                        flanking_plot_file_list.add('%s___%s.SVG' % (gene_1, gene_2))

            pwd_detected_HGT_txt_handle.close()

            extract_donor_recipient_sequences(pwd_combined_ffn_file, recipient_gene_list, donor_gene_list, pwd_recipient_gene_seq_ffn, pwd_recipient_gene_seq_faa, pwd_donor_gene_seq_ffn, pwd_donor_gene_seq_faa)

            for each_flk_plot in flanking_plot_file_list:
                pwd_each_flk_plot = '%s/%s_%s%s_Flanking_region_plots/1_Plots_normal/%s' % (pwd_MetaCHIP_op_folder, output_prefix, detection_rank_list, group_num, each_flk_plot)
                os.system('mv %s %s/%s_%s%s_Flanking_region_plots/' % (pwd_each_flk_plot, pwd_MetaCHIP_op_folder, output_prefix, detection_rank_list, group_num))

            ###################################### Get_circlize_plot #######################################

            grouping_file_re = '%s_MetaCHIP_wd/%s_%s*_grouping.txt' % (output_prefix, output_prefix, detection_rank_list)
            grouping_file = [os.path.basename(file_name) for file_name in glob.glob(grouping_file_re)][0]
            taxon_rank_num = grouping_file[len(output_prefix) + 1:].split('_')[0]
            pwd_grouping_file =         '%s_MetaCHIP_wd/%s'                         % (output_prefix, grouping_file)
            pwd_plot_circos =           '%s/%s_%s_HGT_circos.pdf'                   % (pwd_MetaCHIP_op_folder, output_prefix, taxon_rank_num)

            taxon_to_group_id_dict = {}
            for group in open(pwd_grouping_file):
                group_id = group.strip().split(',')[0]
                group_taxon = group.strip().split(',')[2]
                if group_id not in taxon_to_group_id_dict:
                    taxon_to_group_id_dict[group_id] = group_taxon

            # get genome to taxon dict
            genome_to_taxon_dict = {}
            for genome in open(pwd_grouping_file):
                group_id2 = genome.strip().split(',')[0]
                genome_name = genome.strip().split(',')[1]
                genome_to_taxon_dict[genome_name] = taxon_to_group_id_dict[group_id2]

            Get_circlize_plot(multi_level_detection, output_prefix, pwd_detected_HGT_txt, genome_to_taxon_dict, circos_HGT_R, pwd_plot_circos, detection_rank_list, taxon_rank_num, pwd_MetaCHIP_op_folder)


            # remove tmp files
            os.remove(pwd_detected_HGT_PG_txt)
            os.system('rm -r %s/%s_%s%s_Flanking_region_plots/1_Plots_normal'               % (pwd_MetaCHIP_op_folder, output_prefix, detection_rank_list, group_num))
            os.system('rm -r %s/%s_%s%s_Flanking_region_plots/2_Plots_end_match'            % (pwd_MetaCHIP_op_folder, output_prefix, detection_rank_list, group_num))
            os.system('rm -r %s/%s_%s%s_Flanking_region_plots/3_Plots_full_length_match'    % (pwd_MetaCHIP_op_folder, output_prefix, detection_rank_list, group_num))


        # for multiple level detection
        if len(detection_rank_list) > 1:

            time_format = '[%Y-%m-%d %H:%M:%S]'
            print('%s Combine multiple level predictions' % (datetime.now().strftime(time_format)))

            multi_level_detection = True

            pwd_detected_HGT_txt_list = []
            pwd_flanking_plot_folder_list = []
            for detection_rank in detection_rank_list:
                if detection_rank not in ignored_rank_list:
                    pwd_MetaCHIP_op_folder_re = '%s_MetaCHIP_wd/%s_HGT_ip%s_al%sbp_c%s_ei%s_f%skbp_%s*' % (output_prefix, output_prefix, str(identity_percentile), str(align_len_cutoff), str(cover_cutoff), str(end_match_identity_cutoff), flanking_length_kbp, detection_rank)
                    MetaCHIP_op_folder_list = [os.path.basename(file_name) for file_name in glob.glob(pwd_MetaCHIP_op_folder_re)]

                    if 'combined' not in MetaCHIP_op_folder_list[0]:
                        MetaCHIP_op_folder = MetaCHIP_op_folder_list[0]
                    else:
                        MetaCHIP_op_folder = MetaCHIP_op_folder_list[1]

                    group_num = int(MetaCHIP_op_folder.split('_')[-1][1:])
                    pwd_detected_HGT_txt        = '%s_MetaCHIP_wd/%s/%s_%s%s_HGTs_PG.txt' % (output_prefix, MetaCHIP_op_folder, output_prefix, detection_rank, group_num)
                    pwd_flanking_plot_folder    = '%s_MetaCHIP_wd/%s/%s_%s%s_Flanking_region_plots' % (output_prefix, MetaCHIP_op_folder, output_prefix, detection_rank, group_num)
                    pwd_detected_HGT_txt_list.append(pwd_detected_HGT_txt)
                    pwd_flanking_plot_folder_list.append(pwd_flanking_plot_folder)

            pwd_combined_prediction_folder = '%s_MetaCHIP_wd/%s_combined_%s_HGTs_ip%s_al%sbp_c%s_ei%s_f%skbp' % (output_prefix, output_prefix, detection_rank_list, str(identity_percentile), str(align_len_cutoff), str(cover_cutoff), str(end_match_identity_cutoff), flanking_length_kbp)

            genome_size_file =                          '%s_MetaCHIP_wd/%s_all_genome_size.txt'         % (output_prefix, output_prefix)
            pwd_detected_HGT_txt_combined =             '%s/%s_%s_detected_HGTs.txt'                    % (pwd_combined_prediction_folder, output_prefix, detection_rank_list)
            pwd_recipient_gene_seq_ffn =                '%s/%s_%s_detected_HGTs_recipient_genes.ffn'    % (pwd_combined_prediction_folder, output_prefix, detection_rank_list)
            pwd_recipient_gene_seq_faa =                '%s/%s_%s_detected_HGTs_recipient_genes.faa'    % (pwd_combined_prediction_folder, output_prefix, detection_rank_list)
            pwd_donor_gene_seq_ffn =                    '%s/%s_%s_detected_HGTs_donor_genes.ffn'        % (pwd_combined_prediction_folder, output_prefix, detection_rank_list)
            pwd_donor_gene_seq_faa =                    '%s/%s_%s_detected_HGTs_donor_genes.faa'        % (pwd_combined_prediction_folder, output_prefix, detection_rank_list)
            pwd_flanking_plot_folder_combined_tmp =     '%s/%s_%s_Flanking_region_plots_tmp'            % (pwd_combined_prediction_folder, output_prefix, detection_rank_list)
            pwd_flanking_plot_folder_combined =         '%s/%s_%s_Flanking_region_plots'                % (pwd_combined_prediction_folder, output_prefix, detection_rank_list)

            # combine prediction
            force_create_folder(pwd_combined_prediction_folder)
            #print('pwd_detected_HGT_txt_list')
            #print(pwd_detected_HGT_txt_list)
            combine_PG_output(pwd_detected_HGT_txt_list, output_prefix, detection_rank_list, pwd_detected_HGT_txt_combined)


            ############################################### extract sequences ##############################################

            # get recipient and donor gene list
            recipient_gene_list = set()
            recipient_genome_list = []
            donor_gene_list = set()
            plot_file_list = set()
            for each in open(pwd_detected_HGT_txt_combined):
                if not each.startswith('Gene_1'):

                    each_split = each.strip().split('\t')
                    gene_1 = each_split[0]
                    gene_2 = each_split[1]
                    gene_1_genome = '_'.join(gene_1.split('_')[:-1])
                    gene_2_genome = '_'.join(gene_2.split('_')[:-1])
                    direction = each_split[6]
                    plot_file = '%s___%s.SVG' % (gene_1, gene_2)
                    plot_file_list.add(plot_file)

                    recipient_genome = direction.split('-->')[1]
                    if '%)' in recipient_genome:
                        recipient_genome = recipient_genome.split('(')[0]
                    recipient_genome_list.append(recipient_genome)

                    if gene_1_genome == recipient_genome:
                        recipient_gene_list.add(gene_1)
                        donor_gene_list.add(gene_2)
                    if gene_2_genome == recipient_genome:
                        recipient_gene_list.add(gene_2)
                        donor_gene_list.add(gene_1)

            extract_donor_recipient_sequences(pwd_combined_ffn_file, recipient_gene_list, donor_gene_list, pwd_recipient_gene_seq_ffn, pwd_recipient_gene_seq_faa, pwd_donor_gene_seq_ffn, pwd_donor_gene_seq_faa)


            ############################################ combine flanking plots ############################################

            # create plot folders
            os.mkdir(pwd_flanking_plot_folder_combined_tmp)
            os.mkdir(pwd_flanking_plot_folder_combined)

            for flanking_plot_folder in pwd_flanking_plot_folder_list:
                flanking_plot_re = '%s/1_Plots_normal/*.SVG' % flanking_plot_folder
                flanking_plot_list = [os.path.basename(file_name) for file_name in glob.glob(flanking_plot_re)]

                for flanking_plot in flanking_plot_list:
                    pwd_flanking_plot = '%s/1_Plots_normal/%s' % (flanking_plot_folder, flanking_plot)
                    os.system('cp %s %s/' % (pwd_flanking_plot, pwd_flanking_plot_folder_combined_tmp))

                # os.system('cp %s/1_Plots_normal/* %s/' % (flanking_plot_folder, pwd_flanking_plot_folder_combined_tmp))

            for plot_file in plot_file_list:
                pwd_plot_file = '%s/%s' % (pwd_flanking_plot_folder_combined_tmp, plot_file)
                os.system('mv %s %s/' % (pwd_plot_file, pwd_flanking_plot_folder_combined))

            # remove folder for each level detection
            # for flanking_plot_folder in pwd_flanking_plot_folder_list:
            #     each_level_op_folder = '/'.join(flanking_plot_folder.split('/')[:-1])
            #     os.system('mv %s/* %s_MetaCHIP_wd/' % (each_level_op_folder, output_prefix))
            #     os.system('rm -r %s' % each_level_op_folder)


            ###################################### Get_circlize_plot #######################################

            for detection_rank in detection_rank_list:
                if detection_rank not in ignored_rank_list:
                    grouping_file_re = '%s_MetaCHIP_wd/%s_grouping_%s*.txt' % (output_prefix, output_prefix, detection_rank)
                    grouping_file = [os.path.basename(file_name) for file_name in glob.glob(grouping_file_re)][0]
                    print(grouping_file)
                    taxon_rank_num = grouping_file.split('.')[-2].split('_')[-1][1:]
                    pwd_grouping_file =         '%s_MetaCHIP_wd/%s'                         % (output_prefix, grouping_file)
                    pwd_plot_circos =           '%s/%s_HGTs_among_%s.pdf'                   % (pwd_combined_prediction_folder, output_prefix, rank_abbre_dict_plural[detection_rank])
                    pwd_df_circos =             '%s/%s_HGTs_among_%s.tab'                   % (pwd_combined_prediction_folder, output_prefix, rank_abbre_dict_plural[detection_rank])

                    # get genome to taxon dict
                    genome_to_taxon_dict = {}
                    for genome in open(pwd_grouping_file):
                        genome_name = genome.strip().split(',')[1]
                        genome_taxon = genome.strip().split(',')[2]
                        genome_to_taxon_dict[genome_name] = genome_taxon

                    Get_circlize_plot(multi_level_detection, output_prefix, pwd_detected_HGT_txt_combined, genome_to_taxon_dict, circos_HGT_R, pwd_plot_circos, detection_rank, taxon_rank_num, pwd_combined_prediction_folder)

            ###################################### remove tmp files #######################################

            # remove tmp files
            os.system('rm -r %s' % pwd_flanking_plot_folder_combined_tmp)


if __name__ == '__main__':

    # initialize the options parser
    parser = argparse.ArgumentParser()

    parser.add_argument('-p',             required=True,                                help='output prefix')
    parser.add_argument('-r',             required=False, default=None,                 help='grouping rank')
    parser.add_argument('-g',             required=False, default=None,                 help='grouping file')
    parser.add_argument('-cov',           required=False, type=int,     default=75,     help='coverage cutoff, default: 75')
    parser.add_argument('-al',            required=False, type=int,     default=200,    help='alignment length cutoff, default: 200')
    parser.add_argument('-flk',           required=False, type=int,     default=10,     help='the length of flanking sequences to plot (Kbp), default: 10')
    parser.add_argument('-ip',            required=False, type=int,     default=90,     help='identity percentile cutoff, default: 90')
    parser.add_argument('-ei',            required=False, type=float,   default=80,     help='end match identity cutoff, default: 80')
    parser.add_argument('-t',             required=False, type=int,     default=1,      help='number of threads, default: 1')
    parser.add_argument('-NoEbCheck',     required=False, action="store_true",          help='disable end break and contig match check for fast processing, not recommend for metagenome-assembled genomes (MAGs)')
    parser.add_argument('-force',         required=False, action="store_true",          help='overwrite previous results')
    parser.add_argument('-quiet',         required=False, action="store_true",          help='Do not report progress')
    parser.add_argument('-tmp',           required=False, action="store_true",          help='keep temporary files')

    args = vars(parser.parse_args())

    BP(args, config_dict)

