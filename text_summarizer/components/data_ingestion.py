import os
from pathlib import Path
import urllib.request as request
import py7zr
from text_summarizer.entity import DataIngestionConfig
from text_summarizer.logger import logger
from text_summarizer.utils import get_size

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        fname = None
        header = None
        if not os.path.exists(self.config.local_data_file):
            # with request.urlretrieve(
            #     url=self.config.source_url,
            #     filename=self.config.local_data_file
            # ) as res:
            #     fname, header = res
            #     logger.info(f"{fname} downloaded with the following info {header}")
        
            with request.urlopen(self.config.source_url) as response:
                file_size = int(response.headers.get('Content-Length', 0))
                if file_size == 0:
                    raise ValueError("Content-Length header not found. Unable to determine file size.")
                with open(self.config.local_data_file, 'wb') as out_file:
                    out_file.write(response.read())
                logger.info(f"{fname} downloaded with the following info {header}")
                logger.info(f"Size of the downloaded file {get_size(Path(self.config.local_data_file))}")
        else:
            logger.info(f"{fname} of size {get_size(Path(self.config.local_data_file))} already exists!")
    
    def extract_zip(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with py7zr.SevenZipFile(self.config.local_data_file, 'r') as archive:
            archive.extractall(path=unzip_path)
        # with zipfile.ZipFile(self.config.local_data_file, 'r') as ref:
        #     ref.extractall(unzip_path)