import json
import pickle

friends = {"Dan": [20, "London", 3234342], "Maria": [25, "Madrid", 435257222]}

def serialize(object_to_serialize, file, serializer):

    if serializer == "pickle":
        with open(file, "wb") as f:
            pickle.dump(object_to_serialize, f)

    if serializer == "json":
        with open(file, "w") as f:
            json.dump(object_to_serialize, f)


def deserialize(serialized_object, serializer):

    if serializer == "pickle":
        with open(serialized_object, "rb") as f:
            obj = pickle.load(f)
            return obj

    if serializer == "json":
        with open(serialized_object, "r") as f:
            obj = json.load(f)
            return obj


serialize(friends, "results/friends.pickle", "pickle")
print(deserialize("results/friends.json", "json"))