def solve(str, candidate, all_solutions):
    if str == "":
        # no more choices to make
        if is_balanced(candidate):
            all_solutions.append(candidate)
        return
    
    # means we still have choices to make
    firstchar = str[0]
    remainder = str[1:]
    
    # if the current character is not a bracket, then we don't have a choice, we must include it.
    if not( firstchar == '(' or firstchar == ')' ):
        solve(remainder, candidate + firstchar, all_solutions)
        return
    
    # if the code reaches here, it means that at this level of recursion, the current character is a bracket, then we have two choices!
    
    solve(remainder, candidate + firstchar , all_solutions)
    solve(remainder, candidate, all_solutions)
