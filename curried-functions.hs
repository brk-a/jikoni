inc x = x + 1
add (x, y) = x + y
add_curried x y = x + y
add_curried_lambda  x = \y -> x + y
add_curried_lambda = \x -> (\y -> x + y)
cm (card, pin, request) = 100
cm card pin request = 100
cm = \card -> (\pin -> (\request -> 100))



main = 
    inc 5 -- expected output: 6
    map inc [1..10] -- expected output: [2,3,4,5,6,7,8,9,10,11]

    add(2, 3) -- expected output: 5

    {- a curried function is a function that takes in more than one arg one after the other, not simultaneously -}

    -- define the add function as a curried function
    --add_curried x y = x + y
    add_curried 2 3 -- expected output: 5

    {- what, then, is the point of the so-called 'curried' functions? -}
    {- Easy! One does not have to supply all the args when calling said function -}

    --demo
    {-notice how add_curried is called using only one arg, x. Arg y is supplied via the arr taken in by the map function-}
    map (add_curried 1) [1..10] -- expected output: [2,3,4,5,6,7,8,9,10,11]

    {- what, exactly, is happening in the bonnet? -}
    {- glad you asked. <clears throat> -}
    {- convert add_curried to a lambda function -}
    --add_curried_lambda  x = \y -> x + y  -- add_curried_lambda takes in 1 arg and waits for a second arg so it can return the sum of the 2 args
    -- y -> x + y is the lambda (anonymous or nameless) function
    {- take x to the RHS too -}
    --add_curried_lambda = \x -> (\y -> x + y) -- nested lambda function. add_curried_lambda returns a lambda fn that\
    --takes in arg x and returns a lambda fn that takes in arg y and returns the sum of x and y. Easy, innit?
    -- say this as fast as you can, as many times as you can: schonfinkel-ing

    map (add_curried_lambda 1) [1..10] -- expected output: [2,3,4,5,6,7,8,9,10,11]

    {- Can curried functions be applied in real life? -}
    {- Yes, they can -}

    --demo: cash machine aka ATM

    --cm (card, pin, request) = 100 -- assume the machine gives you 100 units of money every time you use it

    --cm card pin request = 100 -- curried fn
    --cm = \card -> (\pin -> (\request -> 100)) -- curried function containing nested lambda functions
    {- cm is a lambda fn that expects an arg, card, and returns a lambda fn that expects an arg, pin, and returns a lambda fn that expects an arg, request, that returns 100 units of money -}