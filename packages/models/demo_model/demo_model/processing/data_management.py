"""Funcitons for local data management.
"""
import typing as t
import logging
import os
import joblib

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from demo_model import pipeline
from demo_model.config import config
from demo_model import __version__ as _version

_logger = logging.getLogger(__name__)

def create_regression_demo_data(*, mode='production', n_samples=100,
                                file_name=config.DATA_FILE) -> None:
    """
    Create data for regression demo. Supported modes are 'testing' 
    (for testing purposes) and 'production' (for all other data).
    """
    # Generate n_samples
    ## Features, (x1, x2)_{j}, sampled from ~ N(j,10)xN(j,20)
    X = (np.array([[j + 10*(i+1)*np.random.randn() 
                    for i in range(0, 2)] for j in range(0, n_samples)]))

    ## Targets, y_j, sampled from ~N(3j+30,1)
    y = np.array([3*j + np.random.randn() + 30 for j in range(0, n_samples)])

    # Store data as a dictionary
    data_dict = ({config.FEATURES[0]: X[:,0], config.FEATURES[1]: X[:,1], 
                  config.TARGET: y})
    # Convert to data frame
    data = pd.DataFrame(data=data_dict)

    # Specify dataset directory
    if mode == 'production':
        dataset_dir = config.DATASET_DIR
    elif mode == 'testing' :
        dataset_dir = config.DATASET_TESTING_DIR
    else:
        raise ValueError('Value not supported for "mode" in load_dataset.')

    data.to_csv(f'{dataset_dir}/{file_name}', index=False)

def load_dataset(*, mode='production', file_name: str) -> pd.DataFrame:
    """
    Load the specified dataset. Supported modes are 'testing' 
    (for testing purposes) and 'production' (for all other data).
    """
    # Choose were you will load the data from
    if mode == 'production':
        _data = pd.read_csv(f'{config.DATASET_DIR}/{file_name}')
    elif mode == 'testing':
        _data = pd.read_csv(f'{config.DATASET_TESTING_DIR}/{file_name}')
    else:
        raise ValueError('Value not supported for "mode" in load_dataset.')
    return _data

def make_splits(*, file_name=config.DATA_FILE, mode='production', 
                split_type='train_test', test_size=0.2, 
                dev_size=0.2, random_state=3) -> None:
    """
    Make train and dev set splits. Supported modes are 'testing' (for testing purposes) 
    and 'production' (for all other data). Supported split types are 'train_dev' and, 
    the default, 'train_test.' Note dev_size is defined as a fraction of the
    training set after a train_test split.
    """
    # Load data and make train test splits
    data = load_dataset(mode=mode, file_name=file_name)
    X_train, X_test, y_train, y_test = train_test_split(data[config.FEATURES],
                                                        data[config.TARGET],
                                                        test_size=test_size,
                                                        # set the seed here:
                                                        random_state=random_state)
    
    # Specify split type
    first_dataset_name = config.TRAINING_DATA_FILE
    if(split_type == 'train_test'):
        second_dataset_name = config.TESTING_DATA_FILE
    elif(split_type == 'train_dev'):
        second_dataset_name = config.DEVELOPMENT_DATA_FILE
        third_dataset_name = config.TESTING_DATA_FILE
        data = ({config.FEATURES[0]: X_train[:,0], config.FEATURES[1]: X_train[:,1], 
                config.TARGET: y})
        X_train, X_dev, y_train, y_dev = train_test_split(data[config.FEATURES],
                                                    data[config.TARGET],
                                                    test_size=test_size,
                                                    # set the seed here:
                                                    random_state=random_state)
    else:
        raise ValueError('Value not supported for "split_type" in load_dataset.')
    
    # Specify where data will be stored
    if(mode == 'production'):
        dataset_dir = config.DATASET_DIR
    elif(mode == 'testing'):
        dataset_dir = config.DATASET_TESTING_DIR
    else:
        raise ValueError('Value not supported for "mode" in load_dataset.')

    # Join train, dev, and test datasets with their respective targets and save as csv.
    ## train
    train_data = X_train.join(y_train)
    train_data.to_csv(f'{dataset_dir}/{first_dataset_name}', index=False)
    ## dev
    if split_type == 'train_dev':
        dev_data = X_dev.join(y_dev)
        dev_data.to_csv(f'{dataset_dir}/{second_dataset_name}', index=False)
    ## test
    test_data = X_test.join(y_test)
    if split_type == 'train_dev':
        test_data.to_csv(f'{dataset_dir}/{third_dataset_name}', index=False)
    else:
        test_data.to_csv(f'{dataset_dir}/{second_dataset_name}', index=False)


def save_pipeline(*, pipeline_to_persist: pipeline) -> None:
    """Persist the pipline."""
    # Prepare versioned save file name
    save_file_name = f'{config.PIPELINE_SAVE_FILE}{_version}.pkl'
    save_path = config.TRAINED_MODEL_DIR / save_file_name

    # For differential testing
    remove_old_pipelines(files_to_keep=[save_file_name])
    joblib.dump(pipeline_to_persist, save_path)
    _logger.info(f'saved pipeline: {save_file_name}')

def load_pipeline(*, file_name: str) -> Pipeline:
    """Load a persisted pipeline."""
    file_path = config.TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model

def remove_old_pipelines(*, files_to_keep: t.List[str]) -> None:
    """
    Remove old model pipelines.
    
    This is to ensure that there is a one-to-one 
    mapping between the package version and the model
    version to be imported and used by other applications.
    However, we do also include the immediate previous
    pipelines version for differential testing purposes.
    """
    do_not_delete = files_to_keep + ['__init__.py', '__pycache__']
    for model_file in config.TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            print(config.TRAINED_MODEL_DIR)
            print(model_file)
            model_file.unlink()
