import heapq
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if (len(height) == 2):
            return min(height[0], height[1])

        i = 0
        j = len(height)-1
        max_vol = (j-i)*(min(height[i],height[j]))
        second_largest = height.index(min(heapq.nlargest(2, height)))
        largest = height.index(max(height))
        contendor = abs(second_largest-largest)*min(height[second_largest],height[largest])
        print (contendor)
        max_vol = max(contendor,max_vol)
        while True:
            if i==j or max(i,j)>=len(height):
                max_vol = max(max_vol,min(height[i],height[j]))
                break
            try:
                l_vol = (j - i - 1) * min(height[j - 1], height[i])
                r_vol = (j - i - 1) * min(height[i + 1], height[j])
            except:
                break

            print(i,j,max_vol)

            if l_vol > r_vol:
                max_vol = max(l_vol,max_vol)
                j -= 1
                continue
            elif l_vol < r_vol:
                max_vol = max(max_vol, r_vol)
                i+=1
                continue
            elif l_vol == r_vol:
                max_vol = max(max_vol, l_vol)
                i += 1
                j -= 1
                continue

        print(max_vol)

Solution().maxArea([76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191])