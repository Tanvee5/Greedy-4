# Problem 2 : Minimum Domino Rotations For Equal Row
# Time Complexity : 
'''
Using hashMap - O(n) where n is the length of the tops or bottom arrays
'''
# Space Complexity : 
'''
Using hashMap - O(n) where n is the length of the tops or bottom arrays
'''
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

# Using hashMap
from typing import List
from collections import defaultdict
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # define the map that will store number on domino as key and its frequency as value
        map = defaultdict(int)
        # define target variable and set to 1 initially
        target = 1

        # loop from 0 to length of tops array
        for i in range(len(tops)):
            # get the element at ith position of top array
            top = tops[i]
            # increment the value for the top key in the map
            map[top] += 1
            # if the value of the top key is greater or equal to length of the top array then that element is the target and break
            if map[top] >= len(tops):
                target = top
                break
            # get the element at ith position of bottom array
            bottom = bottoms[i]
            # increment the value for the bottom key in the map
            map[bottom] += 1
            # if the value of the bottom key is greater or equal to length of the top array then that element is the target and break
            if map[bottom] >= len(tops):
                target = bottom
                break
        # define aRot and bRot variable and set to 0. These variables will store the number of rotation for top and bottom respectively 
        aRot = 0
        bRot = 0
        # loop from 0 to length of top array
        for i in range(len(tops)):
            # get the elememt at ith position of top array
            top = tops[i]
            # get the elememt at ith position of bottom array
            bottom = bottoms[i]
            # check if the top and bottom are not equal to target and if it is then return -1
            if top != target and bottom != target:
                return -1
            # check if top is not equal to target. If it is then increment the value aRot (number of rotation for top)
            if top != target:
                aRot += 1
            # check if bottom is not equal to target. If it is then increment the value bRot (number of rotation for bottom)
            if bottom != target:
                bRot += 1
        # return the minimum value between aRot and bRot
        return min(aRot, bRot)

# 2nd Method
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # check function to get the minimum number of rotation for the target 
        def check(tops: List[int], bottoms: List[int], target: int) -> int:
            # define aRot and bRot variable and set to 0. These variables will store the number of rotation for top and bottom respectively
            aRot = 0
            bRot = 0
            # loop through tops and bottoms array
            for top, bottom in zip(tops, bottoms):
                # check if the top and bottom are not equal to target and if it is then return -1
                if top != target and bottom != target:
                    return -1
                # check if top is not equal to target. If it is then increment the value aRot (number of rotation for top)
                if top != target:
                    aRot += 1
                # check if bottom is not equal to target. If it is then increment the value bRot (number of rotation for bottom)
                if bottom != target:
                    bRot += 1
            # return the minimum value between aRot and bRot
            return min(aRot, bRot)
        # get the 0th element from the tops array in the a
        a = tops[0]
        # get the number of rotation for the target a 
        result = check(tops, bottoms, a)
        # if the result is -1 then return result
        if result != -1:
            return result
        # now consider the element at 0th position of the bottom array
        b = bottoms[0]
        # get the number of rotation for the target b and return that result
        return check(tops, bottoms, b)
