# Script to train the pose models with csv files of training data.

import argparse
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score  # Accuracy metrics 


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Train the pose model from csv files"
    )

    parser.add_argument(
        "model", 
        type=str, 
        help="Pickle filename to load/save the model"
    )
   
    parser.add_argument(
        "csvfile", 
        type=str, 
        help="CSV file to load the training data."
    )

    # Optional argument to use the full dataset for training
    parser.add_argument(
        "--use-full-dataset",
        "-f",
        action="store_true",
        help="Use the full dataset for training without splitting into train-test sets."
    )

    return parser

def main():
    opt = create_parser().parse_args()
    with open(opt.model, 'rb') as f:
        model = pickle.load(f)
    
    df = pd.read_csv(opt.csvfile)
    print(f">>> Reading in {len(df.index)} frames from csv file")

    X = df.drop('class', axis=1)
    y = df['class']

    if not opt.use_full_dataset:
        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
    else:
        # Use the full dataset for training
        X_train, y_train = X, y

    print(f">>> Starting to train the model")
    model.fit(X_train.values, y_train)

    if not opt.use_full_dataset:
        print(f">>> Evaluating the model")
        yhat = model.predict(X_test.values)
        print(f"Accuracy: {accuracy_score(y_test, yhat)}")

    print(f">>> Overwriting the original model '{opt.model}' with new weights")
    with open(opt.model, 'wb') as fh:
         pickle.dump(model, fh)

if __name__ == "__main__":
    main()
