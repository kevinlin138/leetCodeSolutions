from leetCodeAlgorithms import leetCodeAlgorithms

List1 = [1,3,5,8,20,4,9,15,32]
targetNum = int(18)
romanNum0 = "MCMXCIV"
romanNum1 = 'LVIII'

def main():
    leetCodeAlgorithms.twoSum(List1,targetNum)
    leetCodeAlgorithms.romanToInt(romanNum0)
    leetCodeAlgorithms.romanToInt(romanNum1)

if __name__ == '__main__':
    main()

