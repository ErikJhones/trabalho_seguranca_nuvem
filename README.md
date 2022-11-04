# trabalho_seguranca_nuvem

## equipe

Juliana  
Erik  
Hyago  
Davyson  

## descrição

## Subindo a aplicação pro ec2
Crie uma instância no ec2 (tenha certeza de criar uma nova chave .pem). 

EM seguinda acesse sua instância via SSH. 

Dentro do terminal da instância digite os seguintes comandos:  

`sudo apt-get update`  
`sudo apt-get install -y python3-pip nginx`  
`sudo vim /etc/nginx/sites-enabled/fastapi_nginx`  

Esse último comando vai abrir um novo terminal. Nele, digite o seguinte código:  

`
server {
        listen 80;
        server_name ipv4_da_instancia_ec2;
        location / {
                proxy_pass http://127.0.0.1:8000;
        }
}
`

depois digte `esc` e escreva `:wq` e então digite `enter` (isso irá salvar esse código).  

Após isso digite no terminal:  
`sudo service nginx restart`  

Depois clone a aplicação com: `git clone link_api_do_github`  
Entre dentro do diretório da aplicação com: `cd nome_diretório`  
Instale as dependências do python: `pip install -r requirements.txt`  
Execute a aplicação: `python3 -m uvicorn api:app`  

## usando o dinamodb do aws
Para conseguir criar tabelas, inserir dados e realizar consultas no dinamidb da aws, é necessário fornecer uma permissão.  

Para isso dentro do terminal SSH do ec2 crie uma pasta oculta chamada `.aws`: `mkdir .aws`  

Entre nessa nova pasta: `cd .aws`  

E crie um arquivo chamado `credentials`: `nano credentials`  

Dentro desse arquivo, cole as credenciais do aws e salve.

Essa operação vai permitir que um SDK python consiga criar serviços na aws (como ec2, s3, rcs e etc).