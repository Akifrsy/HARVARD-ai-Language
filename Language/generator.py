import markovify
import sys

# Read text from file
if len(sys.argv) != 2:
    sys.exit("Usage: python generatorçpy sample.txt")
with open(sys.argv[1]) as f:
    text = f.read()

# Train model
text_model = markovify.Text(text)

# Generate sentences
print()
for i range(5):
    print(text_model.make_sentence())
    print()