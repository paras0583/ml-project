import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pandas

from sklearn.model_selection import train_test_split
from dataclass import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class Dataingestionconfig:
    train_data_path = os.path.join('artifacts','train_csv')
    test_data_path = os.path.join('artifacts','test_csv')
    raw_data_path = os.path.join('artifacts','raw_data')

class Dataingestion:
    def __init__(self):
        self.ingestion_config=Dataingestionconfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")

        try:
            df=pd.read_csv('C:\Users\Pallavi\OneDrive\Documents\machine learming project\notebook\data\stud.csv')
            logging.info("Readed the data from the notebook ")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split has been initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path , index=False , header=True)
            test_set.to_csv(self.ingestion_config.test_data_path , index=False , header=True)

            logging.info("Ingestion is done")

            return(self.ingestion_config.train_data_path , self.ingestion_config.test_data_path )

        except exception as e:
            raise customException(e,sys)

if __name__ = __main__:
    obj = Dataingestion()
    train_data , test_data = obj.initiate_data_ingestion()

    data_transformation = Datatransformation()
    train_arr,test_arr = data_transformation.initiate_data_transformation(train_data,test_data)
    model_trainer = Modeltrainer
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))


