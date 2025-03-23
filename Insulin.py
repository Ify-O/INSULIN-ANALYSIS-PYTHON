#Access NCBI at https://ncbi.nlm.nih.gov to access the data to be used.

# data to be cleaned
#ORIGIN      
 #       1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
  #     61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
# //
 #clean the data by removing origin, numbers, spaces and signs.     
malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaed
lqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn

#divide data into specified groups
# 1–24 - malwmrllpllallalwgpdpaaa   (lsinsulin-seq-clean)
# 25–54 - fvnqhlcgshlvealylvcgergffytpkt   (binsulin-seq-clean)
# 55–89 - rreaedlqvgqvelgggpgagslqplalegslqkr  (cinsulin-seq-clean)
# 90–110 - giveqcctsicslyqlenycn  (ainsulin-seq-clean)

# Store the human preproinsulin sequence in a variable called preproinsulin
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
#