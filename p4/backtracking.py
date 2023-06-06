# Python3 program to find all combinations that
# sum to a given value

def combinationSum(arr, sum):
	ans = []
	temp = []

	# first do hashing nothing but set{}
	# since set does not always sort
	# removing the duplicates using Set and
	# Sorting the List
	arr = sorted(list(set(arr)))
	findNumbers(ans, arr, temp, sum, 0)
	return ans

def findNumbers(ans, arr, temp, sum, index):
	
	if(sum == 0):
		
		# Adding deep copy of list to ans
		ans.append(list(temp))
		return
	
	# Iterate from index to len(arr) - 1
	for i in range(index, len(arr)):

		# checking that sum does not become negative
		if(sum - arr[i]) >= 0:

			# adding element which can contribute to
			# sum
			temp.append(arr[i])
			findNumbers(ans, arr, temp, sum-arr[i], i)

			# removing element from list (backtracking)
			temp.remove(arr[i])


# Driver Code
arr =[3, 5 ,6 ,10]
sum = 15
ans = combinationSum(arr, sum)
#test case 2
arr2 =[2,5,7]
sum2 = 11
ans2 = combinationSum(arr2, sum2)
# If result is empty, then
if len(ans) <= 0:
	print("empty")
	
# print all combinations stored in ans
for i in range(len(ans)):

	print( end=' ')
	for j in range(len(ans[i])):
		print(str(ans[i][j])+" ", end=' ')
	print('\n', end=' ')
print("----------------")
# If result is empty, then
if len(ans2) <= 0:
	print("empty")
	
# print all combinations stored in ans
for i in range(len(ans2)):

	print( end=' ')
	for j in range(len(ans2[i])):
		print(str(ans2[i][j])+" ", end=' ')
	print('\n', end=' ')

