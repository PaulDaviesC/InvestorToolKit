import pandas as pd
import time

def whether_warrant_issued(table):
  return table[table[0] == "Whether the Listed Entity has issued any Warrants ?"][1].values[0]

def whether_promotor_share_pledged(table):
  return table[table[0] == "Whether any shares held by promoters are pledge or otherwise encumbered?"][1].values[0]

scrip_code = 533200
for quarter in range(88, 101):
  url = "https://www.bseindia.com/corporates/shpSecurities.aspx?scripcd=%s&qtrid=%s" %(scrip_code, quarter)
  print(url)
  tables = pd.read_html(url, attrs = {'border': '0', 'width': '100%', 'align': 'center', 'cellspacing': '1', 'cellpadding': '4'})
  try:
    print("======%s======" %(tables[0][1][1]))

    sh_activity = tables[1]
    if whether_warrant_issued(sh_activity) != "No": #Share warrants
      print("Share warrant issued")

    if whether_promotor_share_pledged(tables[1]) != "No":
      print("Promoter share pledged")

    sh_details = tables[2]
    print(sh_details[sh_details[0] == "(A) Promoter & Promoter Group"][4].values[0]) #Promoter shareholding  %
    time.sleep(3)
  except:
    print("Error encountered while processing %s" %(url))