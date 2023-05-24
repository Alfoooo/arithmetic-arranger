def arithmetic_arranger(problems, cond=False):
    firstLine = ''
    secondLine = ''
    thirdLine = ''
    fourthLine = ''

    try:
        #Check if problems are more than five
        if len(problems) > 5:
            return "Error: Too many problems."
        
        for numbers in problems:
            item = numbers.split()

            #Check if numbers digit are more than four
            if len(item[0]) > 4 or len(item[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
            
            #Calculating the numbers
            if item[1] == '+':
                result = int(item[0])+int(item[2])
            elif item[1] == '-':
                result = int(item[0])-int(item[2])
            else:
                return "Error: Operator must be '+' or '-'."
            
            #Adding whitespaces for right-align
            if len(item[0]) < len(item[2]):
                i = len(item[0])
                while i < len(item[2]):
                    item[0] = ' ' + item[0]
                    i += 1
            elif len(item[0]) > len(item[2]):
                i = len(item[2])
                while i < len(item[0]):
                    item[2] = ' ' + item[2]
                    i += 1

            firstLine = firstLine + '  ' + item[0] + '    '
            secondLine = secondLine + item[1] + ' ' + item[2] + '    '
            thirdLine = thirdLine + '-' * (len(item[0])+2) + '    '

            if cond:
                if len(str(result)) < len(item[0])+2:
                    i = len(str(result))
                    while i < len(item[0])+2:
                        result = ' ' + str(result)
                        i += 1
                fourthLine = fourthLine + result + '    '
    except ValueError:
        return "Error: Numbers must only contain digits."
    
    results = firstLine.rstrip() + '\n' + secondLine.rstrip() + '\n' + thirdLine.rstrip()
    if cond:
        results = results + '\n' + fourthLine.rstrip()

    return results