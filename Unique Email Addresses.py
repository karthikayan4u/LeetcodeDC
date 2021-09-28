class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()
        for email in emails:
            local, host = email.split('@')
            processed_local = ''.join(ch for ch in local.split('+')[0] if ch != '.')
            uniques.add(processed_local + '@' + host)
        return len(uniques)
    
    Time - O(n*m)
    Space - O(|u|)
