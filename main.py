import pandas as pd
import datetime
import smtplib

#Enter your Authentication Details
user = 'rishatestingpython@yahoo.com'
passid = 'pythoncodetsting'

def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}")
    s = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    s.starttls()
    s.login(user, passid)

    s.sendmail(user, to, f"Subject: {sub}\n\n{msg}")
    s.quit()

if __name__ == "__main__":
    sendEmail(user, "subject", "test message")
    exit()

    df = pd.read_excel("birthday.xlsx")
    #print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    #print(today)
    writeInd = []
    for index , item in df.iterrows():
        #print(index, item['Birthdate'])
        bday = item['Birthdate'].strftime("%d-%m")
        #print(bday)
    
        if(today == bday) and yearNow not in str(item['Year']):
            #sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
            sendEmail(GMAIL_ID, "Happy Birthday", item['Dialogue'])
            writeInd.append(index)

    #print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ',' + str(yearNow)
        #print(df.loc[i, 'Year'])

    #print(df)
    df.to_excel('birthday.xlsx', index = False)
            

