from glob import glob
from itertools import chain
from os.path import getsize

from display import beautify_size_bytes
from parse_args import parse_arguments
from read_pdf import save_images_as_pdf


def main():
    # Parse arguments
    args = parse_arguments()
    input_images = args.input_images
    output = args.output
    # TODO: support page sizes (e.g. for A4, A3, etc.)
    page_size = args.page_size
    resolution = args.resolution

    # Handle wildcard paths
    files = list(map(glob, input_images))
    files = list(chain.from_iterable(files))

    # Convert image files to PDF and save the result
    save_images_as_pdf(files, output, resolution=resolution)

    # Print the output file's size
    out_size = getsize(output)
    print('Output PDF size: {}'.format(beautify_size_bytes(out_size)))


if __name__ == '__main__':
    main()
