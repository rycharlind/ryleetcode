import sys

a = [1, 2, 3]  # reference count for list object is 1
print(f"Memory used by integer a: {sys.getsizeof(a)} bytes")
b = a          # reference count for list object is 2
print(f"Memory used by integer a: {sys.getsizeof(a)} bytes")
del a          # reference count for list object is 1
print(f"Memory used by integer a: {sys.getsizeof(b)} bytes")
del b          # reference count for list object is 0, memory is deallocated