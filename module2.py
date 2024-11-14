#Функция вывода красивого блока текста для 2.2
def sort_brand_export(dict, source):
      for i in range(len(dict[source])):
            try:
                  print(dict[source][i][0] , dict[source][i][1],
                  dict[source][i][2] , dict[source][i][3],
                  dict[source][i][4] , dict[source][i][5],
                  dict[source][i][6] , dict[source][i][7])
            except:
                  print("None")

def nice_export(list):
     print(list[0], list[1],
           list[2], list[3],
           list[4], list[5],
           list[6], list[7]
           )
    