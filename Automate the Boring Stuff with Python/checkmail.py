# 3rd party modules

import imapclient, pyzmail
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('email', 'password')#app password
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['SINCE 20-Aug-2020'])
rawMessage = conn.fetch([messageID], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessage[messageID][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.text_part #was the format text
mesage.html_part #was the format html
message.text_part.get_payload().decode('UTF_8')


conn.logout()
