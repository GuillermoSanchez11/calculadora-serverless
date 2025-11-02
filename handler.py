import json

def _parse_payload(event):
    """
    Extrae operacion, a, b desde:
      - JSON en event['body'] (POST)
      - o desde queryStringParameters (GET), por si quieres probar rápido.
    """
    operacion = None
    a = None
    b = None

    # 1) Intentar body JSON (POST)
    body = event.get("body")
    if body:
        try:
            data = json.loads(body)
            operacion = data.get("operacion")
            a = data.get("a")
            b = data.get("b")
        except Exception:
            pass

    # 2) Fallback: query params (GET)
    if operacion is None:
        qs = event.get("queryStringParameters") or {}
        operacion = qs.get("operacion", operacion)
        a = qs.get("a", a)
        b = qs.get("b", b)

    try:
        a = float(a) if a is not None else None
        b = float(b) if b is not None else None
    except ValueError:
        pass

    return operacion, a, b


def operaciones(event, context):
    operacion, a, b = _parse_payload(event)

    # Validaciones básicas
    if operacion not in {"suma", "resta", "multiplicacion", "division"}:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Operación no válida. Use: suma | resta | multiplicacion | division"})
        }

    if a is None or b is None:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Parámetros faltantes. Envíe 'a' y 'b'."})
        }

    # Cálculo
    if operacion == "suma":
        resultado = a + b
    elif operacion == "resta":
        resultado = a - b
    elif operacion == "multiplicacion":
        resultado = a * b
    elif operacion == "division":
        if b == 0:
            return {"statusCode": 400, "body": json.dumps({"error": "Error: división por cero"})}
        resultado = a / b

    return {
        "statusCode": 200,
        "body": json.dumps({"resultado": resultado})
    }
