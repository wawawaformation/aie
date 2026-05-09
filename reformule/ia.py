#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Question - réponse avec l'API OLLAMA
"""

from get_token import get_token
import requests


def send(user_message: str, system_message: str) -> str:
    token = get_token()
    model = "gpt-oss:20b"
    url = "https://ollama.com/api/chat"

    try:
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message},
                ],
                "stream": False,
            },
            timeout=30,
        )

        response.raise_for_status()

        try:
            data = response.json()
        except ValueError:
            return "L'API a renvoyé une réponse illisible."

        message = data.get("message")

        if not isinstance(message, dict):
            return "La réponse de l'API ne contient pas de message exploitable."

        content = message.get("content")

        if not isinstance(content, str):
            return "La réponse de l'API ne contient pas de texte exploitable."

        return content

    except requests.exceptions.Timeout:
        return "L'API met trop de temps à répondre."

    except requests.exceptions.HTTPError:
        return "L'API a renvoyé une erreur HTTP."

    except requests.exceptions.RequestException:
        return "Impossible de contacter l'API."