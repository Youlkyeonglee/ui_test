import streamlit as st
import argparse
from datetime import datetime
import os

parser = argparse.ArgumentParser(description='AlphaPose Demo')
parser.add_argument('--output', type=str, default='output',
                    help='experiment configure file name')
args = parser.parse_args()

def main(args):
    folder_time = datetime.now().strftime("%Y%m%d%H%M")
    args.outputpath = os.path.join(args.output, folder_time)
    print(args.outputpath)
    
def app():
    main(args)

if __name__ == '__main__':
    app()