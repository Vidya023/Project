import os
import sys
from nlp_files.exception import NLPException
from nlp_files.pipeline.training_pipeline import TrainPipeline

from nlp_files.constants import *


def training():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

    except Exception as e:
        raise NLPException(e, sys) from e


if __name__ == "__main__":
    training()


