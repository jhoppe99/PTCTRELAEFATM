# main python file, for now running script
# just check if proper version of all dependencies 
# are installed properly 

from computations import VersionCheck

def main():
    vc = VersionCheck(are_versions_ok=False)
    print("*--------------------------------------------------*")
    print("|            Welcome! This is program              |")
    print("|    to calculate the rotational energy levels     |") 
    print("|   and eigenvectors for asymmetric top molecules  |")
    print("*--------------------------------------------------*")
    print("")
    print("Your dependencies status:")
    print(vc.print_version_checker_output())
    print("")

if __name__ == "__main__":

    main()
