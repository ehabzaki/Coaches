import distribution

def main():
    cd = distribution.CoachDistribution ()
    students1 = [ ]
    for i in range ( 13 ):
        students1.append (distribution.Student( "ahmed" ))
    for i in students1:
        cd.add_student ( i )
    coaches = [ ]
    for i in range ( 3 ):
        coaches.append (distribution.Coach())
    for i in coaches:
        cd.add_coach ( i )
    cd.distribute ()
    print ( "problem 1 ==>" )
    for i in coaches:
        print ( "Coach" + str ( i.id ) + ":" + str ( len ( i.students ) ) )
        print ( "Student IDs:" + str ( i.students ) )
    students2 = [ ]

    for i in range ( 10 ):
        students2.append (distribution.Student ( "mohamed" ) )
    for i in students2:
        cd.add_student ( i )
    cd.distribute ()
    print ( "problem 2 ==>" )

    for i in coaches:
        print ( "coach" + str ( i.id ) + ":" + str ( len ( i.students ) ) )
        print ( "Student IDs:" + str ( i.students ) )
    capacities = [ 20, 30, 50 ]
    c = 0
    for i in coaches:
        i.change_capacity ( capacities[ c ] )
        c += 1
    cd.distribute ()
    print ( "problem 3 ==>" )

    for i in coaches:
        print ( "coach" + str ( i.id ) + ":" + str ( len ( i.students ) ) )
        print ( "Student IDs:" + str ( i.students ) )


if __name__ == "__main__":
    main ()

