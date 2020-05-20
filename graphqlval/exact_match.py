from graphql import parse


# returns true if the prediction matches the target where any arguments or selection_sets are in unordered sets
# prediction and target are both string graphql queries
def exact_set_match(prediction, target):
    prediction_document = parse(prediction, no_location=True)
    target_document = parse(target, no_location=True)
    return prediction_document == target_document


# calculates exact match accuracy over a list of predictions and their corresponding targets
def exact_match_accuracy(predictions, targets):
    assert len(predictions) == len(targets)
    matches = [1 if exact_set_match(prediction, target) else 0 for prediction, target in zip(predictions, targets)]
    sum(matches)
    return sum(matches)/len(targets)
