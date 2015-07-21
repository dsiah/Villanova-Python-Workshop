class Solution:
		# @return a tuple, (index1, index2)
		def twoSum(self, num, target):
			sort_arr = sorted(num)
			i = 0
			j = len(sort_arr) - 1
			tried = sort_arr[i] + sort_arr[j]
			while (tried != target):
				if (tried > target):
					j -= 1
				else:
					i += 1

				tried = sort_arr[i] + sort_arr[j]

			part1 = num.index(sort_arr[i]) + 1
			num.reverse()
			part2 = len(num) - num.index(sort_arr[j])
			if part1 < part2:
				return (part1, part2)
			else 
				return (part2, part1)	
			

SolObj = Solution()
solution = SolObj.twoSum([0,4,3,0], 0)
#print solution