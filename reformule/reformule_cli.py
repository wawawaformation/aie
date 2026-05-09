#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Principale du projet de reformulation de texte avec l'API OLLAMA
"""

from ia import send
from args import parse_args


def lire_fichier(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise RuntimeError(f"Le fichier n'existe pas : {path}")
    except PermissionError:
        raise RuntimeError(f"Vous n'avez pas les droits pour lire le fichier : {path}")
    except IsADirectoryError:
        raise RuntimeError(f"Le chemin indiqué est un dossier, pas un fichier : {path}")


def ecrire_fichier(path: str, content: str) -> None:
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)
    except PermissionError:
        raise RuntimeError(f"Vous n'avez pas les droits pour écrire dans le fichier : {path}")
    except IsADirectoryError:
        raise RuntimeError(f"Le chemin de sortie indiqué est un dossier : {path}")


def main() -> int:
    try:
        args = parse_args()

        system_message = f"Reformule le texte suivant en utilisant un ton {args.tone} :"

        user_message = lire_fichier(args.input)

        if args.context:
            context_message = lire_fichier(args.context)
            system_message += f"\n\nContexte supplémentaire : {context_message}"

        result = send(user_message, system_message)

        if args.output:
            ecrire_fichier(args.output, result)
        else:
            print(result)

        return 0

    except RuntimeError as error:
        print(f"Erreur : {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())