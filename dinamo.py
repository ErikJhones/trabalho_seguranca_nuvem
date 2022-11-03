import boto3

def criando_tabela():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='grupo2',
        KeySchema=[
            {
                'AttributeName': 'nome',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'matricula',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'nome',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'matricula',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.wait_until_exists()
    print(table.item_count)

def escrevendo(nome, matricula):

    # dynamodb = boto3.resource('dynamodb')
    # table = dynamodb.Table('grupo2')
    # print(table.creation_date_time)

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('grupo2')

    table.put_item(
        Item={
            'nome': nome,
            'matricula': matricula
        }
    )

def lendo(nome):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('grupo2')
    # response = table.get_item(
    #     Key={
    #         'nome': nome
    #     }
    # )
    # item = response['Item']

    response = table.query(KeyConditionExpression=boto3.dynamodb.conditions.Key('nome').eq(nome))
    item = response['Items']
    return item

def deletando_tabela():

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('grupo2')
    table.delete()