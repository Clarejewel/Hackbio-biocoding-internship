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


#Organise the information in a more readable format

print("Names                : ",Team_Proline1_Info ["Member_1"]["Name"],   Team_Proline1_Info ["Member_2"]["Name"],   Team_Proline1_Info ["Member_3"]["Name"],  Team_Proline1_Info ["Member_4"]["Name"],  Team_Proline1_Info ["Member_5"]["Name"])
print("Slack Usernames      : ",Team_Proline1_Info ["Member_1"]["Slack Username"],  Team_Proline1_Info ["Member_2"]["Slack Username"],  Team_Proline1_Info ["Member_3"]["Slack Username"],  Team_Proline1_Info ["Member_4"]["Slack Username"],  Team_Proline1_Info ["Member_5"]["Slack Username"])
print("Emails               : ",Team_Proline1_Info ["Member_1"]["Email"],  Team_Proline1_Info ["Member_2"]["Email"],  Team_Proline1_Info ["Member_3"]["Email"],  Team_Proline1_Info ["Member_4"]["Email"],  Team_Proline1_Info ["Member_5"]["Email"])
print("Hobbies              : ",Team_Proline1_Info ["Member_1"]["Hobby"],  Team_Proline1_Info ["Member_2"]["Hobby"],  Team_Proline1_Info ["Member_3"]["Hobby"],  Team_Proline1_Info ["Member_4"]["Hobby"],  Team_Proline1_Info ["Member_5"]["Hobby"])
print("Countries            : ",Team_Proline1_Info ["Member_1"]["Country"],  Team_Proline1_Info ["Member_2"]["Country"],  Team_Proline1_Info ["Member_3"]["Country"],  Team_Proline1_Info ["Member_4"]["Country"],  Team_Proline1_Info ["Member_5"]["Country"])
print("Disciplines          : ",Team_Proline1_Info ["Member_1"]["Discipline"],  Team_Proline1_Info ["Member_2"]["Discipline"],  Team_Proline1_Info ["Member_3"]["Discipline"],  Team_Proline1_Info ["Member_4"]["Discipline"],  Team_Proline1_Info ["Member_5"]["Discipline"])
print("Programming Languages: ", Team_Proline1_Info ["Member_1"]["Programming Language"],  Team_Proline1_Info ["Member_2"]["Programming Language"],  Team_Proline1_Info ["Member_3"]["Programming Language"],  Team_Proline1_Info ["Member_4"]["Programming Language"],  Team_Proline1_Info ["Member_5"]["Programming Language"])

#Output: 
#Names                :  Adeola Akintola Alamin Omitogun Chika Onyedikachukwu Judith Mbamalu Princewill_Ukot Eseoghene Cynthia
#Slack Usernames      :  adeolaa Alamin Onyedikachukwu JudithM Ese
#Emails               :  akintolaadeola09@gmail.com omitogunaminbabatunde@gmail.com chikadika18@gmail.com mbamalujudith@gmail.com ese.princewillukot@gmail.com
#Hobbies              :  Surfing for information Running, reading Reading Travelling and Learning Reading and Coding
#Countries            :  Nigeria Nigeria Nigeria Nigeria Nigeria
#Disciplines          :  Public Health Pharmacology, Cell biology Medical Laboratory Science Plant Science Plant Science and Biotechnology
#Programming Languages:  Python Python Python Python Python

