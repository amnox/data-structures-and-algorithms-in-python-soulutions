class Solution:

    def find_and_replace_pattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def generate_substr(word):
            gener=[]
            total = len(word)
            for i, w in enumerate(word):
                if w in word[:i]:
                    if word[i-1] == w:
                        total = total - 2
                    else:
                        total = total - 1
                gener.append(total)
            return gener

        def most_occured(word):
            words=list(set([w for w in word if word.count(w)>1]))
            occurences=[]
            for w in words:
                occurences.extend(i for i,x in enumerate(word) if x==w)
            return sorted(occurences)

        pattern_code = generate_substr(pattern)
        matches = []
        for word in words:
            if pattern_code == generate_substr(word):
                matches.append(word)
        filtered=[]
        pattern_seq = most_occured(pattern)
        for match in matches:
            if pattern_seq == most_occured(match):
                filtered.append(match)

        return filtered


a = Solution()
print(a.find_and_replace_pattern(["ktittgzawn","dgphvfjniv","gceqobzmis","alrztxdlah","jijuevoioe","mawiizpkub","onwpmnujos","zszkptjgzj","zwfvzhrucv","isyaphcszn"], "zdqmjnczma"))
#[10, 10, 10, 10, 10, 10, 10, 9, 8, 8]
#[10, 10, 10, 10, 10, 10, 10, 9, 8, 8]

#alrztxdlah
#zdqmjnczma