
"""
given n points calculate total number of circles that can be for by using any 3 points

Example:
    Input: n=5
    Output: 10
"""

n = int(input("Enter number of point: "))
ans = ((n-1)*(n-2)*n)//6
print("Total number of circle that can be formed = ", ans)
