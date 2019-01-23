import pandas as pd
import time

def get_index_of_string(table, str, type):
    for column in table:
      index = table[column][table[column] == str].index
      if index.size > 0 and index[0] > 1:
        return index[0] if type == "row" else column

def get_value_of_column(row_str, col_str):
  row = get_index_of_string(table, row_str, "row")
  col = get_index_of_string(table, col_str, "col")
  return table[col][row]

def get_promotor_shareholding(table):
  return get_value_of_column(
    "(A) Promoter & Promoter Group",
    "Shareholding as a % of total no. of shares (calculated as per SCRR, 1957)As a % of (A+B+C2)"
  )

def whether_warrant_issued(table):
  return get_value_of_column(
    "Whether the Listed Entity has issued any Warrants ?",
    "Yes/No"
  )

def whether_promotor_share_pledged(table):
  return get_value_of_column(
    "Whether any shares held by promoters are pledge or otherwise encumbered?",
    "Yes/No"
  )

scrip_code = 500302
for quarter in range(88, 101):
  url = "https://www.bseindia.com/corporates/shpSecurities.aspx?scripcd=%s&qtrid=%s" %(scrip_code, quarter)
  print(url)
  tables = pd.read_html(url)
  try:
    table = tables[0]
    print("======%s======" %(table[1][8]))
    if whether_warrant_issued(table) != "No": #Share warrants
      print("Share warrant issued")
    if whether_promotor_share_pledged(table) != "No":
      print("Promoter share pledged")
    print(get_promotor_shareholding(table)) #Promoter shareholding  %
    time.sleep(3)
  except:
    print("Error encountered while processing %s" %(url))