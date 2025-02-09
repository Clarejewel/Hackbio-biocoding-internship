#Hackbio Code for Bio_Stage-zero project
#Stage Zero Project.
#Using dictionary data structure to organize proline members information

#The information is nested as it contains different groupings/classifications

#The organisation is in alphabetical order

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

#To access Member's info (e.g. Name)

print(Team_Proline1_Info["Member_4"]["Name"]) 
#output: Judith Mbamalu

#Access a member's email

print(Team_Proline1_Info["Member_4"]["Email"]) 
#output: Judith Mbamalu
