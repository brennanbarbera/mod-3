#modules
import os
import csv

counties = ["Arapahoe", "Denver", "Jefferson"]

counties.append("El Paso")
print(counties)

counties_dict ={}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

counties_dict.items()

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

#user votes
my_votes = int(input("How many cotes did you get in the election? "))
#total votes
total_votes = int(input("What was the total votes in the election? "))
#calculate and print percentage
percent_vote = (my_votes / total_votes) *100
print("I recieved " + str(percent_vote) + "% of the total votes")