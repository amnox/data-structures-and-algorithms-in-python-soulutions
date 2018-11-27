class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        pointer = numRows
        columns = []
        if len(s)<=2:
            return s
        while len(s)>=0:
            if (len(s) < 1):
                break
            if pointer == numRows:
                new_arr = []
                while pointer>0:
                    if (len(s) < 1):
                        break

                    s, result = s[1:], s[0]
                    new_arr.append(result)
                    pointer = pointer -1
                columns.append(new_arr)
                continue
            else:

                pointer+=1
                if (pointer + 1 >= numRows):
                    pointer = numRows
                    continue
                new_arr = [0]*numRows
                s, result = s[1:], s[0]
                new_arr[numRows-pointer-1] = result
                columns.append(new_arr)

                continue
        string = ''

        if len(columns)<2:
            return "".join(columns[0])
        for i in range(0,len(columns[0])):

            for j in columns:
                if i>len(j)-1:
                    continue
                if j[i] == 0:
                    continue
                string += j[i]

        return string

print(Solution().convert('ABCDE',4)[::])