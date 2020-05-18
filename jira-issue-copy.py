from jira import JIRA
import sys



user = 'john.doe@something.com'
apikey = 'YOUR JIRA API KEY'
own_jira_server = 'https://yourJIRA.atlassian.net/'
client_jira_server = 'https://yourClientsJIRA.atlassian.net/'

options_own_jira = {
 'server': own_jira_server
}

options_client_jira = {
 'server': client_jira_server
}

own_jira = JIRA(options_own_jira, basic_auth=(user,apikey) )
client_jira = JIRA(options_client_jira, basic_auth=(user,apikey) )

def copy_issue(issue_code, own_project_key):
    original_issue = client_jira.issue(issue_code)
    
    new_issue = own_jira.create_issue(project=own_project_key,
        summary='['+original_issue.key+'] ' + original_issue.fields.summary, 
        description=original_issue.fields.description,
        issuetype={'name': 'Bug'})
    
    for attachment in original_issue.fields.attachment:
        own_jira.add_attachment(issue=new_issue, attachment=attachment.get(), filename=attachment.filename)

    for comment in original_issue.fields.comment.comments:
        own_jira.add_comment(new_issue, comment.body)

    print(new_issue.key)

if len(sys.argv)<3:
    print('There are missing parameters.')
    print('Usage: python3 jira-issue-cop.py [Client issue code] [Own project key]')
    sys.exit()

issue_code = sys.argv[1]
own_project_key = sys.argv[2]

#?> python3 jira-issue-copy.py [Client issue code] [Own project key]
#?> python3 jira-issue-copy.py SSS-914 COM
copy_issue(issue_code,own_project_key)
