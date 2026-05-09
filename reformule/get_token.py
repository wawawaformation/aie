#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Retourner un token d'accès à l'API OLLAMA
"""

import os

def get_token():
    """
    Retourner un token d'accès à l'API OLLAMA
    """
    token = os.getenv("OLLAMA_API_KEY")
    if not token:
        raise ValueError("Le token d'accès à l'API OLLAMA n'est pas défini. Veuillez définir la variable d'environnement OLLAMA_API_KEY.")
    return token

if __name__ == "__main__":
    try:
        token = get_token()
        print("Le token est bien défini.")

        if not token:
            raise ValueError("OLLAMA_API_KEY manquant ou vide.")
    except ValueError as e:
        print(e)
