import jarvis.parse as p

mean_command = p.Utterance(utterance="Could you please compute the mean of the dataset X?")


def test_reformat():
    mean_command.reformat()
    reformatted = mean_command.filtered
    assert reformatted == ["compute", "mean", "dataset", "X"]


def test_parse_intent():
    reformatted = mean_command.reformat()
    command = mean_command.parse_intent(reformatted)
    assert command == ("Compute mean", "Dataset X")