# Script to train the pose models with csv files of training data.

import argparse
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score # Accuracy metrics 


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Train the posemodel from csv files"
    )

    parser.add_argument(
        "model", 
        type=str, 
        help="Pickle filename to load the model fname"
    )

   
    parser.add_argument(
        "csvfile", 
        type=str, 
        help="csv file to load the training data."
    )

    return parser

def main():
    opt = create_parser().parse_args()
    with open(opt.model, 'rb') as f:
        model = pickle.load(f)
    
    df = pd.read_csv(opt.csvfile)
    X = df.drop('class', axis = 1)
    y = df['class']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

    print(f">>> Starting to train the model")
    model.fit(X_train, y_train)

    print(f">>> Evaluating the model")
    yhat = model.predict(X_test)
    print(accuracy_score(y_test, yhat))


if __name__ == "__main__":
    main()