import json
import logging
 
# Configurar o logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
def lambda_handler(event, context):
    """
    Função Lambda de exemplo.
 
    Parameters:
    - event: dict, os dados recebidos pela Lambda (ex: de uma chamada do API Gateway)
    - context: objeto com informações sobre a execução (tempo, memória, etc)
 
    Returns:
    - dict: resposta compatível com API Gateway
    """
    logger.info("Evento recebido: %s", json.dumps(event))
 
    try:
        # Exemplo: extrair parâmetro do corpo JSON
        body = json.loads(event.get("body", "{}"))
        nome = body.get("nome", "Mundo")
 
        mensagem = f"Olá, {nome}!"
 
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "mensagem": mensagem
            })
        }
 
    except Exception as e:
        logger.error("Erro na execução da Lambda: %s", str(e))
 
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "erro": "Erro interno na função Lambda."
            })
        }
 
print(lambda_handler({}, []))