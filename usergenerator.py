import requests
import random
import sys

iterations = int(sys.argv[1])

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
username_site = "https://raw.githubusercontent.com/maryrosecook/commonusernames/master/usernames.txt"

username_response = requests.get(username_site)
userList = username_response.text.splitlines()

response = requests.get(word_site)
wordList = response.text.splitlines()

outputFile = open('sqlstatement.sql', 'w')

# Remove words less than four characters long
largewords = list(filter(lambda x: len(x) > 4, wordList))
largeusers = list(filter(lambda x: len(x) > 4, userList))

sqlList = list()

# generate a random combination of words and usernames.
for i in range(iterations):
    username = random.choice(largeusers)
    password = random.choice(largewords)
    email = username + str(random.randrange(1000)) + "@gmail.com"
    result = "('" + username + "', '" + email + "', '" + password + "');"
    sqlList.append(result)


# output valid sql to a file
for item in sqlList:
    constSql = "INSERT INTO users (username, email, password) VALUES "
    outputFile.writelines(constSql + item + "\n")
