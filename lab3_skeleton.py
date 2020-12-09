#!/usr/bin/python

# Lab 3
# Script: charged_sequence.py
# Problem Description: 
#    Read in amino acid sequences from an input file and
#    calculate statistics on the 'disordered' region.

# Open the sequence file in read mode.
in_file = open("Hsp90_conserved.txt", 'r')

# Open an empty file called 'aaoutput.txt' in write mode
write_file = open("aaoutput.txt", 'w')

##### First, develop the code to process just 1 sequence before trying to
##### process all lines in the file. Use the .readline() method to read the first
##### line of the file and perform all operations and calculations only
##### on that line. Once your code for the first line works, paste it into the 
##### Section 2 below to make it run on all lines.

##### Code for processing the first line only
# Read in the first line of the file
seq_line = in_file.readline().rstrip()
# Remove any trailing newline characters from the sequence 
# refer to rstrip() above

# Split line on tab character and save into two variables
total_seq = seq_line.split("\t")
name = total_seq[0] # first element of list after splitting is name
seq = total_seq[1] # second element of list after splitting is sequence
seq_len = len(seq) # length of sequence

# Extract the 'disordered' region of the Hsp90 sequence
start = seq.find("EYLEE")# disordered region starts at the beginning of the first domain
end = seq.find("LNKTKP") + 5 # disordered region ends at the end of the last domain
disordered_seq = seq[start:end] # disordered region 
disordered_seq_len = len(disordered_seq) # length of disordered sequence

# Find the percentage of negatively charged amino acids in the disordered region
# neg charge AA: Aspartic Acid - D, Glutamic Acid - E
D_count = disordered_seq.count("D") # counts how many occurences of Aspartic Acid are in the sequence
E_count = disordered_seq.count("E") # counts how many occurences of Glutamic Acid are in the sequence
neg_occur = (D_count + E_count) / disordered_seq_len # adds both occurences and divides by total amount of amino acids in disordered sequence
neg_occur_perc = "{:.0%}".format(neg_occur) # formats the decimal as a percentage 

# Find the percentage of positively charged amino acids in the disordered region
# pos charge AA: Arginine - R, Histidine - H, Lysine - K
R_count = disordered_seq.count("R") # counts how many occurences of Arginine are in the sequence
H_count = disordered_seq.count("H") # counts how many occurences of Hisitidine are in the sequence
K_count = disordered_seq.count("H") # counts how many occurences of Lysine are in the sequence
pos_occur = (R_count + H_count + K_count) / disordered_seq_len # adds all three occurences and divides by total amount of amino acids in disordered sequence
pos_occur_perc = "{:.0%}".format(pos_occur) # formats the decimal as a percentage 

# Repeat the calculations above for the complete sequence
D_count_seq = seq.count("D") # counts how many occurences of Aspartic Acid are in the sequence
E_count_seq = seq.count("E") # counts how many occurences of Glutamic Acid are in the sequence
neg_occur_seq = (D_count_seq + E_count_seq) / seq_len # adds both occurences and divides by total amount of amino acids in complete sequence
neg_occur_seq_perc = "{:.0%}".format(neg_occur_seq) # formats the decimal as a percentage 

R_count_seq = seq.count("R") # counts how many occurences of Arginine are in the sequence
H_count_seq = seq.count("H") # counts how many occurences of Hisitidine are in the sequence
K_count_seq = seq.count("K") # counts how many occurences of Lysine are in the sequence
pos_occur_seq = (R_count_seq + H_count_seq + K_count_seq) / seq_len # adds all three occurences and divides by total amount of amino acids in complete sequence
pos_occur_seq_perc = "{:.0%}".format(pos_occur_seq) # formats the decimal as a percentage 

# print output for this line to the file
column = ("Sequence Name\t\t% Positive Disordered\t% Negative Disordered\tDisordered Length\t% Positive Sequence\t% Negative Sequence") # column of information for output file
print(column, file = write_file) # prints first column to output file
print(name, "\t\t", pos_occur_perc, "\t\t\t", neg_occur_perc, "\t\t\t", disordered_seq_len, "\t\t\t", pos_occur_seq_perc, "\t\t\t", neg_occur_seq_perc, file = write_file) # prints data to output file

in_file.close() # closes sequence file
write_file.close() # closes output write file


