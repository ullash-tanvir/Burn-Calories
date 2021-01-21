from datetime import datetime
from os import listdir
from application_logging.logger import App_Logger
import pandas as pd


class dataTransform:


     def __init__(self):
          self.goodDataPath = "Training_Raw_files_validated/Good_Raw"
          self.logger = App_Logger()


     def addQuotesToStringValuesInColumn(self):
         

          log_file = open("Training_Logs/addQuotesToStringValuesInColumn.txt", 'a+')
          try:
               onlyfiles = [f for f in listdir(self.goodDataPath)]
               for file in onlyfiles:
                    data = pd.read_csv(self.goodDataPath+"/" + file)
                    #data = self.removeHyphenFromColumnNames(data)
                    # for col in data.columns:
                    #      # if col in column: # add quotes in string value
                    data['Id'] = data["Id"].apply(lambda x: "'" + str(x) + "'")
                    data['ActivityDate'] = data["ActivityDate"].apply(lambda x: "'" + str(x) + "'")
            
                   
                    data.to_csv(self.goodDataPath+ "/" + file, index=None, header=True)
                    self.logger.log(log_file," %s: Quotes added successfully!!" % file)
               
          except Exception as e:
               self.logger.log(log_file, "Data Transformation failed because:: %s" % e)
               log_file.close()
          log_file.close()

    
