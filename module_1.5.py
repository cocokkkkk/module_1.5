immutable_var = 1, 2, 'a', 'b'
print(immutable_var)
#immutable_var [0] = 2
#print(immutable_var) В этом заключается оссобеность и отличие кортежа от списка, его элементы нельзя изменить.
mutable_lis = [1, 2, "a", "b"]
mutable_lis[1] = '10'
mutable_lis.append("c")
mutable_lis.extend('Привет')
print(mutable_lis)