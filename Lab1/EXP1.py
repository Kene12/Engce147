squares = [ x**2 for x in range( 10 ) ]

squares_dict = { x: x**2 for x in range( 5 ) }

even_squares = { x**2 for x in range( 10 ) if x % 2 == 0 }

# output
print( squares )
print( squares_dict )
print( even_squares )