##### Section 2:  Code for processing all lines in the file
##### NOTE: only try this after you've gotten your code for the
##### first line to work above.
##### To get the for loop to work, replace the XXX and YYY with the appropriate variable names,
##### then copy your code from above. You'll need to uncomment the line with "for".

in_file = open("Hsp90_conserved.txt", 'r') # opens sequence file in read mode
write_file = open("aaoutput.txt", 'w') # opens output file in write mode
column = ("Sequence Name\t\t% Positive Disordered\t% Negative Disordered\tDisordered Length\t% Positive Sequence\t% Negative Sequence") # column of information for output file
print(column, file = write_file) # prints first column to output file

for seq in in_file:
    # indent all your code for the for loop like this
    # fill in your code here
    # Read in the first line of the file
    seq_line = in_file.readline().rstrip()
    # Remove any trailing newline characters from the sequence 
    # refer to rstrip() above
    
    # Split line on tab character and save into two variables
    total_seq = seq_line.split("\t")
    name = total_seq[0] # first element of list after splitting is name
    seq = total_seq[1] # second element of list after splitting is sequence
    seq_len = len(seq) # length of sequence
    
    # Extract the 'disordered' region of the Hsp90 sequence
    start = seq.find("EYLEE")# disordered region starts at the beginning of the first domain
    end = seq.find("LNKTKP") + 5 # disordered region ends at the end of the last domain
    disordered_seq = seq[start:end] # disordered region 
    disordered_seq_len = len(disordered_seq) # length of disordered sequence
    
    # Find the percentage of negatively charged amino acids in the disordered region
    # neg charge AA: Aspartic Acid - D, Glutamic Acid - E
    D_count = disordered_seq.count("D") # counts how many occurences of Aspartic Acid are in the sequence
    E_count = disordered_seq.count("E") # counts how many occurences of Glutamic Acid are in the sequence
    neg_occur = (D_count + E_count) / disordered_seq_len # adds both occurences and divides by total amount of amino acids in disordered sequence
    neg_occur_perc = "{:.0%}".format(neg_occur) # formats the decimal as a percentage 
    
    # Find the percentage of positively charged amino acids in the disordered region
    # pos charge AA: Arginine - R, Histidine - H, Lysine - K
    R_count = disordered_seq.count("R") # counts how many occurences of Arginine are in the sequence
    H_count = disordered_seq.count("H") # counts how many occurences of Hisitidine are in the sequence
    K_count = disordered_seq.count("H") # counts how many occurences of Lysine are in the sequence
    pos_occur = (R_count + H_count + K_count) / disordered_seq_len # adds all three occurences and divides by total amount of amino acids in disordered sequence
    pos_occur_perc = "{:.0%}".format(pos_occur) # formats the decimal as a percentage 
    
    # Repeat the calculations above for the complete sequence
    D_count_seq = seq.count("D") # counts how many occurences of Aspartic Acid are in the sequence
    E_count_seq = seq.count("E") # counts how many occurences of Glutamic Acid are in the sequence
    neg_occur_seq = (D_count_seq + E_count_seq) / seq_len # adds both occurences and divides by total amount of amino acids in complete sequence
    neg_occur_seq_perc = "{:.0%}".format(neg_occur_seq) # formats the decimal as a percentage 
    
    R_count_seq = seq.count("R") # counts how many occurences of Arginine are in the sequence
    H_count_seq = seq.count("H") # counts how many occurences of Hisitidine are in the sequence
    K_count_seq = seq.count("K") # counts how many occurences of Lysine are in the sequence
    pos_occur_seq = (R_count_seq + H_count_seq + K_count_seq) / seq_len # adds all three occurences and divides by total amount of amino acids in complete sequence
    pos_occur_seq_perc = "{:.0%}".format(pos_occur_seq) # formats the decimal as a percentage 
    
    
    # print output for this line to the file
    print(name, "\t\t", pos_occur_perc, "\t\t\t", neg_occur_perc, "\t\t\t", disordered_seq_len, "\t\t\t", pos_occur_seq_perc, "\t\t\t", neg_occur_seq_perc, file = write_file) # prints data to output file
    
    
# Close the input file -- (NOTE this is not inside the for loop, so it should not be indented)
in_file.close()

# Close the output file
write_file.close()
