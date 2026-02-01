import pickle
import sys

def view():
    print("Loading dataset...")
    try:
        with open('data.pkl', 'rb') as f:
            data = pickle.load(f)
            print("Data loaded successfully.")
            print(f"Data content: {data}")
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    view()
