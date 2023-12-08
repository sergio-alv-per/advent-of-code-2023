from sys import stdin

def make_prediction(ecosystem):
    if all(x == 0 for x in ecosystem):
        return 0
    else:
        # Literally the only line changed from part 1
        return ecosystem[0] - make_prediction([y-x for x, y in zip(ecosystem, ecosystem[1:])])

prediction_sum = 0
for line in (l.strip() for l in stdin):
    ecosystem = [int(x) for x in line.split(" ")]
    prediction_sum += make_prediction(ecosystem)

print(prediction_sum)