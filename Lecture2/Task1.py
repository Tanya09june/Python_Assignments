LIMIT = 42
Length = float(input("Enter the length of zander in cm:- "))
if Length >= LIMIT:
    print (f"Good Job! Trapped")
else:
    difference= LIMIT - Length
    print(f"The zander is below the legal size limit. \nPlease release fish back into the lake. \nIts {difference:.2f} CM short of limit.")

