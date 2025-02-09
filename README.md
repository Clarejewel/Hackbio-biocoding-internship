# Hackbio-biocoding-internship
Introduction to coding for biological sciences

**#Stage-Zero Project**
### **README Guide for the Stage-Zero Project

The data structure of choice used was **Dictionary**

--- 

#### ** Project Title & Description**  
```md
# The Information of Members of Team Proline1
This is a simple Python dictionary storing details of five group members, including their names, slack user name, email address, hobby, country, discipline and preferred programming language.
The project's aim was to organise proline member's information using any data structure of choice

```

---

** Data Structure (Dictionary Format)**  
```md

## Data Structure
The dataset is stored in this dictionary with the following format:
```#Hackbio Code for Bio_Stage-zero project
#Stage Zero Project.
#Using dictionary data structure to organize proline members information

#The information will be nested as it contains different groupings/classifications
#The organisation is in alphabetical order

print("Team_Proline1_Members_Info")
Team_Proline1_Info = {
    "Member_1": {
        "Name": "Adeola Akintola",
        "Slack_Username": "adeolaa",
        "Email": " akintolaadeola09@gmail.com",
        "Hobby": "Surfing for information",
        "Country": "Nigeria",
        "Discipline": "Public Health",
        "Programming Language": "Python"
    },

    "Member_2": {
        "Name": "Chika Onyedikachukwu",
        "Slack Username": "Onyedikachukwu",
        "Email": " chikadika18@gmail.com",
        "Hobby": "Reading",
        "Country": "Nigeria",
        "Discipline" : "Medical Laboratory Science",
        "Programming Language": "Python"
    },
    
    "Member_3": {
        "Name": "Judith Mbamalu",
        "Slack Username": "JudithM",
        "Email": " mbamalujudith@gmail.com",
        "Hobby": "Travelling and Learning",
        "Country": "Nigeria",
        "Discipline": "Plant Science",
        "Programming Language": "Python"
    },

    "Member_4": {
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
To access a group member's details:
```
print(Team_Proline1_Info["Member_2"]["Name"])  # Output: Adeola Akintola
```
To modify a member’s information:
```
Team_Proline1_Info["Member_x"]["email"] = "newemail@example.com"
```


