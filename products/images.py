# from os import listdir
import os
# from os.path import isfile, join

categories = [{'name': 'makirikiri', 'count': 22}, {
    'name': 'shanga', 'count': 13}, {'name': 'plain', 'count': 36}]
images_dir = 'D:\\MyProjects\\Customers\\Zani\\Images'
onlyfiles = [f for f in os.listdir(
    images_dir) if os.path.isfile(os.path.join(images_dir, f))]
# print(sum([x['count'] for x in categories]))
# print(len(onlyfiles))
# for f in onlyfiles:
#     print(f)
pointer = 0
counter = 0
for cat in categories:
    prev = pointer
    pointer += cat['count']
    # print(pointer)
    lst = onlyfiles[prev:pointer]
    # print(len(lst))
    name = cat['name']
    for f in lst:
        counter += 1
        fn = f'{counter:02}-{name}.jpeg'
        os.rename(os.path.join(images_dir, f), os.path.join(images_dir, fn))
        print(fn)
