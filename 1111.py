def remove_element(nums:list,val:int)->int:
    j:int=0
    newnums=list()
    while j<len(nums):
        if nums[j]!=val:
            newnums.append(nums[j])
        j+=1
    nums[:] = newnums
    return len(nums)
    #nums[:] = [item for item in nums if item != val]
    #return len(nums)
nums = [1,2,2,3,0,4,2]
print(remove_element(nums,2),nums)
print(nums) 
def is_valid_word(word:str, tiles:str)->bool:
    for i in range(len(word)):
        if word[i] in tiles:
            tiles=tiles.replace(word[i],'',1)
            continue
        else:
            return False
            break
        
    return True
print(is_valid_word('ART','TKABR'))
print(is_valid_word('HUE','TKABR'))
print(is_valid_word('NCCU','TKABCRNUC'))

def count_bits(n:int)->int:
    return bin(n).count('1')
print(count_bits(5))
print(count_bits(15))
print(count_bits(500000010213123123))

n=10
x=0
for i in range(1,n+1):
    k=i+1
    while k<=n:
        x=x+1
        k+=1
print(x)


class Test:
    def __init__(self, w):
      self.word = w
    def __len__(self):
      return len(self.word)
    def __str__(self):
      return f"Hello, {self.word}!"
    def __iter__(self):
      for c in self.word:
        yield c

ABC = Test('abc')
print(ABC.__str__())
print(ABC.__len__())
print(ABC.__iter__())

an_integer=123
print(an_integer)

digit_string = str(an_integer)



digit_map = map(int, digit_string)



digit_list = list(digit_map)

    if '{:032b}'.format(x)=='1000000000000000000000000000000000'or len('{:032b}'.format(x))>33:
        return 0
    else:
        return x
print(digit_list)
