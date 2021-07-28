import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('jlundholm@uinta1.com', 'password')  #app password need for google
conn.sendmail('from', 'ro', 'Subject: so long...\n\nDear Jared,\nSo long and thanks for all the fish.\n\nJared')
conn.quit()
