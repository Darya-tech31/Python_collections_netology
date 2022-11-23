queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

dis = {}
for queries_qnty in queries:
  total_len = queries_qnty.split()
  if len(total_len) in dis.keys():
    dis[len(total_len)] += 1
  else:
    dis[len(total_len)] = 1
for key, value in dis.items():
  percent = round((value / len(queries)) * 100, 2)
  print(f'Поисковых запросов из {key} слова: {percent}%')
