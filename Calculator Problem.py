def Calc(string):
    # Step 1 - Make the Numbers into a List---------------------------------------------------------------------------------
    # Seperate string into a list, but regroup repeating integers
    MyList1 = []
    A = 0
    B = 1
    for i in range(0,len(string)):
        # Check if the string is a number
        try:
            if string[i] == " ":
                "Do Nothing"
            else:
                # Negative Sign Detected
                if string[i] == "-":
                    if B == 1:
                        B = B + 1
                        A = 0
                    else:
                        MyList1.append(string[i])
                else: 
                        if string[i] == ".":
                            A = A+1
                        else:
                            float(string[i])
                            A = A + 1 
                        # Make numbers negative
                        if B == 2:
                            MyList1.append("-" + string[i])
                        else: 
                            #Combine Consecutive Numbers
                            if A > 1:
                                MyList1[len(MyList1)-1] = MyList1[len(MyList1)-1] + string[i]
                            else:
                                MyList1.append(string[i])    
                            if i == len(string)-1:
                                "Do Nothing"
                            else:
                                if string[i+1] == "(": 
                                   MyList1.append("*")        
        # If not number, then return the string
        except:
            MyList1.append(string[i])
            A = 0
        if i == 0:
            "Do Nothing"
        else:
            if string[i] == "-":
                "Do Nothing"
            else:
                if string[i] == "(" or string[i] == "+" or string[i] == "*" or string[i] == "/" or string[i] == "-":
                    B = 1
                else:
                    B = 3

    # Turn Number Strings into floats in the list 
    MyList2 = []
    for i in range(0,len(MyList1)):
        # Check if the string is a number
        try:
            MyList2.append(float(MyList1[i]))
        # Otherwise return the string
        except:
            MyList2.append(MyList1[i])

    # Step 2 - Solve Each Parenthesis---------------------------------------------------------------------------------
    # Continue Solving sets of parenthesis until none are left
    while MyList2.count("(") > 0 or MyList2.count(")") > 0:
        #Make a Array of '(' & ')' Locations
        OpenParenthesis = []
        CloseParenthesis = []
        for i in range(0,len(MyList2)):
            if MyList2[i] == "(": 
                OpenParenthesis.append(i)
            if MyList2[i] == ")":
                CloseParenthesis.append(i)

        # Find Parenthesis For Evaluation - Looking for something with no parenthesis inside
        i = 0
        A = 0 
        # Compare the location of the open parenthesis to closed
        while A == 0:
            for j in range(0,len(CloseParenthesis)):
                # Create a test list of the rest of the Open Parenthesis in the array
                TestList = OpenParenthesis[i+1:len(OpenParenthesis)]
                # If you're on the last one, and all others have failed the test below, 
                # then we can assume that one has no open parenthesis before the next closed
                if len(TestList) == 0:
                    A = 1
                    Open_Val = OpenParenthesis[i]+1 
                    Closed_Val = CloseParenthesis[j]
                    break
                else:   
                    # Test if the minimum of the rest of the open parenthesis locations
                    # is greater than each respective closed parenthesis location
                    if min(TestList) > CloseParenthesis[j] and min(TestList):
                        A = 1
                        Open_Val = OpenParenthesis[i]+1
                        Closed_Val = CloseParenthesis[j]
                        break
            i = i+1           

        # Splice original set to concentrate and solve
        StringSolving = MyList2[Open_Val:Closed_Val]
        # Save the other splices for later "Reconstruction"
        String_Unsolved_Start = MyList2[0:Open_Val-1]
        String_Unsolved_Final = MyList2[Closed_Val+1:len(MyList2)]

        # Evaluate Exponent
        Solution = []
        A = 0
        # Continue looping until no more ^ exist
        while StringSolving.count("^") > 0:
            for i in range(0,len(StringSolving)):
                # Evaluate ^ signs (Once per cycle)
                U = StringSolving[i:len(StringSolving)].count("^")
                if A == 0 and StringSolving[i] == "^":
                    if U == 1:
                        Solution.append(StringSolving[i-1]**StringSolving[i+1])
                        A = i
                    else:
                        Solution.append(StringSolving[i-1])
                        Solution.append(StringSolving[i])
                else:
                    # Once First Evaluation is Completed, Append everything unless it's the value right after.
                    if A > 0:
                        if i == A + 1:
                            "Do Nothing"
                        else:
                            Solution.append(StringSolving[i])
                    else:
                        # Add in integers that aren't already being evaluated by ^, copy *, /, +, - signs
                        if i == 0: # If i is value 0, we need to trim the if statement to not include the value before it
                            if (isinstance(StringSolving[i],float) and (StringSolving[i+1] == "+" or StringSolving[i+1] == "-"
                            or StringSolving[i+1] == "*" or StringSolving[i+1] == "/")):
                                Solution.append(StringSolving[i])
                        else:
                            if i == len(StringSolving)-1: # If i is the last value, we need to trim the if statement to not include the value after it
                                if (isinstance(StringSolving[i],float) and (StringSolving[i-1] == "+" or StringSolving[i-1] == "-"
                                or StringSolving[i-1] == "*" or StringSolving[i-1] == "/")):
                                    Solution.append(StringSolving[i])
                            else:
                                if (isinstance(StringSolving[i],float) and (StringSolving[i-1] == "+" or StringSolving[i-1] == "-"
                                or StringSolving[i-1] == "*" or StringSolving[i-1] == "/") and (StringSolving[i+1] == "+" or StringSolving[i+1] == "-"
                                or StringSolving[i+1] == "*" or StringSolving[i+1] == "/")):
                                    Solution.append(StringSolving[i])
                                else:
                                    if StringSolving[i] == "+" or StringSolving[i] == "-" or StringSolving[i] == "*" or StringSolving[i] == "/":
                                        Solution.append(StringSolving[i])
            # Reset A, and transfer the solution back to the solving array
            A = 0
            StringSolving = []
            StringSolving = Solution
            Solution = []

        # Evaluate Multiplication vs Division
        Solution = []
        A = 0
        # Continue looping until no more * or / exist
        while StringSolving.count("*") > 0 or StringSolving.count("/") > 0:
            for i in range(0,len(StringSolving)):
                # Evaluate * and / signs (Once per cycle)
                if A == 0 and (StringSolving[i] == "*" or StringSolving[i] == "/"):
                    if StringSolving[i] == "*":
                        Solution.append(StringSolving[i-1]*StringSolving[i+1])
                        A = i
                    if StringSolving[i] == "/":
                        Solution.append(StringSolving[i-1]/StringSolving[i+1])
                        A = i
                else:
                    # Once First Evaluation is Completed, Append everything unless it's the value right after.
                    if A > 0:
                        if i == A + 1:
                            "Do Nothing"
                        else:
                            Solution.append(StringSolving[i])
                    else:
                        # Add in integers that aren't already being evaluated in the * and /, and copy + and -
                        if i == 0: # If i is value 0, we need to trim the if statement to not include the value before it
                            if isinstance(StringSolving[i],float) and (StringSolving[i+1] == "+" or StringSolving[i+1] == "-"):
                                Solution.append(StringSolving[i])
                        else:
                            if i == len(StringSolving)-1: # If i is the last value, we need to trim the if statement to not include the value after it
                                if isinstance(StringSolving[i],float) and (StringSolving[i-1] == "+" or StringSolving[i-1] == "-"):
                                    Solution.append(StringSolving[i])
                            else:
                                if (isinstance(StringSolving[i],float) and (StringSolving[i+1] == "+" or StringSolving[i+1] == "-") 
                                and (StringSolving[i-1] == "+" or StringSolving[i-1] == "-")):
                                    Solution.append(StringSolving[i])
                                else:
                                    if StringSolving[i] == "+" or StringSolving[i] == "-":
                                        Solution.append(StringSolving[i])
            # Reset A, and transfer the solution back to the solving array
            A = 0
            StringSolving = []
            StringSolving = Solution
            Solution = []

        # Now Evaluate Addition and Subtraction
        # Continue looping until no more + or - exist
        while StringSolving.count("+") > 0 or StringSolving.count("-") > 0:
            for i in range(0,len(StringSolving)):
                # Allow only once cycle of addition and subtraction, then repeat
                if A == 0 and (StringSolving[i] == "+" or StringSolving[i] == "-"): 
                    if StringSolving[i] == "+":
                        Solution.append(StringSolving[i-1]+StringSolving[i+1])
                        A = i
                    if StringSolving[i] == "-":
                        Solution.append(StringSolving[i-1]-StringSolving[i+1])
                        A = i
                else:
                    if A > 0:
                        if i == A + 1:
                            "Do Nothing"
                        else:
                            Solution.append(StringSolving[i])
            # Reset A, and transfer the solution back to the solving array
            A = 0
            StringSolving = []
            StringSolving = Solution
            Solution = []
        # Make new list and run it again!
        MyList2 = String_Unsolved_Start + StringSolving + String_Unsolved_Final

    #Code is Repeated from Solution Above to solve the final problem with no more parenthesis
    StringSolving = MyList2
    # ---------------------------------- REPEATED CODE START-------------------------------------------------------------------
    # This code is to carry out PEMDAS once the parenthesis are gone. This is the final step now that the entire array contains no parenthesis
    #EVAL Exponenents
    Solution = []
    A = 0
    while StringSolving.count("^") > 0:
        for i in range(0,len(StringSolving)):
            U = StringSolving[i:len(StringSolving)].count("^")
            if A == 0 and StringSolving[i] == "^":
                if U == 1:
                    Solution.append(StringSolving[i-1]**StringSolving[i+1])
                    A = i
                else:
                    Solution.append(StringSolving[i-1])
                    Solution.append(StringSolving[i])
            else:
                if A > 0:
                    if i == A + 1:
                        "Do Nothing"
                    else:
                        Solution.append(StringSolving[i])
                else:
                    if i == 0: 
                        if (isinstance(StringSolving[i],float) and (StringSolving[i+1] == "+" or StringSolving[i+1] == "-"
                        or StringSolving[i+1] == "*" or StringSolving[i+1] == "/")):
                            Solution.append(StringSolving[i])
                    else:
                        if i == len(StringSolving)-1: 
                            if (isinstance(StringSolving[i],float) and (StringSolving[i-1] == "+" or StringSolving[i-1] == "-"
                            or StringSolving[i-1] == "*" or StringSolving[i-1] == "/")):
                                Solution.append(StringSolving[i])
                        else:
                            if (isinstance(StringSolving[i],float) and (StringSolving[i-1] == "+" or StringSolving[i-1] == "-"
                            or StringSolving[i-1] == "*" or StringSolving[i-1] == "/") and (StringSolving[i+1] == "+" or StringSolving[i+1] == "-"
                            or StringSolving[i+1] == "*" or StringSolving[i+1] == "/")):
                                Solution.append(StringSolving[i])
                            else:
                                if StringSolving[i] == "+" or StringSolving[i] == "-" or StringSolving[i] == "*" or StringSolving[i] == "/":
                                    Solution.append(StringSolving[i])
        A = 0
        StringSolving = []
        StringSolving = Solution
        Solution = []
    
    # EVAL Multi/Division
    Solution = []
    A = 0
    while StringSolving.count("*") > 0 or StringSolving.count("/") > 0:
        for i in range(0,len(StringSolving)):
            if A == 0 and (StringSolving[i] == "*" or StringSolving[i] == "/"):
                if StringSolving[i] == "*":
                    Solution.append(StringSolving[i-1]*StringSolving[i+1])
                    A = i
                if StringSolving[i] == "/":
                    Solution.append(StringSolving[i-1]/StringSolving[i+1])
                    A = i
            else:
                if A > 0:
                    if i == A + 1:
                        "Do Nothing"
                    else:
                        Solution.append(StringSolving[i])
                else:
                    if i == 0: 
                        if isinstance(StringSolving[i],float) and (StringSolving[i+1] == "+" or StringSolving[i+1] == "-"):
                            Solution.append(StringSolving[i])
                    else:
                        if i == len(StringSolving)-1: 
                            if isinstance(StringSolving[i],float) and (StringSolving[i-1] == "+" or StringSolving[i-1] == "-"):
                                Solution.append(StringSolving[i])
                        else:
                            if (isinstance(StringSolving[i],float) and (StringSolving[i+1] == "+" or StringSolving[i+1] == "-") 
                            and (StringSolving[i-1] == "+" or StringSolving[i-1] == "-")):
                                Solution.append(StringSolving[i])
                            else:
                                if StringSolving[i] == "+" or StringSolving[i] == "-":
                                        Solution.append(StringSolving[i])
        A = 0
        StringSolving = []
        StringSolving = Solution
        Solution = []

    # EVAL Addition/Subtraction
    while StringSolving.count("+") > 0 or StringSolving.count("-") > 0:
        for i in range(0,len(StringSolving)):
            if A == 0 and (StringSolving[i] == "+" or StringSolving[i] == "-"):
                if StringSolving[i] == "+":
                    Solution.append(StringSolving[i-1]+StringSolving[i+1])
                    A = i
                if StringSolving[i] == "-":
                    Solution.append(StringSolving[i-1]-StringSolving[i+1])
                    A = i
            else:
                if A > 0:
                    if i == A + 1:
                        "Do Nothing"
                    else:
                        Solution.append(StringSolving[i])
        A = 0
        StringSolving = []
        StringSolving = Solution
        Solution = []
    # ---------------------------------- REPEATED CODE END-------------------------------------------------------------------
    return(StringSolving[0])

print(Calc("(4^2^3)-(-3)^3"))
