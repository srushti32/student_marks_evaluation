import sys

if len(sys.argv) < 2:
    print("usage: python scores_local.py <s1> <s2> <s3>...")
    sys.exit(1)

scores = [float(x) for x in sys.argv[1:]]

print("scores:", scores)
print("sum:", sum(scores))
print("average:", sum(scores) / len(scores))
print("maximum:", max(scores))
print("minimum:", min(scores))


