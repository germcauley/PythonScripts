'''Bulk delete messages or files from Slack
Makes use of slack cleaner repo: https://github.com/kfei/slack-cleaner
Uses python 3.5
Capabilities:
1:Delete messages from a given user,channel and date
2:Delete all files across all channels

Gerald McAuley 2017'''

import os
'''install slack-cleaner
NOTE: You may need to enter: 'sudo pip install slack-cleaner' in the terminal depending on your permissions
'''

installCommand = 'pip install slack-cleaner'
os.system(installCommand)


'''Define functions'''

#Delete Message
def deleteMessagesFromChannel(token,channel, user, date):
    #messages from the user(s) dating backwards from given date are displayed
    displayFilesToDelete=str('slack-cleaner'
    ' --token %s'
    ' --message'
    ' --channel %s'
    ' --user "%s" '
    ' --before %s'%(token,channel,user,date))
    os.system(displayFilesToDelete)

#User is asked to confirm message deletion or to cancel process
    print('Do you want to permanently delete these messages? y/n')
    confirm = input()

    # if user selects 'y' , messages are deleted
    if confirm == 'y':
        deleteAll =str('slack-cleaner'
                       ' --token %s'
                       ' --message'
                       ' --channel %s'
                       ' --user "%s" '
                       ' --before %s --perform'% (token, channel, user, date)
                       )
        os.system(deleteAll)
    else:
        print('Slack messages will not be deleted')

#Delete Files
def deleteFiles(user):
    #messages from the user(s) dating backwards from given date are displayed
    displayFilesToDelete=str('slack-cleaner'
    ' --token %s'
    ' --file'
    ' --user "%s" '%(token,user))
#--perform
    os.system(displayFilesToDelete)

#User is asked to confirm message deletion or to cancel process
    print('Do you want to permanently delete these files? y/n')
    confirm = input()

    # if user selects 'y' , messages are deleted
    if confirm == 'y':
        deleteAll =str('slack-cleaner'
        ' --token %s'
        ' --file'
        ' --user "%s" --perform'%(token,user))
        os.system(deleteAll)
    else:
        print('Slack files will not be deleted\n')


#Main program
ans ='y'
while ans == 'y':
    # ask for username
    print('\nPlease enter username/displayname(Case Sensitive)')  # can type '*' for all users
    user = input()

    print('Do you want to delete:\n1:Messages?\n2:files?')
    choice = int(input())

    # assign slack token to a variabe
    token = 'Place your api token here'
    
    # you need to get your own API token from:  https://api.slack.com/web


    #Remove messages or files depending on user choice
    if choice==1:
        # ask for date
        print('\nPlease enter a date in format: yyyymmdd (no dividers!)\n'
              'All slack messages before this date will be selected for deletion')
        date = input()
        # ask for channel to delete messages from
        print('\nPlease enter the name of the channel\n'
              'that you want to remove messages/files from (Case sensitive)')
        channel = input()
        deleteMessagesFromChannel(token,channel, user, date)
    else:
        deleteFiles(user)

    print('Run this program again?(y/n)')
    ans=str(input())

print('Goodbye!')
