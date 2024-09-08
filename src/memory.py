import sys

a = 10
b = [1, 2, 3]
c = "Hello"

print(f"Memory used by integer a: {sys.getsizeof(a)} bytes")
print(f"Memory used by list b: {sys.getsizeof(b)} bytes")
print(f"Memory used by string c: {sys.getsizeof(c)} bytes")
