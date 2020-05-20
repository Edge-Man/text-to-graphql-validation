from graphql import parse


# returns true if the prediction matches the target where any arguments or selection_sets are in unordered sets
# prediction and target are both string graphql queries
def is_exact_match(prediction, target):
    prediction_document = parse(prediction, no_location=True)
    target_document = parse(target, no_location=True)
    return prediction_document == target_document


# calls is_exact_set_match.
# 1 for true 0 for false
# handles errors as 0
def exact_match(prediction, target):
    try:
        return int(is_exact_match(prediction, target) == True)
    except:
        return 0


# calculates exact match accuracy over a list of predictions and their corresponding targets
def exact_match_accuracy(predictions, targets):
    assert len(predictions) == len(targets)
    matches = [exact_match(prediction, target) for prediction, target in zip(predictions, targets)]
    return sum(matches) / len(targets)
