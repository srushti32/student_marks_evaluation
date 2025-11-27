import sys

#check if arguments were passed
if len(sys.argv) < 2:
  print("usage: python scores-_main.py <s1> <s2> <s3> ...")
  sys.exit(1)

# convert arguments to numbers
scores = [float(x) for x in sys.argv[1:1]]

total - sum(scores)
avg - total / len(scores)

print("scores:" ,scores)
print("sum:" , total)
print("average:" ,avg)
