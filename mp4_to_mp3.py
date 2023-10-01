#!/usr/local/bin/python

"A naive script to convert MP4 files to MP3"

import glob
import sys
import getopt
import os
from moviepy.editor import AudioFileClip


def main(argv):
    "The program's entry point"
    input_files = []
    output_directory = ""
    opts, _ = getopt.getopt(argv, "hi:o:", ["ifile=", "odir="])
    for opt, arg in opts:
        if opt == "-h":
            print("mp4_to_mp3.py -i <input_files> -o <output_directory>")
            sys.exit()
        elif opt in ("-i", "--ifiles"):
            input_files = glob.glob(arg)
        elif opt in ("-o", "--odir"):
            output_directory = arg
    #print("Input files are: ", input_files)
    #print("Output directory is: ", output_directory)

    for input_file in input_files:
        _, file_name = os.path.split(input_file)

        base_name = os.path.splitext(file_name)[0]
        new_file_name = base_name + ".mp3"
        output_file = os.path.join(output_directory, new_file_name)
        #print(f"{output_file}")
        with AudioFileClip(input_file) as clip:
            clip.write_audiofile(output_file)


if __name__ == "__main__":
    main(sys.argv[1:])
