import jarvis.parse as p


def test_reformat():
    mean_command = p.Utterance(utterance="Could you please compute the mean of the dataset X?")
    mean_command.reformat()
    reformatted = mean_command.filtered
    assert reformatted == ["compute", "mean", "dataset", "x"]


def test_parse_intent():
    mean_command = p.Utterance(utterance="Could you please compute the mean of the dataset X?")
    reformatted = mean_command.reformat()
    command = mean_command.parse_intent(reformatted)
    assert command == ("Compute mean", "Dataset X")


