import argparse
import os
import time
import sys
import logging


#  set default values to some variables 
parser = argparse.ArgumentParser("ImageNet")
parser.add_argument('--batch_size', type=int, default=256, help='batch size')
parser.add_argument('--learning_rate', type=float, default=0.05, help='init learning rate')
parser.add_argument('--momentum', type=float, default=0.9, help='momentum')
parser.add_argument('--weight_decay', type=float, default=0.0001, help='weight decay')
parser.add_argument('--report_freq', type=float, default=100, help='report frequency')
parser.add_argument('--epochs', type=int, default=40, help='num of training epochs')
parser.add_argument('--save', type=str, default='EXP', help='experiment name')
parser.add_argument('--seed', type=int, default=2, help='random seed')
parser.add_argument('--grad_clip', type=float, default=10, help='gradient clipping')
parser.add_argument('--resume_train', action='store_true', default=False, help='resume training')
parser.add_argument('--resume_dir', type=str, default='./weights/checkpoint.pth.tar', help='save weights directory')
parser.add_argument('--load_epoch', type=int, default=30, help='random seed')
parser.add_argument('--weights_dir', type=str, default='./weights/', help='save weights directory')
parser.add_argument('--learning_step', type=list, default=[25,35,40], help='learning rate steps')


args = parser.parse_args()   # parse the arguments



###--------------------logging-----------------------------
# https://docs.python.org/3/library/logging.html


log_format = '%(asctime)s %(message)s'    # set logger format

# set logging basic configuration
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
    format=log_format, datefmt='%m/%d %I:%M:%S') 


#  create a directory to save the log files
if not os.path.exists(args.save):
    os.makedirs(args.save)


fh = logging.FileHandler(os.path.join(args.save, 'log.txt'))   # create file handler
fh.setFormatter(logging.Formatter(log_format))   # adding formatter to the file handler


logger = logging.getLogger()    # create logging object
logger.addHandler(fh)    # add file handler to logger

###--------------------------------------------------------

def main():

    epochs = args.epochs   # pass the values to the variables in the main script
    batch_size = args.batch_size

    print(batch_size)
    print(epochs)

    for epoch in range(epochs):

        logger.info('epoch %d lr %e', epoch, args.learning_rate)    # write the logging info



if __name__ == '__main__':
	main()