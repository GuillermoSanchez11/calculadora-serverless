# 🧮 Calculadora Serverless (Python + AWS Lambda)

Proyecto del **Laboratorio 3 - Cloud Computing / Serverless**, implementado con el **Serverless Framework**, **Python 3.12** y **AWS Lambda**.

---

## 🚀 Descripción del proyecto

Esta aplicación expone una **API RESTful** desplegada en **AWS Lambda** y **API Gateway**, que permite realizar operaciones matemáticas básicas:

- ➕ Suma  
- ➖ Resta  
- ✖️ Multiplicación  
- ➗ División  

El proyecto está desarrollado en **Python**, utilizando el **Serverless Framework** para automatizar el despliegue, pruebas locales y configuración de infraestructura en AWS.

---

## 📁 Estructura del proyecto

```text
calculadora-serverless/
│
├── handler.py        # Código principal de la función Lambda
├── serverless.yml    # Configuración del framework Serverless
├── package.json      # Dependencias locales (por ejemplo, serverless-offline)
└── README.md         # Documentación del proyecto
```


---

## ⚙️ Tecnologías utilizadas

- **AWS Lambda** → Funciones sin servidor  
- **AWS API Gateway** → Exposición HTTP del servicio  
- **Serverless Framework** → Automatización de despliegues y entornos  
- **Python 3.12** → Lenguaje de programación  
- **Node.js / npm** → Gestión de dependencias  
- **serverless-offline** → Pruebas locales de la API  

---

## 🧠 Funcionamiento

El endpoint principal recibe un cuerpo JSON con los siguientes campos:

```json
{
  "operacion": "suma | resta | multiplicacion | division",
  "a": 10,
  "b": 5
}
```

Y responde con un JSON que contiene el resultado:
```json
{
  "resultado": 15
}
```