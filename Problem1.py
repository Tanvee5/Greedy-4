# Problem 1 : Shortest Way to Form String
# Time Complexity : 
'''
1st Approach - O(m*n) where m is the length of the source and n is the length of the target
Binary Search - O(t log s) where t is the length of the target and s is the length of the source
'''
# Space Complexity : 
'''
1st Approach - O(1)
Binary Search - O(s) where s is the length of the source
'''
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
# 1st Approach
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # define a hashset and add the characters for the souurce in the set 
        sourceSet = set(source)
        # get the length of the source and target
        sl = len(source)
        tl = len(target)
        
        # check if each character of target was not in the hash set and if character is not present in the set then return -1
        for c in target:
            if c not in sourceSet:
                return -1
        
        # define the count variable to count the subsequence and set to 1
        count = 1
        # define pointers for source and target and set to 0
        sp = 0
        tp = 0
        
        # loop till tp is less than the length of the target
        while tp < tl:
            # check if sp is equal to length of source and if it is then set the sp to 0 and increment the value of count
            if sp == sl:
                sp = 0 
                count += 1
            # check if the character at sp position of source and character at tp position of target
            if source[sp] == target[tp]:
                # if it is then increment the value of tp
                tp += 1
            # increment the value of sp
            sp += 1
        # return the value of count
        return count
    
# Binary Search 
from collections import defaultdict
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # define the dictionary which will store the key as character of the source and values will be list of indices of the characters
        charIndices = defaultdict(list)
        # loop through source string
        for i, c in enumerate(source):
            # add the index of the character c to the list to key c in the map.
            charIndices[c].append(i)
        # define the count variable to count the subsequence and set to 1
        count = 1
        # define pointers for source and target and set to 0
        sp = 0
        tp = 0
        # get the length of the source string
        sl = len(source)
        # loop till tp is less than the length of the target
        while tp < len(target):
            # get the character at tp position in the target
            tChar = target[tp]
            # check if the character of the target is not in the hashmap
            if tChar not in charIndices:
                # if the character is not there then return -1
                return -1
            # check if sp is equal to length of source and if it is then set the sp to 0 and increment the value of count
            if sp == sl:
                count += 1
                sp = 0
            # get the character at sp position of source
            sChar = source[sp]
            # check if the character of source is not equal to character of target
            if sChar != tChar:
                # get the list of index for the character of target 
                indices = charIndices[tChar]
                # call the binary search on the list of the index and sp value and get the index 
                bsIndex = self.binarySearch(indices, sp)
                # check if the index is equal to length of the list 
                if bsIndex == len(indices):
                    # if it is then set the sp to 0th position in the list and increment the count
                    sp = indices[0]
                    count += 1
                else:
                    # else set the sp to index position in the list 
                    sp = indices[bsIndex]
            # increment the value of tp and sp
            tp += 1
            sp += 1
        # return count   
        return count
    
    # binary Serach function
    def binarySearch(self, indices, target: int) -> int:
        # define low and high and set the values to 0 and length of indices - 1 respectively
        low = 0
        high = len(indices) - 1
        # loop till low <= high
        while low <= high:
            # get the middle value
            mid = low + (high - low) // 2
            # check if the value at mid position of indices is less than the target then set the low to mid + 1
            if indices[mid] < target:
                low = mid + 1
            else:
                # else set the high to mid - 1
                high = mid - 1
        # return the low value
        return low
