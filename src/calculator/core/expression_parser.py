"""
Expression Parser
Parses and evaluates mathematical expressions.
"""

import math
import re
from typing import Union


class ExpressionParser:
    """Parser for mathematical expressions"""
    
    def __init__(self):
        self.operators = {
            '+': (1, lambda x, y: x + y),
            '-': (1, lambda x, y: x - y),
            '*': (2, lambda x, y: x * y),
            '/': (2, lambda x, y: x / y),
            '^': (3, lambda x, y: x ** y),
            '**': (3, lambda x, y: x ** y)
        }
    
    def parse_and_evaluate(self, expression: str) -> float:
        """
        Parse and evaluate a mathematical expression.
        
        Args:
            expression (str): Mathematical expression to evaluate
            
        Returns:
            float: Result of the evaluation
        """
        # Replace constants
        expression = expression.replace('pi', str(math.pi))
        expression = expression.replace('e', str(math.e))
        
        # Handle implicit multiplication (e.g., 2pi -> 2*pi)
        expression = re.sub(r'(\d)([a-z])', r'\1*\2', expression)
        expression = re.sub(r'([a-z])(\d)', r'\1*\2', expression)
        
        # Convert to postfix notation and evaluate
        tokens = self._tokenize(expression)
        postfix = self._infix_to_postfix(tokens)
        return self._evaluate_postfix(postfix)
    
    def _tokenize(self, expression: str) -> list:
        """Tokenize the expression"""
        # Remove spaces
        expression = expression.replace(' ', '')
        
        # Split into tokens
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit() or expression[i] == '.':
                # Number
                num = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                tokens.append(float(num))
            elif expression[i] in '+-*/^()':
                # Operator or parenthesis
                if expression[i] == '*' and i + 1 < len(expression) and expression[i+1] == '*':
                    tokens.append('**')
                    i += 2
                else:
                    tokens.append(expression[i])
                    i += 1
            elif expression[i].isalpha():
                # Function or variable
                func = ''
                while i < len(expression) and expression[i].isalpha():
                    func += expression[i]
                    i += 1
                tokens.append(func)
            else:
                i += 1
                
        return tokens
    
    def _infix_to_postfix(self, tokens: list) -> list:
        """Convert infix notation to postfix notation"""
        output = []
        operator_stack = []
        
        for token in tokens:
            if isinstance(token, (int, float)):
                output.append(token)
            elif token in self.operators:
                while (operator_stack and 
                       operator_stack[-1] != '(' and
                       operator_stack[-1] in self.operators and
                       self.operators[operator_stack[-1]][0] >= self.operators[token][0]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if operator_stack:
                    operator_stack.pop()  # Remove '('
        
        while operator_stack:
            output.append(operator_stack.pop())
            
        return output
    
    def _evaluate_postfix(self, postfix: list) -> float:
        """Evaluate postfix expression"""
        stack = []
        
        for token in postfix:
            if isinstance(token, (int, float)):
                stack.append(token)
            elif token in self.operators:
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                b = stack.pop()
                a = stack.pop()
                result = self.operators[token][1](a, b)
                stack.append(result)
            else:
                raise ValueError(f"Unknown token: {token}")
                
        if len(stack) != 1:
            raise ValueError("Invalid expression")
            
        return stack[0]