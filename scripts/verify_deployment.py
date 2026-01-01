#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Verificação para Deploy do GitHub Pages
Verifica se todos os arquivos necessários estão presentes e corretos antes do deploy.
"""

import os
import json
import sys
from pathlib import Path
from typing import List, Tuple

# Configurar encoding UTF-8 para stdout
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def check_file_exists(filepath: str) -> Tuple[bool, str]:
    """Verifica se um arquivo existe."""
    if os.path.exists(filepath):
        return True, f"✅ {filepath}"
    return False, f"❌ {filepath} (NÃO ENCONTRADO)"


def check_json_valid(filepath: str) -> Tuple[bool, str]:
    """Verifica se um arquivo JSON é válido."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            json.load(f)
        return True, f"✅ {filepath} (JSON válido)"
    except json.JSONDecodeError as e:
        return False, f"❌ {filepath} (JSON inválido: {e})"
    except FileNotFoundError:
        return False, f"❌ {filepath} (arquivo não encontrado)"


def verify_deployment_structure():
    """Verifica a estrutura completa do diretório docs/."""
    print("=" * 60)
    print("VERIFICAÇÃO DE ESTRUTURA PARA GITHUB PAGES")
    print("=" * 60)
    
    errors = []
    warnings = []
    
    # Arquivos obrigatórios
    required_files = [
        "docs/index.html",
        "docs/.nojekyll",
        "docs/_config.yml",
        "docs/css/styles.css",
        "docs/js/search.js",
        "docs/js/app.js",
    ]
    
    print("\n[ARQUIVOS] Verificando arquivos obrigatorios:")
    for filepath in required_files:
        exists, message = check_file_exists(filepath)
        print(f"  {message}")
        if not exists:
            errors.append(filepath)
    
    # Arquivos opcionais mas recomendados
    optional_files = [
        "docs/404.html",
        "docs/n8nrd.png",
    ]
    
    print("\n[ARQUIVOS] Verificando arquivos opcionais:")
    for filepath in optional_files:
        exists, message = check_file_exists(filepath)
        print(f"  {message}")
        if not exists:
            warnings.append(filepath)
    
    # Arquivos da API
    api_files = [
        "docs/api/search-index.json",
        "docs/api/stats.json",
        "docs/api/categories.json",
        "docs/api/integrations.json",
        "docs/api/metadata.json",
    ]
    
    print("\n[API] Verificando arquivos da API:")
    for filepath in api_files:
        exists, message = check_file_exists(filepath)
        print(f"  {message}")
        if not exists:
            errors.append(filepath)
        else:
            # Verificar se o JSON é válido
            valid, json_message = check_json_valid(filepath)
            if not valid:
                errors.append(f"{filepath} (JSON inválido)")
            else:
                print(f"    {json_message}")
    
    # Verificar paths no index.html
    print("\n[PATHS] Verificando paths no index.html:")
    try:
        with open("docs/index.html", 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar se não há paths absolutos com /docs/
        if '/docs/' in content:
            print("  [AVISO] Encontrado path absoluto '/docs/' no index.html")
            print("     Paths devem ser relativos (sem /docs/)")
            warnings.append("Paths absolutos encontrados no index.html")
        else:
            print("  [OK] Nenhum path absoluto '/docs/' encontrado")
        
        # Verificar se os paths relativos existem
        relative_paths = [
            "css/styles.css",
            "js/search.js",
            "js/app.js",
            "n8nrd.png",
        ]
        
        for rel_path in relative_paths:
            full_path = f"docs/{rel_path}"
            exists, message = check_file_exists(full_path)
            if not exists:
                warnings.append(f"Path referenciado não encontrado: {rel_path}")
    except FileNotFoundError:
        errors.append("docs/index.html não encontrado")
    
    # Verificar paths no search.js
    print("\n[PATHS] Verificando paths no search.js:")
    try:
        with open("docs/js/search.js", 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '/docs/' in content or '/api/' in content:
            print("  [AVISO] Encontrado path absoluto no search.js")
            print("     Paths devem ser relativos (ex: 'api/search-index.json')")
            warnings.append("Paths absolutos encontrados no search.js")
        else:
            print("  [OK] Paths relativos corretos")
    except FileNotFoundError:
        errors.append("docs/js/search.js não encontrado")
    
    # Verificar estrutura do search-index.json
    print("\n[ESTRUTURA] Verificando estrutura do search-index.json:")
    try:
        with open("docs/api/search-index.json", 'r', encoding='utf-8') as f:
            search_index = json.load(f)
        
        required_keys = ["version", "generated_at", "stats", "workflows"]
        for key in required_keys:
            if key in search_index:
                print(f"  ✅ Chave '{key}' presente")
            else:
                errors.append(f"search-index.json falta chave: {key}")
        
        # Verificar se há workflows
        if "workflows" in search_index:
            workflow_count = len(search_index["workflows"])
            print(f"  ✅ {workflow_count} workflows no índice")
            if workflow_count == 0:
                warnings.append("Nenhum workflow encontrado no índice")
    except Exception as e:
        errors.append(f"Erro ao verificar search-index.json: {e}")
    
    # Resumo
    print("\n" + "=" * 60)
    print("RESUMO")
    print("=" * 60)
    
    if errors:
        print(f"\n[ERRO] ERROS ENCONTRADOS ({len(errors)}):")
        for error in errors:
            print(f"  - {error}")
        print("\n[AVISO] CORRIJA OS ERROS ANTES DE FAZER DEPLOY!")
        return False
    else:
        print("\n[OK] NENHUM ERRO ENCONTRADO!")
    
    if warnings:
        print(f"\n[AVISO] AVISOS ({len(warnings)}):")
        for warning in warnings:
            print(f"  - {warning}")
        print("\n[INFO] Estes avisos nao impedem o deploy, mas devem ser revisados.")
    else:
        print("\n[OK] NENHUM AVISO!")
    
    print("\n[OK] Estrutura pronta para deploy no GitHub Pages!")
    print("\n[PROXIMOS PASSOS]")
    print("  1. Configure GitHub Pages para usar 'GitHub Actions'")
    print("  2. Faça commit e push das mudanças")
    print("  3. Verifique o workflow em Actions")
    print("  4. Acesse: https://runawaydevil.github.io/n8n-workflows/")
    
    return len(errors) == 0


if __name__ == "__main__":
    success = verify_deployment_structure()
    exit(0 if success else 1)

