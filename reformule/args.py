#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--input",
        help="Chemin vers le fichier d'entrée contenant le texte à reformuler",
        required=True)
    parser.add_argument(
        "-t", "--tone", 
        default="simple",
        choices=["simple", "humoristique", "commercial", "professionnel", "amical", "formel", "informel", "redacteur_web_seo"],
        help="Ton de la reformulation (par défaut: simple)")
    parser.add_argument(
        "-o", "--output", 
        default=None,
        help="Chemin vers le fichier de sortie. Si non spécifié, le résultat sera affiché dans la console")
    parser.add_argument(
        "-c", "--context",
        default=None,
        help="Contexte supplémentaire pour la reformulation. Fichier contenant des informations contextuelles ou des instructions spécifiques pour guider la reformulation  ")
    return parser.parse_args()
