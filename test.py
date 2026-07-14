
while True:
    ans_1 = int(input("""
          Escape the Boring Lecture.
          Your chracter is stuck in a mind numbing slide reading class, and you
          have to sneak out of the room without the proffesor noticing.
          
          The proffesor is on slide 47 of 100. Your brain is melting.
          Do you: 1)Try to sneak out the back door,
          or 2)Fake a coughing fit to leave?    """))
    
    if ans_1 == 1:
        print("You have successfully made it to the hallway.")
        ans_2 = int(input("""
                  You're in the hallway, but the security guard is walking towards you.
                  Do you: 1) Hide in the bathroom, or 2) Pretend you're looking for the library?"""))
        if ans_2 == 1:
            print("""
                  You duck into the bathroom just in time. You hear the heavy boots
                  of the security guard walk right past the door and fade down the hallway.
                  Once the coast is clear, you slip out the exit door to freedom.""")
            break
        elif ans_2 == 2:
            print("""
                You try to act casual and tell him you're just looking for the library.
                Unfortunately, the guard is too helpful. He says, "Oh, it's easy to get lost here,
                let me escort you!" He walks you right back to your classroom, opens the door,
                and escorts you straight back to your seat in front of the whole class.""")
            break
        else:
            print("Only answer with 1 or 2!")        
            
        
        
    elif ans_1 == 2:
        print("The professor handed you a tissue and told you to sitdown. Game over!")
        break
    else:
            print("Only answer with 1 or 2!")
            
    
    



