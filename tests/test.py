import cmake_example as m
import cmake_example_sub as ms

assert m.__version__ == '0.0.1'
assert m.add(1, 2) == 3
assert m.subtract(1, 2) == -1
print(ms.add_sub(10,20))
