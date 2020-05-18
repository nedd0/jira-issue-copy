# jira-issue-copy

## Utility to clone JIRA issues from one project to another

Certifications like ISO or CMMI requiere that you have control over the issues your team works on, but for confidentiality or cost issues you can't add everyone to your client's JIRA. Also you may want to work internally and not disclose everything you discuss with your team to your client. 

In that context it is often needed to clone issues from their JIRA to yours. This utility allowes you to do that, moving descriptions, issue name (adding the client's key to it), attachments and comments to your JIRA. 

requirments

pip3 install JIRA. 

usage

python3 jira-issue-copy <client-issue-id> <your-jira-project-code> 

Example 

python3 jira-issue-copy XXX-123 YYY 

## DISCLAIMER
This is an utility that I created for my own use case. You are free to clone, modify and use under your own risk. 
