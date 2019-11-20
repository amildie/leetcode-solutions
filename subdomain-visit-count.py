# https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def extractDomains(self, domains: List[str]) -> List[str]:
        res = []
        domains = reversed(domains.split('.'))
        
        acc = ""     
        for d in domains:
            if acc == "":
                acc = d + acc
            else:
                acc = d + "." + acc
            res.append(acc)

        return res
  
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hits = {}
        for cpd in cpdomains:
            tmp = cpd.split(' ')
            numVisits = tmp[0]
            
            domains = self.extractDomains(tmp[1])            
            for d in domains:
                if d in hits:
                    hits[d] += int(numVisits)
                else:
                    hits[d] = int(numVisits)
                    
        res = []
        for k, v in hits.items():
            res.append(str(v) + " " + str(k))
        return res
