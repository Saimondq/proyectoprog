import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.set_page_config(page_title="Calculadora de Derivadas", layout="wide")
    st.title("Calculadora de Derivadas")
    st.sidebar.title("Navegación")
    option = st.sidebar.radio("Ir a", ["Introducción", "Fundamentación Matemática", "Ejemplos de Derivadas", "Cómo Añadir una Función", "Calculadora de Derivadas"])

    if option == "Introducción":
        st.header("Introducción")
        st.write("""
        La derivada de una función es una medida de la rapidez con la que cambia el valor de la función en relación con el cambio en su variable independiente. En términos simples, la derivada representa la pendiente de la tangente a la curva de la función en un punto dado.

        Las derivadas son fundamentales en muchas áreas de las matemáticas y las ciencias aplicadas. Se utilizan para encontrar tasas de cambio en problemas de física, optimización en economía, y para resolver ecuaciones diferenciales en ingeniería, entre otros.
        """)
    
    elif option == "Fundamentación Matemática":
        st.header("Fundamentación Matemática")
        st.write("""
        Si \( f(x) \) es una función, su derivada se denota como \( f'(x) \) o \( \\frac{df}{dx} \). La derivada se calcula usando las reglas básicas de derivación, como la regla de la suma, la regla del producto, la regla del cociente y la regla de la cadena.

        ### Reglas Básicas de Derivación:
        - **Regla de la suma**: \( (f(x) + g(x))' = f'(x) + g'(x) \)
        - **Regla del producto**: \( (f(x)g(x))' = f'(x)g(x) + f(x)g'(x) \)
        - **Regla del cociente**: \( \\left( \\frac{f(x)}{g(x)} \\right)' = \\frac{f'(x)g(x) - f(x)g'(x)}{(g(x))^2} \)
        - **Regla de la cadena**: \( (f(g(x)))' = f'(g(x))g'(x) \)

        ### Ejemplo de derivada:
        Si \( f(x) = x^2 \), su derivada es \( f'(x) = 2x \).
        """)

    elif option == "Ejemplos de Derivadas":
        st.header("Ejemplos de Derivadas")

        examples = [
            ("Derivada de f(x) = x^2", "f'(x) = 2x"),
            ("Derivada de f(x) = sin(x)", "f'(x) = cos(x)"),
            ("Derivada de f(x) = e^x", "f'(x) = e^x"),
            ("Derivada de f(x) = ln(x)", "f'(x) = 1/x"),
            ("Derivada de f(x) = 1/x", "f'(x) = -1/x^2"),
            ("Derivada de f(x) = cos(x)", "f'(x) = -sin(x)")
        ]

        for example, result in examples:
            st.write(f"**{example}:**")
            st.latex(f"{result}")

    elif option == "Cómo Añadir una Función":
        st.header("Cómo Añadir una Función a la Calculadora")

        st.write("""
        Para añadir una función en la calculadora de derivadas, sigue estos pasos:

        ### Paso 1: Escribir la Función
        - Introduce la función en términos de \( x \). Por ejemplo, para \( f(x) = x^2 \), escribe `x**2`.

        ### Paso 2: Calcular la Derivada
        - Haz clic en el botón "Calcular Derivada".

        ### Paso 3: Visualizar la Derivada y la Gráfica
        - La calculadora mostrará la derivada de la función y una gráfica que compara la función original con su derivada.

        ### Ejemplo
        Supongamos que queremos calcular la derivada de \( f(x) = x^3 \).

        #### Paso 1: Escribir la Función
        - Introduce `x**3`.

        #### Paso 2: Calcular la Derivada
        - Haz clic en "Calcular Derivada".

        Esto generará la respuesta \( 3x^2 \), que es la derivada de \( f(x) = x^3 \).
        """)

    elif option == "Calculadora de Derivadas":
        st.header("Calculadora de Derivadas")
        st.write("Introduce una función en términos de x:")
        expression = st.text_input("Función", "x^2")
        
        if st.button("Calcular Derivada"):
            try:
                x = sp.symbols('x')
                funcion = sp.sympify(expression)

                derivada = sp.diff(funcion, x)
                st.write(f"La derivada de la función {expression} es:")
                st.latex(f"{sp.latex(derivada)}")
                
                st.write("### Gráfica de la Función y su Derivada")
                f = sp.lambdify(x, funcion, 'numpy')
                f_deriv = sp.lambdify(x, derivada, 'numpy')

                x_vals = np.linspace(-10, 10, 400)
                y_vals = f(x_vals)
                y_deriv_vals = f_deriv(x_vals)

                plt.figure(figsize=(10, 5))
                plt.plot(x_vals, y_vals, label='f(x)')
                plt.plot(x_vals, y_deriv_vals, label="f'(x)")
                plt.legend()
                st.pyplot(plt)
            except Exception as e:
                st.write(f"Error en la entrada: {e}")

if __name__ == '__main__':
    main()
