# Hackbio-biocoding-internship
Introduction to coding for biological sciences

**#Stage-Zero**
### **README Guide for the Stage-Zero Project****
**###Instruction: Use any data structure of your choice to organise the given team members' information**

**###Background**
### Data structures are ways to organise data. Data can be organised in lists, tuples, sets or dictionaries.

The data structure of choice used for this task is **Dictionary**
```

# A dictionary is like a mini database in Python. It helps store and retrieve data easily. It makes use of key-value pairs. Like in a real-world dictionary where one looks up a word (key) to find its meaning (value), in Python, a dictionary helps you look up a key to find its associated value. It can also store nested information. 

--- 
```
#### ** Project Title & Description**  
```md
# The Information of Members of Team Proline1

#The project contains a simple Python dictionary storing details of five group members, including their names, slack user name, email address, hobby, country, discipline and preferred programming language.

#The information is nested as it contains different groupings/classifications

#The organisation is in alphabetical order


```

---

** Data Structure (Dictionary Format)**  
```md

## Data Structure
The dataset is stored in this dictionary with the following format:
```#Stage Zero Project: Using dictionary data structure to organize proline members information

print("Team_Proline1_Members_Info")
Team_Proline1_Info = {
    "Member_1": {
        "Name": "Adeola Akintola",
        "Slack Username": "adeolaa",
        "Email": " akintolaadeola09@gmail.com",
        "Hobby": "Surfing for information",
        "Country": "Nigeria",
        "Discipline": "Public Health",
        "Programming Language": "Python"
    },

    "Member_2" : {
        "Name": "Alamin Omitogun",
        "Slack Username": "Alamin",
        "Email": "omitogunaminbabatunde@gmail.com",
        "Hobby": "Running, reading",
        "Country": "Nigeria",
        "Discipline": "Pharmacology, Cell biology",
         "Programming Language": "Python"
    },
    
    "Member_3": {
        "Name": "Chika Onyedikachukwu",
        "Slack Username": "Onyedikachukwu",
        "Email": " chikadika18@gmail.com",
        "Hobby": "Reading",
        "Country": "Nigeria",
        "Discipline" : "Medical Laboratory Science",
        "Programming Language": "Python"
    },
    
    "Member_4": {
        "Name": "Judith Mbamalu",
        "Slack Username": "JudithM",
        "Email": " mbamalujudith@gmail.com",
        "Hobby": "Travelling and Learning",
        "Country": "Nigeria",
        "Discipline": "Plant Science",
        "Programming Language": "Python"
    },

    "Member_5": {
        "Name": "Princewill_Ukot Eseoghene Cynthia",
        "Slack Username": "Ese",
        "Email": "princewillukot@gmail.com",
        "Hobby": "Reading and Coding",
        "Country": "Nigeria",
        "Discipline": "Plant Science and Biotechnology",
        "Programming Language": "Python"
    }   

}
print(Team_Proline1_Info)

```

## Usage

#To access a member's info (e.g. Name)
```
print(Team_Proline1_Info["Member_4"]["Name"]) 
#output: Judith Mbamalu

```
#To access a member's email
```
print(Team_Proline1_Info["Member_4"]["Email"])  #output: Judith Mbamalu
```

To modify a member’s information:
```
Team_Proline1_Info["Member_x"]["email"] = "newemail@example.com"

```
Here is what the elements in the dictionary above mean:
```
# Print(): is used to display the output of what is contained in the bracket on the screen.

# "Team_Proline1_Members_Info": This is the title of the entire info to be displayed.

# "Team_Proline1_Info" followed by  an equal to  sign = a curly bracket {} creates the dictionary within which the key-value pairs are housed.

# "Member_4" is a key. Within it is the value which is made up of  another key "Name" with the corresponding value "Judith Mbamalu". Other keys are "Slack Username" "Email", "Hobby", "Country", "Discipline", and "Preferred Language" with their corresponding values following the **colon:**

# Note that this is a nested data set, hence the key-value pair within the key.

# The same applies to all team members (Member_1 to Member_5).
# Each key-value pair is separated with a comma.
# Each member's info is also separated with a comma.








