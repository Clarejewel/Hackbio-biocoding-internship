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
```

### 3. Using your function, generate a dataframe with 100 different growth curves

100 different growth curves would have different time points with different values of K, r, and t_mid.

#1. FIrst create a list of time points from say, 0 to 25 using the numpy linspace function. It would be a timeline (0 → 25) with 100 time points.
#Something to note: "np.linspace(start, stop, num)" - Creates evenly spaced numbers between start and stop. The num parameter determines how many numbers to generate.

```
import numpy as np
diff_time_points = np.linspace(0,25,100) 
print(diff_time_points)
```

#2. The function will use random values for K, r, and t_mid for each growth curve.
#The random values will be generated using the scipy.stats.uniform.rvs(). 
This function generates random variables from a uniform distribution.
#random_values = uniform.rvs(loc=low, scale=high-low, size=n) where loc is the lower bound, scale is the upper bound, and size is the number of random variables to generate.
```
from scipy.stats import uniform #importing the uniform distribution from scipy.stats
K_values = uniform.rvs(loc = 10, scale = 150, size = 100) 
r_values = uniform.rvs(loc = 0.01, scale = 0.25, size = 100) 
t_mid_values = uniform.rvs(loc = 5, scale = 50, size = 100) #
```

#3. Then compute the 100 different growth curves using the function
The function will loop through the 100 time points and calculate the population size at each time point using the logistic growth curve formula.
The population size at each time point will be stored in a dictionary.
```

import pandas as pd 
growth_curve_data = {} 
```

Generating the 100 different growth curves. The function will store the population size at each time point in a list.
```

for i in range(100):
    K = K_values[i] 
    r = r_values[i] 
    t_mid = t_mid_values[i] 
    population_size = [] 
    for t in diff_time_points:
        population = growth_curve_generator(t, K, r, t_mid) 
        population_size.append(population) 
    growth_curve_data[f"Growth Curve {i+1}"] 
```
    
#4. Finally, the function will create a dataframe with the time points and the population size at each time point.
```
df = pd.DataFrame(growth_curve_data, index = diff_time_points) 
print(df)
```

#Let's visualize some of the growth curves using a line plot.
```
import matplotlib.pyplot as plt #importing the matplotlib library to plot the growth curves 
#Plotting the first 5 growth curves
df.iloc[:, :5].plot() #plots the first 5 growth curves.
plt.xlabel("Time") #x-axis label
plt.ylabel("Population Size") #y-axis label
plt.title("Logistic Population Growth Curves") #title of the plot
plt.show() #displays the plot
```


###4. Write a function for determining the time to reach 80% of the maximum growth; usually the carrying capacity
Time to reach 80% of maximum growth is P(t) = 0.8K.
```
Imput this in this formula "P(t) = K/1+e^-r(t-tmid))" and make t the subject of the formula 

t = t_mid - log(1/0.8) - 1)/r where 0.8 is the percentage (i.e 80%)

```
Now create the function
```
def time_to_80_percent(K, r, t_mid):
    t_80 = t_mid - (math.log(1/0.8) - 1)/r #calculates the time to reach 80% of the maximum growth.
    return t_80 #returns the time to reach 80% of the maximum growth.
```

#Testing the function with random values for K =100, r = 0.1, t_mid = 5
```
time_80_percent = time_to_80_percent(K = 100, r = 0.1, t_mid = 5)
print(f"The time to reach 80% of the maximum growth is {time_80_percent} units of time.")
```

###5. Write a function for calculating the hamming distance between your Slack username and twitter/X handle (synthesize if you don’t have one). Feel free to pad it with extra words if they are not of the same length.

- The Hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.
- The Hamming distance is calculated by comparing the characters at each position in the two strings and counting the number of differences.
- The function will loop through the characters in the two strings and compare them.
- If the characters are different, it will increment the count of differences.
- Finally, it will return the count of differences as the Hamming distance.

#Finally, write a function for calculating the hamming distance between your Slack username and twitter/X handle (synthesize if you don’t have one). Feel free to pad it with extra words if they are not of the same length.
#The Hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.

Slack_username = "JudithMba"
Twitter_handle = "clarejudy"

#First define the function for calculating the Hamming distance between two strings.
```
def hamming_distance(s1, s2):
    distance = 0 #initialize the distance to 0.
    for i in range(len(s1)): #loops through the characters in the strings.
        if s1[i] != s2[i]: #checks if the characters are not equal.
            distance += 1 #increments the distance by 1.
    return distance #returns the Hamming distance.
```
#Testing the function with the Slack username and Twitter (X) handle.
```
hamming_dist = hamming_distance(Slack_username, Twitter_handle)
print(f"The Hamming distance between the Slack username and Twitter handle is {hamming_dist}.")

#The output: The Hamming distance between the Slack username and Twitter handle is 9.
```
This means that the characters in the Slack username and Twitter handle are different at 9 positions.
The Hamming distance is a measure of the dissimilarity between two strings of equal length. A lower Hamming distance indicates greater similarity between the strings, while a higher Hamming distance indicates greater dissimilarity. In this case, the Hamming distance between the Slack username and Twitter handle is 9, indicating that they are different at 9 positions.


