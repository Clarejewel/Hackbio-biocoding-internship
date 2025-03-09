Hackbio-biocoding-internship
Introduction to coding for biological sciences

### **Stage-one

### **README Guide for the Stage-one Project**
### **Instructions:
1. Write a function for translating DNA to protein
2. Write a function that simulates and generates a logistic population growth curve. Your function should include 2 extra parameters that randomize the length of the lag phase and the exponential phase [See population curve here - https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fsrep15159/MediaObjects/41598_2015_Article_BFsrep15159_Fig1_HTML.jpg
). Most living populations follow a logistic population growth. Therefore, your growth curve can be: Population Size vs Time, Cell density vs Time, OD vs Time, CFU vs Time, etc
3. Using your function, generate a dataframe with 100 different growth curves
4. Write a function for determining the time to reach 80% of the maximum growth; usually the carrying capacity
5. Finally, write a function for calculating the hamming distance between your Slack username and twitter/X handle (synthesize if you don’t have one). Feel free to pad it with extra words if they are not of the same length.

### **Solutions

This stage project requires the use of the knowledge of dictionaries and functions. 

### 1. Write a function for translating DNA to protein
   -----
#First, define and assign the codons for amino acids using a dictionary (see stage-0 for dictionaries)
  For this task, I worked with the first ten amino acids. 
  
#Next, write a function that translates DNA to protein.
  Functions are created with 'def'
  
***#How will the function work?***

- The function will take a DNA sequence as input and return the corresponding protein sequence.
  ```
  def protein_translation(dna_sequences):
    protein_sequence = ""

- The function will loop through the DNA sequence in step of 3 to read the DNA sequence in codons (3 nucleotides at a time).
  ```
  for i in range(0, len(dna_sequences), 3):
      codon = dna_sequences[i:i+3]
- It will then check if the codon exists as a key in the dictionary, amino_acids, and add the corresponding amino acid to the protein sequence.
   ```
   for amino_acid, codons in amino_acids.items():
        if codon in codons:
           protein_sequence += amino_acid

- Finally, it will return the translated protein sequence.
 ```
return protein_sequence
```
---
##You can test the function with a sample DNA sequence

#Sample DNA sequence
```
dna_sequences = ("CACATATCCATTCCGACCAAACCATGATAAAGTATATGCCACGTCACTATTCATCGTCGATTAGTTTTTA")
```
#calling the function
```
protein_translation(dna_sequences)
```
----

#Output
```
'Histidine Isoleucine Isoleucine Isoleucine Cysteine Histidine Isoleucine Histidine Arginine Arginine '
```

### 2. Write a function that simulates and generates a logistic population growth curve.
Simply speaking, I want to create a function that simulates how a population grows over time using a logistic growth model. 
**Background**
*Look up what a logistic model plot looks like - its an S-curve, a sigmoid function.*
This model has three key phases:
Lag Phase: The population grows slowly at the beginning.
Exponential Phase: The population grows rapidly.
Logistic Growth Phase: The population growth slows down and stabilizes as it approaches a maximum limit (called carrying capacity).

#The logistic growth model has a formula: 

```
#P(t) = K/1+e^-r(t-tmid))

where
#P(t) = the population at time (or f(x) which is the value of the function at point 𝑥 (x could represent a population or other quantities like time, concentration, density, etc
#K = the maximum population (carrying capacity)
#r = the growth rate (how quickly the population grows).
#tmid = the midpoint or inflection point. This represents the point at which the growth changes most rapidly, from slow to fast (or xmid)
```

In the case above, my growth curve is Population Size vs Time, but it can also be Cell density vs Time, OD vs Time, CFU vs Time, etc. 
In creating a function, I can replace the (t) with (x), where x represents any independent variable (e.g., time, population size, concentration etc.).

The function would read thus:

#f(x) = K/1+e^-r(x-xmid)).

#Creating the function using this formula #P(t) = K/1+e^-r(t-tmid))
```
def population_growthcurve_generator(x , r = 2, x_mid = 5):

    solution = 1/(1 + math.exp(-r*(x-x_mid))) #where K is assumed to be 1

    return solution

#the function will be 
def growth_curve_generator(t, K,r,t_mid):
    answer = K/(1 + math.exp(-r*(t-t_mid)))
    return answer
```
#Testing the function with random values for the parameters where t = 10, K = 100,r = 0.1, t_mid = 5
```
import math #importing the math module to use the exponential function

#calling the function
new_population = growth_curve_generator(t = 10, K =100, r = 0.1, t_mid = 5)
print(f"The population size at time t = 10 is {new_population}")

#The output: he population size at time t = 10 is 62.245933120185455

#The population size increases from 0 to 62.2 as time increases from 0 to 10, following the logistic growth curve formula.




