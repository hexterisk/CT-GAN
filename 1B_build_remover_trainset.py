from procedures.datasetBuilder import *

# Init dataset builder for creating a dataset of evidence to inject
print('Initializing Dataset Builder for Evidence Removal')
builder = Extractor(is_healthy_dataset=True, parallelize=True)

# Extract training instances
# Source data location and save location is loaded from config.py
print('Extracting instances...')
builder.extract()

print('Done.')