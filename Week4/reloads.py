import sample
import importlib

def changes():
    update = importlib.reload(sample)
    print(update)

for i in range(5):
    changes()
    input('Hit Enter to see update...')
