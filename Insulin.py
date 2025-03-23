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

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights 
insulin = bInsulin + aInsulin 
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))
molecularWeightInsulinActual = 5807.63   #To calculate the error percentage:error percentage = (| measured – accepted | / accepted)*100%
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

#Calculating the Net Charge of Insulin by Using Python Lists and Loops
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}
#use the count() method and list comprehension to count the number of Y, C, K, H, R, D, and E amino acids.
insulin.count("Y")
float(insulin.count("Y"))
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
pH = 0
while (pH <= 14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    print('{0:.2f}'.format(pH), netCharge)
    pH +=1