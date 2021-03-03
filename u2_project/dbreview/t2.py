import pickle,simplejson,json

i = int(1)
s = 'https://movie.douban.com/subject/26357307/reviews'
l = {'1': 'https://movie.douban.com/subject/26357307/reviews'}

m = pickle.dumps(l)
print(m, len(m))


