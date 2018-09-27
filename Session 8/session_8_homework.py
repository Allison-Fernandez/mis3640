
a = ord('a') - 96
b = ord('b') - 96
c = ord('c') - 96
d = ord('d') - 96
e = ord('e') - 96
f = ord('f') - 96
g = ord('g') - 96
h = ord('h') - 96
i = ord('i') - 96
j = ord('j') - 96
k = ord('k') - 96
l = ord('l') - 96
m = ord('m') - 96
n = ord('n') - 96
o = ord('o') - 96
p = ord('p') - 96
q = ord('q') - 96
r = ord('r') - 96
s = ord('s') - 96
t = ord('t') - 96
u = ord('u') - 96
v = ord('v') - 96
w = ord('w') - 96
x = ord('x') - 96
y = ord('y') - 96
z = ord('z') - 96

bananas = [b,a,n,a,n,a,s]
sum_bananas = sum(bananas)

rice = [r,i,c,e]
sum_rice = sum(rice)

paprika = [p,a,p,r,i,k,a]
sum_paprika = sum(paprika)

potato_chips = [p,o,t,a,t,o,c,h,i,p,s]
sum_potato_chips = sum(potato_chips)

Total = sum_bananas + sum_rice + sum_paprika + sum_potato_chips
Total_nc = sum_bananas + sum_rice + sum_paprika

print('#1')
print()
print('bananas ${}'.format(sum_bananas))
print('rice ${}'.format(sum_rice))
print('paprika ${}'.format(sum_paprika))
print('potato chips ${}'.format(sum_potato_chips))
print('------------------------------')
print('Total ${}'.format(Total))

print()
print()
print('#2')
print()
print('bananas ${:>20.2f}'.format((sum_bananas)))
print('rice ${:>23.2f}'.format(sum_rice))
print('paprika ${:>20.2f}'.format(sum_paprika))
print('potato chips ${:>15.2f}'.format(sum_potato_chips))
print('------------------------------')
print('Total ${:>22.2f}'.format(Total))

print()
print()
print('#3')
print()
print('bananas ${:>20.2f}'.format((sum_bananas)))
print('rice ${:>23.2f}'.format(sum_rice))
print('paprika ${:>20.2f}'.format(sum_paprika))
print('------------------------------')
print('Total ${:>22.2f}'.format(Total_nc))