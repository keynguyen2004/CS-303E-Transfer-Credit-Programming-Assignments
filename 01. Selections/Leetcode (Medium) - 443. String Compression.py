"""
Leetcode Problem #: 443
Leetcode Problem: String Compression
Difficulty: Medium

To begin with, we want to keep track of the length of the current 
compressed string, which is also where the length of the current 
cluster of letters with the same characters. From there, we join 
the cluseter's letter with the string and write all of that after 
end of the compressed string

"""

class Solution:
    def compress(self, chars):
        count = 1
        if len(chars) == 1:
            return 1
        else:
            count = 1
            index = 0
            start_index = 0
            while index < len(chars) - 1:
                if chars[index] == chars[index + 1]:
                    count += 1
                    index += 1
                else:
                    if count == 1:
                        start_index += 1
                    elif 1 < count < 10:
                        chars[start_index + 1] = str(count)
                        del chars[start_index + 2:index+1]
                        start_index += 2
                    elif 10<=count<=99:
                        chars[start_index + 1] = str(count)[0]
                        chars[start_index + 2] = str(count)[1]
                        del chars[start_index + 3:index+1]
                        start_index += 3
                    elif 100 <= count <= 999:
                        chars[start_index + 1] = str(count)[0]
                        chars[start_index + 2] = str(count)[1]
                        chars[start_index + 3] = str(count)[2]
                        del chars[start_index + 4:index+1]
                        start_index += 4
                    else:
                        chars[start_index + 1] = str(count)[0]
                        chars[start_index + 2] = str(count)[1]
                        chars[start_index + 3] = str(count)[2]
                        chars[start_index + 4] = str(count)[3]
                        del chars[start_index + 5:index+1]
                        start_index += 4
                    index = start_index
                    count = 1
                
            if 1 < count < 10:
                chars[start_index + 1] = str(count)
                del chars[start_index + 2:index+1]
            elif 10<=count<=99:
                chars[start_index + 1] = str(count)[0]
                chars[start_index + 2] = str(count)[1]
                del chars[start_index + 3:index+1]
            elif 100 <= count <= 999:
                chars[start_index + 1] = str(count)[0]
                chars[start_index + 2] = str(count)[1]
                chars[start_index + 3] = str(count)[2]
                del chars[start_index + 4:index+1]
            elif count >= 1000:
                chars[start_index + 1] = str(count)[0]
                chars[start_index + 2] = str(count)[1]
                chars[start_index + 3] = str(count)[2]
                chars[start_index + 4] = str(count)[3]
                del chars[start_index + 5:index+1]

            return len(chars)



# As you can see, there's a lot of branching and selections. Therefore, 
# we should clean up our code so it's much neater and more readable       

class Solution:
    def compress(self, chars):

        n = len(chars)
        string, count = 0 

        for i in range(n):
            count += 1
            if chars[i] != chars[i + 1] or i == n - 1:
                if count <= 1:
                    chars[string] = chars[i]
                    string += 1
                else:
                    string = string + len(str(count))
                    count = list(chars[i] + str(count)) 
                    chars[string: string + len(str(count))] = count
                
                count = 0

        return string