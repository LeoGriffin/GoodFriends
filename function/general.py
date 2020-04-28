import pickle


def save(data, list):
    if data == "person":
        file = "data/person.dat"
    elif data == "dette":
        file = "data/dette.dat"
    with open(file, "wb") as f:
        pickle.dump(len(list), f)
        for value in list:
            pickle.dump(value, f)