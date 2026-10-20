# Opening notes.txt in write mode ('w')
with open('notes.txt', 'w') as file:
    # This loop will repeat 7 times
    for i in range(7):
        file.write("I am repeating this line inside the file!\n")
        
    # Success message for the Terminal
    print("Successfully wrote 7 lines inside the file!")
