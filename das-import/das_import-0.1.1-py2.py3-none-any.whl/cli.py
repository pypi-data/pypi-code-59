import argparse
import csv
import logging

from tqdm import tqdm

from .client import Client
from .exceptions import CardImportError
from .types import Card, CardType, Expansion

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Import cards to Decks Against Society"
    )
    parser.add_argument("-u", "--username", help="DAS username", required=True)
    parser.add_argument("-p", "--password", help="DAS password", required=True)
    parser.add_argument(
        "-e", "--expansion", help="Deck ID to add new cards to", required=True
    )
    parser.add_argument(
        "-c", "--card-type", type=CardType, choices=list(CardType), required=True
    )
    parser.add_argument(
        "file", help="Path to file with cards (separated with new lines)"
    )

    args = parser.parse_args()

    with open(args.file) as file_:
        reader = csv.reader(file_)
        cards = list(load_cards(args.card_type, reader))
        logger.info(f"Read {len(cards)} card(s)")

    client = Client(args.username, args.password)
    expansion = Expansion(args.expansion)

    failed_cards = []
    for i, card in enumerate(tqdm(cards, unit="cards"), start=1):
        try:
            client.add_card(expansion, card)
        except CardImportError:
            failed_cards.append((i, card))

    logger.info(f"Successfully loaded {len(cards)-len(failed_cards)} card(s)")
    if failed_cards:
        breakdown = "\n".join(f"{i}. {card.content}" for i, card in failed_cards)
        logger.error(f"Following cards failed to import:\n{breakdown}")


def load_cards(card_type, file_):
    for row in file_:
        yield Card(type=card_type, content=row[0].strip())


if __name__ == "__main__":
    main()
