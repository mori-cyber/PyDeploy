import argparse

def get_plant_name():
    parser = argparse.ArgumentParser(description='Get a flower or plant name.')
    parser.add_argument('plant_name', type=str, help='Name of the flower or plant')
    args = parser.parse_args()
    return args.plant_name

if __name__ == "__main__":
    plant_name = get_plant_name()
    print("The provided plant name is:", plant_name)
