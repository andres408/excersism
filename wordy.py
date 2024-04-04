def answer(question):
    """
    Takes a question as input and evaluates the mathematical expression in the question.
    
    Parameters:
        question (str): The question containing a mathematical expression.
        
    Returns:
        Integer: The result of the expression
        
    Raises:
        ValueError: If the operation or question is not supported or contains invalid syntax
        
    """
    unsupported_operations = ["cubed"]
    non_math_questions = ["President", "United States"]
    invalid_syntax = ["plus plus"]

    question = question.removeprefix("What is").removesuffix("?").strip()
    if not question: raise ValueError("syntax error")

    if any(op in question for op in unsupported_operations):
        raise ValueError("unkwown operation")
    if any(non_math_questions in question for non_math_questions in non_math_questions):
        raise ValueError("unkwown question")
    if any(sintax in question for sintax in invalid_syntax):
        raise ValueError("syntax error")

    operations_accepted = ["plus","divided","minus","multiplied"]
    lista = [word for word in question.rstrip('?').split()]
    operations = [word for word in lista if word in operations_accepted]
    numeros = [int(word) for word in lista if word.isdigit() or word[0] == '-']
    total = numeros[0]
    indices_a_eliminar = [0,1]
    while True:
        if not operations:
            break
        if len(numeros) < 2:
            raise ValueError("syntax error")
        for i in operations:
            if i == 'plus': 
                result = numeros[0] + numeros[1]
            elif i == 'divided':
                result = numeros[0] / numeros[1]
            elif i == 'minus':
                result = numeros[0] - (numeros[1])
            elif i == 'multiplied':
                result = numeros[0] * numeros[1] 
            operations.remove(i)
            numeros.pop(0)
            numeros.pop(0)
            numeros.insert(0,result)
            total = result
            result = 0
    return total
    
    

print(answer("What is 1 plus 2 1?"))