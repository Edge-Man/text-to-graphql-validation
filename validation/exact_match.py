from graphql import parse

# This is exact set matching? it's either correct or not.
# "Full set matching" would be comparing the name of each node in the tree. it would be an accuracy out of the number of nodes.
# so i would be comparing the child nodes at each level to get a percentage correct.


# returns true if the prediction matches the target where any arguments or selection_sets are in unordered sets
# prediction and target are both string graphql queries
def exact_set_match(prediction, target):
    prediction_document = parse(prediction)
    target_document = parse(target)
    return prediction_document == target_document

