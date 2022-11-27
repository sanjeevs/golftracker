# Script to create a specified scikit-learn model
import argparse
import pickle


from sklearn.pipeline import make_pipeline 
from sklearn.preprocessing import StandardScaler 

from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Create a scilearn ml model and save to pkl"
    )

    parser.add_argument(
        "model", 
        type=str, 
        help="Pickle filename to save the model to."
    )

   
    parser.add_argument(
        "--algo",
        "-a",
        default='rf',
        type=str,
        help="ML Algorithm to use."
    )


    return parser

def main():
    opt = create_parser().parse_args()

    if opt.algo == "lr":
        pipeline = make_pipeline(StandardScaler(), LogisticRegression())
    elif opt.algo == "rc":
        pipeline = make_pipeline(StandardScaler(), RidgeClassifier())
    elif opt.algo == "rf":
        pipeline= make_pipeline(StandardScaler(), RandomForestClassifier())
    elif opt.algo == "gb":
        pipeline = make_pipeline(StandardScaler(), GradientBoostingClassifier())
    else:
        raise ValueError(f"Invalid value of algo='{opt.algo}'")
    

    with open(opt.model, 'wb') as fh:
        pickle.dump(pipeline, fh)


if __name__ == "__main__":
    main()