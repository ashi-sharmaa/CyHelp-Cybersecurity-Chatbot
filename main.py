#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breachbot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Facebook data breach!")
      
#Introduces breach
print("Would you like to learn about the Facebook data breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("\nThe 2019 Facebook data breach was caused by malicious actors who used the method of scraping to retrieve personal information, such as phone numbers, full names, locations, and email addresses, of 533 million Facebook users. They did this by utilizing a vulnerability in a pre-existing feature that allowed users to connect to each other by phone number, and then they later posted the data on an amateur hacking forum.")
  
  elif topic.lower() == "b":
    print("\nFollowing the data breach in August of that year, Facebook fixed the vulnerability and removed the connection-through-phone-number feature. They stated that they would not individually contact affected users, as the data was publicly accessible, and did not recommend any actions for the users since it was out of their hands.")
  
  elif topic.lower() == "c":
    break;
  
  else:
    print("\nSorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")
  
#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()

  if topic.lower() == "a":
    print("\nThe Facebook data breach impacts the confidentiality pillar of the CIA triad because it involved unauthorized access to and public availability of many pieces of personal information of 533 million users. This breach of confidentiality deals with data that was meant to be protected despite its public accessibility, allowing for dangerous misuse and exploitation.")

  elif topic.lower() == "b":
    print("\nI somewhat agree with Facebook’s response because the dataset that was compiled from inputted user info in the connect through phone number feature was susceptible to all sorts of security concerns if not checked for bugs, which in this case, a bug was present that gave access to imports of the data to malicious actors- Facebook made the right decision by shutting down that feature. On the other hand, while it is true that they couldn’t have recommended an action to users to relieve the breach’s consequences, the organization should have educated users about being cautious with inputting such sensitive types and amounts of personal information on an online platform. If a user is giving away so much personal info anywhere online, it is bound to be used against them when they unknowingly use a site that mishandles data.")

  elif topic.lower() == "c":
    print("I would convince victims to take action by deleting their sensitive personal information from their accounts if it is not permanently saved in Facebook’s datasets. My advice would be to more cautiously check on how the sites they use may access their data once inputted; I know that Facebook has a page asking the user to confirm their permission for the organization to use the data in any way they want, which most individuals skip over, much like any other site.")

  elif topic.lower() == "d":
    break;

  else:
    print("\nSorry, I didn't catch that. Choose one of the options listed.")

  input("\nPress enter to continue\n\n")


#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")