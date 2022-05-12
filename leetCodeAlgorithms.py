class leetCodeAlgorithms:
    #code explains as it does each step

#this is a test


    # #twosum

    def twoSum(nums: list[int], target: int) -> list[int]:
        print(' ')
        print('target number to sum to = {}'.format(target))
        # List to store results
        result = []
        # Dictionary to store the difference and its index
        index_map = {}
        print('-'*30)
        # Loop for each element
        for indexNum, num in enumerate(nums):
            # Difference which needs to be checked
            print('index Number = ' + str(indexNum))
            print('number Value = ' + str(num))
            difference = target - num
            print("calculating difference using: {} - {}".format(target,num))
            print(f"looking for [ {difference} ] in index map")
            print('indexmap: '+ str(index_map))
            print('-'*30)
            if difference in index_map:
                print("Found tuple that sums to {}".format(target))
                result.append(indexNum)
                print("appended index = {} into the result".format(indexNum))
                result.append(index_map[difference])
                print('appended index_map[{}] = {} into result'.format(difference,index_map[difference]))
                break
            else:
                index_map[num] = indexNum
        print (result)
        
# def twoSum(nums: List[int], target: int) -> List[int]:
#     # List to store results
#     result = []
#     # Dictionary to store the difference and its index
#     index_map = {}
#     # Loop for each element
#     for i, n in enumerate(nums):
#         # Difference which needs to be checked
#         difference = target - n
#         if difference in index_map:
#             result.append(i)
#             result.append(index_map[difference])
#             break
#         else:
#             index_map[n] = i
#     return result


    def romanToInt(s:str)->int:
        #dicationary with values to string
        roman_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        #length of given string
        n = len(s)
        #stores result
        answer = roman_map[s[n-1]] #needs the -1 because index starts at 0, so youd need to account for it, example 'FOUR' length is 4 but starts counting from 0 so it would actually be 0=F,1=O,2=U,3=R
        print("")
        print('-'*30)
        print('convert this roman numeral string: ' + s)
        print('-'*30)
        print('current answer = ' + str(answer))

        for i in range(n-2,-1,-1): #start at n-2, because you have value of last number already from up above, end at -1 index(null), step back -1 every time
            if roman_map[s[i]] >= roman_map[s[i+1]]:
                print('if loop which compares {} >= {}'.format(roman_map[s[i]],roman_map[s[i+1]]))
                print('value of s[i]} = ' + str(roman_map[s[i]]))
                print('value of s[i+1] = ' + str(roman_map[s[i+1]]))
                print('did calculation {} + {}'.format(answer,roman_map[s[i]])) 
                answer += roman_map[s[i]] #if current number >=, add total + value of current
                print('new result is = '  + str(answer))
                print('-'*30)
            else: #value is less than 
                print('else loop which compares {} < {}'.format(roman_map[s[i]],roman_map[s[i+1]]))
                print('did calculation {} - {}'.format(answer,roman_map[s[i]]))
                answer -= roman_map[s[i]] #if less, subtract
                print('new result is = '  + str(answer))
                print('-'*30)
        # return answer
        print('{} = {}'.format(s,answer))
        print('-'*30)

# def romanToInt(s: str) -> int:
#     # Dictionary of roman numerals
#     roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     # Length of the given string
#     n = len(s)
#     # This variable will store result
#     num = roman_map[s[n - 1]]
#     # Loop for each character from right to left
#     for i in range(n - 2, -1, -1):
#         # Check if the character at right of current character is bigger or smaller
#         if roman_map[s[i]] >= roman_map[s[i + 1]]:
#             num += roman_map[s[i]]
#         else:
#             num -= roman_map[s[i]]
#     return num        
