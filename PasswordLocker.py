#! python3
#PasswordLocker.py - A Simple password locker program to store complex passwords
import pyperclip

x =1
#store account and passwords
PASSWORDS ={'email':'asdfgh45645645623424234',
            'blog':'dfgerfgf34553df55',
            'site':'tttt464565464',
            'bank_account':'009988uijkhuyi!!!4544567234d'}

#promt user to type the account they need password for
print('Please type the name of the account you need a password for:')

for key in PASSWORDS:
    print(key)
    x += 1

account = input()

#copy the password for the user input account to clipboard or else throw error
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named' + account)


'''Additional functionality to add in future:
-Prompt user to enter new accunt and password and add to directory
-change password with old passwword confirmation
-allow user to select accout by typing number '''
