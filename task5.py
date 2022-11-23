list = ['2018-01-01', 'yandex', 'cpc', 100]
last = list.pop()
for i in reversed(list):
  last = {i: last}
  print(last)