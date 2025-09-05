from pathlib import Path

# path = Path ("ecommerce1")
path = Path ()
# print(path.exists())
# print(path.glob('*.py'))
for file in path.glob('*'):
    print(file)