import os

if __name__ == '__main__':
    os.system("rm -rf ./models/* && rasa train && rasa run --cors \"*\"")