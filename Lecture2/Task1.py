LIMIT = 42
Length = float(input("Enter the length of zander in cm:- "))
if Length >= LIMIT:
    print (f"Good Job! Trapped")
else:
    Difference= LIMIT - Length
    print(f"The zander is below the legal size limit. \nPlease release fish back into the lake. \nIts {Difference:.2f} CM short of limit.")

