from os import mkdir, path

from clone import Clone 

if __name__ == "__main__":
    if not path.exists("cache"):
        mkdir("cache")
    Clone().run()
