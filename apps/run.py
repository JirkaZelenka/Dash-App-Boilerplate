import pandas as pd
from typing import Optional
import os
import json
from tqdm import tqdm

from config import Config
from db_managment.data_manager import DataManager
from utils.logger import Logger
from utils.mailing import Mailing
from utils.utils import Utils

class Runner:
    
    def __init__(self) -> None: 
        self.cf = Config()   
        self.data_manager = DataManager()
        self.logger = Logger()
        self.mailing = Mailing()
        self.utils = Utils()
  
        
    def first_function(self) -> None:
        
        print("Hello World")
        return