import xlrd
import csv
from datetime import datetime

filename = "expense.xlsx"
csvfile = "data.csv"
sheetname="Sheet1"
book = xlrd.open_workbook(filename)
worksheet = book.sheet_by_name(sheetname)
csvfile = open(csvfile,'wb')
wr = csv.writer(csvfile,quoting= csv.QUOTE_NONE)
wr.writerow(worksheet.row_values(0))

for row in range(1,worksheet.nrows):
    date = worksheet.row_values(row)[4]

    if isinstance(date, float) or isinstance(date, int):
        year, month, day, hour, minute, sec = xlrd.xldate_as_tuple(date, book.datemode)
        py_date = "%02d/%02d/%04d" % (month, day, year)
        wr.writerow([py_date] + worksheet.row_values(row)[0:3])

csvfile.close()