Hackbio-biocoding-internship Introduction to coding for biological sciences

**Stage-two
README Guide for the Stage-two Projects

## Task Code 2.1:
## Microbiology

#Look at this dataset here- https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv

#This is the description of the dataset . https://github.com/HackBio-Internship/2025_project_collection/blob/main/Python/Dataset/mcgc_METADATA.txt [open in a new tab, not a file to be downloaded].

## Plot all the growth curves of OD600 vs Time for the different Strains with the following instructions

#For each strain, plot a growth curve of the the knock out (-) an knock in (+) strain overlaid on top of each other

#Using your function from last stage, determine the time to reach the carrying capacity for each strain/mutant

#Generate a scatter plot of the time it takes to reach carrying capacity for the knock out and the knock in strains

#Generate a box plot of the time it takes to reach carrying capacity for the knock out and the knock in strains

#Is there a statistical difference in the time it takes the knock out strains to reach their maximum carrying capacity compared to the knock in strains

#What do you see? Explain your observations as comments in your code.


## Task Code 2.3:
## Botany and Plant Science
#Have a look at this dataset- https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Pesticide_treatment_data.txt

#Some scientists are trying to engineer mutants for a crop to become resistant to a pesticide. They compared the metabolic response of the engineered mutants to the metabolic response of the wild type plants. They took readings after 8 and 24 hours

##Your task
#Calculate the difference in metabolic response (ΔM) between the DMSO treatment from the 24-hour treatment for the wild type and mutants

#Generate a scatter plot showing the difference for ΔM for WT and Mutants

#Fit a line that satifies a y-intercept of 0 and a slope of 1.

#Using a residual cut off of your choice (calculated a the difference between the fitted line and each point) calculate the residual of each point on the scatter plot

#Color metabolites that fall within +/- n of your residual grey. For example, if you have a cut-off of 0.3, color residual values that are within -0.3 and +0.3 grey

#Color metabolites that fall outside this range salmon.

#What are these metabolites. How do you explain the trends you see on either direction of the plot?

#Pick any 6 metabolites that fall outside this range and generate a line plot that spans from their 0h treatment to their 8h and 24hr.

#What can you say about the plots you see?




## Task Code 2.7:
## Public Health

#NHANES is a program run by the CDC to assess the health and nutritional status of adults and children in the US. It combines survey questions and physical examinations, including medical and physiological measurements and laboratory tests, and examines a representative sample of about 5,000 people each year. The data is used to determine the prevalence of diseases and risk factors, establish national standards, and support epidemiology studies and health sciences research. This information helps to develop public health policy, design health programs and services, and expand the nation's health knowledge.

Dataset here - https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/nhanes.csv

Data Dictionary - https://github.com/HackBio-Internship/public_datasets/blob/main/R/nhanes_dd.csv

#Tasks:
- Process all NA (either by deleting or by converting to zero) {Hard :fire:}
- Visualize the distribution of BMI, Weight, Weight in pounds (weight *2.2) and Age with an histogram.
- What’s the mean 60-second pulse rate for all participants in the data?
73.63382
- What’s the range of values for diastolic blood pressure in all participants? (Hint: see help for min(), max()).
0-116
- What’s the variance and standard deviation for income among all participants?
- Visualize the relationship between weight and height ?
- Color the points by
    .gender
    .diabetes
    .smoking status
- Conduct t-test between the following variables and make conclusions on the relationship between them based on P-Value
. Age and Gender
. BMI and Diabetes
. Alcohol Year and Relationship Status


### Extra Task Code 2.6:
## Transcriptomics
This is a processed RNAseq dataset involving reading in quantitated gene expression data from an RNA-seq experiment, exploring the data using base R functions and then interpretation. The dataset contains an experiment between a diseased cell line and diseased cell lines treated with compound X. The difference in expression change between the two health status is computed as Fold change to log 2 (Log2FC) and the significance of each is computed in p-value.
Access Dataset Here
Task:
Generate a volcano plot. (Hint search for volcano plot online)
Determine the upregulated genes (Genes with Log2FC > 1 and pvalue < 0.01)
Determine the downregulated genes (Genes with Log2FC < -1 and pvalue < 0.01)
What are the functions of the top 5 upregulated genes and top 5 downregulated genes. (Use genecards)


