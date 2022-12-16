import cv2
import argparse 


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Convert the image to a test image."
    )

    parser.add_argument(
        "image", type=str, help="Input image"
    )

    parser.add_argument(
        "--scale",
        "-s",
        default=100,
        type=int,
        help="resize the incoming video file by scale percent",
    )

    parser.add_argument(
        "--out",
        "-o",
        default='',
        type=str,
        help="Output csv file name"
    )

    return parser

def main():
    opt = create_parser().parse_args()
    if not opt.out:
        opt.out = "test.jpg"


    frame = cv2.imread(opt.image, 0)
    width = int(frame.shape[1] * opt.scale / 100)
    height = int(frame.shape[0] * opt.scale / 100)
    dim = (width, height)
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    cv2.imwrite(opt.out, resized)

if __name__ == "__main__":
    main()