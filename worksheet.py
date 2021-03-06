# -*- coding: UTF-8 -*-

import sys
import time
import datetime
import gspread
import traceback 
reload(sys)
sys.setdefaultencoding('utf-8')

class worksheet():

    def __init__(self):
        pass

    def updatecell(self,worksheet,title_list,traffic_list):

        try:
            # read and update worksheet (title)
            rowworksheet = worksheet.col_values(1)

            if(len(rowworksheet) <= 0):
                for title in title_list:
                    if(title == ""):
                        break
                    worksheet.insert_row([title],2)
                    time.sleep(2)
                worksheet.insert_row(['加總'],2)
            elif(len(title_list) != len(rowworksheet)-2):
                for i in range(len(title_list)-len(rowworksheet)+2):
                    worksheet.insert_row([title_list[len(rowworksheet)-2+i]],3)
                    time.sleep(2)
            

            # update traffic
            rowworksheet = worksheet.col_values(1)

            colworksheet = worksheet.row_values(len(worksheet.col_values(1)))

            for i in range(len(rowworksheet)):
                if(i == 0):                    
                    worksheet.add_cols(1)
                    worksheet.update_cell(i+1,len(colworksheet)+1,datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                    time.sleep(2)
                elif(i > 1):
                    worksheet.add_cols(1)
                    worksheet.update_cell(i+1,len(colworksheet)+1,traffic_list[len(traffic_list)-i+1])
                    time.sleep(2)
            worksheet.update_cell(2,len(colworksheet)+1,sum(traffic_list))
        
        except Exception as ex:
            traceback.print_exc()
            print(ex)