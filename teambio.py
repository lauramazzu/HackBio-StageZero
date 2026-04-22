# Creating a dictionary structure to store our details

all_bio_combined = {
    "team_member1": {
    "name":"Laura Mazzucchi",
     "affiliation":"a Freelance researcher",
     "loved_gene":"rbcL, also known as RUBISCO",
     "organism":"all photosynthetic organisms",
    },


    "team_member2": {
    "name":"Himabindu Kumdam",
    "affiliation":"insert here",
    "loved_gene":"insert here",
    "organism":"insert here"

    },

    "team_member3": {
        "name": "Devina Sharma",
        "affiliation": "insert here",
        "loved_gene": "insert here",
        "organism": "insert here"

    },
}

#Using a for loop to iterate over each member

print("Hi, we are team-glutamine :), and we are part of the AI Genomic HackBio internship.\nRead below to learn more about us.")
for key in all_bio_combined:
    member = all_bio_combined[key]
    #print(f"Hi, my name is {member["name"]}, {member["affiliation"]}. My favourite gene is {member["loved_gene"]}, "
          #f"which is found in {member["organism"]}")
    print(f"{member["name"]} is a {member["affiliation"]}. Her favourite gene is {member["loved_gene"]}, "
          f"which is found in {member["organism"]}")