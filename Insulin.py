#Access NCBI at https://ncbi.nlm.nih.gov to access the data to be used.

# data to be cleaned
#ORIGIN      
 #       1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
  #     61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
# //
#clean the data by removing origin, numbers, spaces and signs.     
# malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn

#divide data into specified groups
# 1–24 - malwmrllpllallalwgpdpaaa   (lsinsulin-seq-clean)
# 25–54 - fvnqhlcgshlvealylvcgergffytpkt   (binsulin-seq-clean)
# 55–89 - rreaedlqvgqvelgggpgagslqplalegslqkr  (cinsulin-seq-clean)
# 90–110 - giveqcctsicslyqlenycn  (ainsulin-seq-clean)

# Store the human preproinsulin sequence in a variable called preproinsulin
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
# Store the remaining sequence elements of human insulin in variables
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")
print(preproInsulin)
# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin) #concatenate strings, use the plus sign (+) in the print() statement
print("The sequence of human insulin, chain a:", bInsulin) #The built-in print() function accepts multiple arguments