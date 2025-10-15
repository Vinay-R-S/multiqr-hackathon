import subprocess

def main():
    try:
        print("Running Step 5: rename_dataset.py")
        subprocess.run(["python", "./src/script/rename_dataset.py"], check=True)

        print("Running Step 6: train.py")
        subprocess.run(["python", "./train.py"], check=True)

        print("Running Step 7: infer.py")
        subprocess.run(["python", "./infer.py"], check=True)

        print("Running Step 8: evaluate.py")
        subprocess.run(["python", "./evaluate.py"], check=True)

        print("All steps executed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error while executing a script: {e}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")


if __name__ == "__main__":
    main()
