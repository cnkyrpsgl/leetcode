class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        rec = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            rec.add(local + '@' + domain)
        return len(rec)