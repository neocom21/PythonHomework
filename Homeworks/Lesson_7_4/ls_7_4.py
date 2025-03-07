def common_elements():

	set1 = set(range(0,100, 3))

	set2 = set(range(0, 100, 5))

	return set1 & set2



assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

