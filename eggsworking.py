def EggsintoBoxes():
    eggs = int(input("input the number of eggs here "))
    boxesfilled = eggs / 6
    boxcalc = eggs % 6
    if boxcalc != 0:
        boxesfilled = boxesfilled - (boxesfilled % 1)
        Eggleftover = eggs -(boxesfilled * 6)
        print ("There are",Eggleftover, "eggs left over")
        if boxesfilled == 1:
            print (boxesfilled, "Box is filled")
        if boxesfilled > 1:
            print (boxesfilled, "Boxes are filled")
    if boxcalc == 0:
        print (boxesfilled)
        print ("There are no eggs left over")
    

EggsintoBoxes()
