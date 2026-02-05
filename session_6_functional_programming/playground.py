# class MyIter :
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):  # 1 to 20
#         if self.start < self.end :
#             val = self.start
#             self.start += 1
#             return val
#         else:
#             raise StopIteration
#
# itr = MyIter(1,20)
#
# for i in itr :
#     print(i)
#



def my_iter_gen(start, end):
    for i in range(start, end):
        yield i

itr = my_iter_gen(1, 21)

for i in itr :
    print(i)
