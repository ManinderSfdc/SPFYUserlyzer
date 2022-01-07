strUsername = 'ENTER SALESFORCE USERNAME'
strPassword = 'ENTER SALESFORCE PASSWORD'
strToken = 'ENTER SALESFORCE USER SECURITY TOKEN'

# for sandboxes set strdomain = 'test' amd for production set it to blank strdomain = ''
strdomain = 'test' 

# the salesforce org url for example 'https://saproduction--mani.lightning.force.com'
orgURL = 'ENTER SALESFORCE ORG URL'

# MODIFY THE SOQL QUERY WHERE CLAUSE TO FILTER THE USERS FOR WHOM THE DATA STORAGE METRIC IS REQUIRED
query = "SELECT Id FROM User WHERE Profile.UserLicense.Name = 'Salesforce' AND IsActive = TRUE"

# MODIFY WITH THE PATH WHERE chromedriver EXECUTABLE FILE IS SAVED
chromeDriverPath = '/usr/local/bin/chromedriver'

