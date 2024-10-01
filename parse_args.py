import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert images to PDF')
    parser.add_argument('input_images', type=str, nargs='+', 
                        help='Input images to convert')
    parser.add_argument('-o', '--output', type=str, default='output.pdf', 
                        help='Output PDF file name (default: output.pdf)')
    parser.add_argument('-p', '--page-size', type=str, default='A4', 
                        help='Page size (default: A4)')
    parser.add_argument('-r', '--resolution', type=int, default=300, 
                        help='Resolution (default: 300 dpi)')
    args = parser.parse_args()
    return args