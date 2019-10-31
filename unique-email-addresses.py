# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def clean(self, email: str) -> str:
        splitEmail = email.split('@')
        lName = splitEmail[0]
        dName = splitEmail[1]
        lName = lName.replace('.', '')
        if '+' in lName:
            lName = lName.split('+')[0]
        return lName + '@' + dName

    def numUniqueEmails(self, emails: List[str]) -> int:
        emails = set(map(self.clean, emails))
        return len(emails)

