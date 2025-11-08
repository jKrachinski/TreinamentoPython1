def fibonacci(x):
    """
    Calcula o número de Fibonacci na posição x.
    
    Args:
        x (int): A posição do número de Fibonacci (começando de 0)
    
    Returns:
        int: O número de Fibonacci na posição x
    
    Exemplos:
        fibonacci(0) -> 0
        fibonacci(1) -> 1
        fibonacci(2) -> 1
        fibonacci(3) -> 2
        fibonacci(10) -> 55
    """
    if x < 0:
        raise ValueError("A posição deve ser um número não-negativo")
    
    if x == 0:
        return 0
    elif x == 1:
        return 1
    
    # Cálculo iterativo para melhor performance
    a, b = 0, 1
    for _ in range(2, x + 1):
        a, b = b, a + b
    
    return b


def fibonacci_recursivo(x):
    """
    Calcula o número de Fibonacci na posição x usando recursão.
    Nota: Menos eficiente para valores grandes de x.
    
    Args:
        x (int): A posição do número de Fibonacci
    
    Returns:
        int: O número de Fibonacci na posição x
    """
    if x < 0:
        raise ValueError("A posição deve ser um número não-negativo")
    
    if x == 0:
        return 0
    elif x == 1:
        return 1
    
    return fibonacci_recursivo(x - 1) + fibonacci_recursivo(x - 2)


def fibonacci_sequencia(n):
    """
    Gera uma sequência de Fibonacci com n elementos.
    
    Args:
        n (int): Quantidade de números na sequência
    
    Returns:
        list: Lista com os primeiros n números de Fibonacci
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequencia = [0, 1]
    for i in range(2, n):
        sequencia.append(sequencia[i-1] + sequencia[i-2])
    
    return sequencia


if __name__ == "__main__":
    # Exemplos de uso
    print("Calculando números de Fibonacci:")
    print("-" * 40)
    
    # Teste com diferentes posições
    posicoes = [0, 1, 2, 5, 10, 15, 20]
    for pos in posicoes:
        resultado = fibonacci(pos)
        print(f"Fibonacci({pos}) = {resultado}")
    
    print("\n" + "=" * 40)
    print("\nPrimeiros 15 números da sequência:")
    print(fibonacci_sequencia(15))
    
    print("\n" + "=" * 40)
    print("\nTeste interativo:")
    try:
        x = int(input("\nDigite uma posição para calcular Fibonacci: "))
        resultado = fibonacci(x)
        print(f"\nO número de Fibonacci na posição {x} é: {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")
    except KeyboardInterrupt:
        print("\n\nPrograma encerrado.")
