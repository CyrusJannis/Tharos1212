test_list = [('Cryomancer', 4), ('Wou', 6), ('randomuser', 5), ('VincentheGreat', 5), ('Cecilia', 6), ('Tomar', 1), ('Flockington', 4), ('Mqlons', 5), ('Strawberry', 7), ('Crimson', 5), ('Baller', 5), ('Swadee', 5), ('Al B', 5.5), ('Farmer Joe999', 4), ('laraaa', 6), ('lostee', 6), ('Frankthetank', 7), ('Hyper', 5), ('andy_ru12', 5.75), ('Universal', 7.25),]
N = 10
print("The original list is : " + str(test_list))
res = sorted(test_list, key = lambda x: x[1], reverse = True)[:N]
print("The top N records are : " + str(res))