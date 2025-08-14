#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Personalização do Gerador de Fichas de Treino
Autor: Filipe Soares - Consultoria Esportiva
Versão: 1.0

Este script automatiza a personalização do gerador de fichas de treino
para cada cliente, substituindo os placeholders pelos dados específicos.
"""

import os
import shutil
import json
from pathlib import Path

def personalizar_projeto(dados_cliente, pasta_origem=".", pasta_destino=None):
    """
    Personaliza o projeto para um cliente específico.
    
    Args:
        dados_cliente (dict): Dicionário com os dados do cliente
        pasta_origem (str): Pasta do template base
        pasta_destino (str): Pasta onde será criado o projeto personalizado
    
    Returns:
        str: Caminho da pasta do projeto personalizado
    """
    
    # Validar dados obrigatórios
    campos_obrigatorios = ["nome", "empresa", "cref", "telefone", "short_name"]
    for campo in campos_obrigatorios:
        if campo not in dados_cliente or not dados_cliente[campo]:
            raise ValueError(f"Campo obrigatório '{campo}' não fornecido ou vazio")
    
    # Definir pasta de destino se não fornecida
    if pasta_destino is None:
        nome_pasta = dados_cliente["nome"].lower().replace(" ", "-")
        pasta_destino = f"ficha-treino-{nome_pasta}"
    
    # Criar pasta de destino
    if os.path.exists(pasta_destino):
        resposta = input(f"A pasta '{pasta_destino}' já existe. Deseja sobrescrever? (s/n): ")
        if resposta.lower() != "s":
            print("Operação cancelada.")
            return None
        shutil.rmtree(pasta_destino)
    
    # Copiar arquivos do template
    print(f"Copiando arquivos do template para '{pasta_destino}'...")
    shutil.copytree(pasta_origem, pasta_destino, ignore=shutil.ignore_patterns("personalizar.py", "__pycache__", "*.pyc"))
    
    # Definir placeholders e seus valores
    placeholders = {
        "{{CONSULTOR_NOME}}": dados_cliente["nome"],
        "{{CONSULTOR_NOME_UPPER}}": dados_cliente["nome"].upper(),
        "{{CONSULTOR_EMPRESA}}": dados_cliente["empresa"],
        "{{CONSULTOR_CREF}}": dados_cliente["cref"],
        "{{CONSULTOR_TELEFONE}}": dados_cliente["telefone"],
        "{{CONSULTOR_SHORT_NAME}}": dados_cliente["short_name"]
    }
    
    # Arquivos que serão personalizados
    arquivos_para_personalizar = [
        "index.html",
        "manifest.json"
    ]
    
    # Personalizar cada arquivo
    for arquivo in arquivos_para_personalizar:
        caminho_arquivo = os.path.join(pasta_destino, arquivo)
        if os.path.exists(caminho_arquivo):
            print(f"Personalizando {arquivo}...")
            
            # Ler conteúdo do arquivo
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                conteudo = f.read()
            
            # Substituir placeholders
            for placeholder, valor in placeholders.items():
                conteudo = conteudo.replace(placeholder, valor)
            
            # Escrever arquivo personalizado
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                f.write(conteudo)
    
    print(f"\n✅ Projeto personalizado criado com sucesso em: {pasta_destino}")
    print(f"📁 Pasta: {os.path.abspath(pasta_destino)}")
    
    return pasta_destino

def criar_readme_cliente(pasta_projeto, dados_cliente):
    """
    Cria um README específico para o cliente.
    """
    readme_content = f"""# Gerador de Fichas de Treino - {dados_cliente["nome"]}

## 📋 Informações do Cliente

- **Nome**: {dados_cliente["nome"]}
- **Empresa**: {dados_cliente["empresa"]}
- **CREF**: {dados_cliente["cref"]}
- **Telefone**: {dados_cliente["telefone"]}

## 🚀 Como usar

1. Faça upload desta pasta para um repositório GitHub
2. Conecte o repositório ao Vercel
3. O deploy será feito automaticamente
4. Compartilhe o URL com o cliente

## 📱 PWA (Progressive Web App)

Este projeto é um PWA que pode ser instalado na tela inicial do celular:

### Android:
- Abra no Chrome/Firefox
- Aparecerá um banner de instalação
- Toque em "Instalar"

### iOS:
- Abra no Safari
- Toque no ícone de compartilhamento
- Selecione "Adicionar à Tela de Início"

## 🔧 Personalização

Este projeto foi personalizado automaticamente com os dados do cliente.
Todos os placeholders foram substituídos pelos dados específicos.

## 📞 Suporte

Para suporte técnico, entre em contato com Filipe Soares - Consultoria Esportiva.
"""
    
    caminho_readme = os.path.join(pasta_projeto, "README.md")
    with open(caminho_readme, "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print(f"📄 README.md criado para o cliente")

def main():
    """
    Função principal - interface de linha de comando.
    """
    print("🏋️ Gerador de Fichas de Treino - Script de Personalização")
    print("=" * 60)
    
    # Coletar dados do cliente
    print("\n📝 Insira os dados do cliente:")
    
    dados_cliente = {}
    dados_cliente["nome"] = input("Nome completo do consultor: ").strip()
    dados_cliente["empresa"] = input("Nome da empresa/consultoria: ").strip()
    dados_cliente["cref"] = input("CREF (ex: 123456-G/SP): ").strip()
    dados_cliente["telefone"] = input("Telefone (ex: +55 11 99999-9999): ").strip()
    dados_cliente["short_name"] = input("Nome curto para o app (ex: Fichas JS): ").strip()
    
    # Validar se todos os campos foram preenchidos
    for campo, valor in dados_cliente.items():
        if not valor:
            print(f"❌ Erro: O campo '{campo}' é obrigatório.")
            return
    
    # Confirmar dados
    print("\n📋 Dados inseridos:")
    for campo, valor in dados_cliente.items():
        print(f"  {campo.replace('_', ' ').title()}: {valor}")
    
    confirmar = input("\n✅ Os dados estão corretos? (s/n): ").strip().lower()
    if confirmar != "s":
        print("❌ Operação cancelada.")
        return
    
    try:
        # Personalizar projeto
        pasta_projeto = personalizar_projeto(dados_cliente)
        
        if pasta_projeto:
            # Criar README para o cliente
            criar_readme_cliente(pasta_projeto, dados_cliente)
            
            print("\n🎉 Personalização concluída com sucesso!")
            print(f"\n📋 Próximos passos:")
            print(f"1. Substitua os ícones (icon-*.png) pelos ícones do cliente")
            print(f"2. Substitua o logo.jpeg pelo logo do cliente")
            print(f"3. Crie um repositório GitHub com os arquivos da pasta: {pasta_projeto}")
            print(f"4. Conecte o repositório ao Vercel")
            print(f"5. Entregue o URL do Vercel ao cliente")
            
    except Exception as e:
        print(f"❌ Erro durante a personalização: {e}")

if __name__ == "__main__":
    main()

