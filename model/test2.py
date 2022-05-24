from ddstable import ddstable



b = "N:QJT5432.T.6.QJ82 .J97543.K7532.94 87.A62.QJT4.AT75 AK96.KQ8.A98.K63".encode()

def print_dds(PBN) :
  all = ddstable.get_ddstable(PBN)

  print("{:>5} {:>5} {:>5} {:>5} {:>5} {:>5}".format("", "S", "H", "D", "C", "NT"))
  # may use  card_suit=["C", "D", "H", "S", "NT"]
  for each in all.keys():
    print("{:>5}".format(each),end='')
    for suit in ddstable.dcardSuit:
        trick=all[each][suit]
        if trick>7:
            print(" {:5}".format(trick - 6),end='')
        else:
            print(" {:>5}".format("-"),end='')
    print("")



print_dds(b)