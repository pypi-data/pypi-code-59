from typing import *
import royalnet
import royalnet.commands as rc
import royalnet.utils as ru
from ..tables import Treasure, FiorygiTransaction


class TreasureCommand(rc.Command):
    name: str = "treasure"

    description: str = "Riscatta un Treasure che hai trovato da qualche parte."

    syntax: str = "{code}"

    async def run(self, args: rc.CommandArgs, data: rc.CommandData) -> None:
        author = await data.get_author(error_if_none=True)
        code = args[0].lower()

        TreasureT = self.alchemy.get(Treasure)

        treasure = await ru.asyncify(data.session.query(TreasureT).get, code)
        if treasure is None:
            raise rc.UserError("Non esiste nessun Treasure con quel codice.")
        if treasure.redeemed_by is not None:
            raise rc.UserError(f"Quel tesoro è già stato riscattato da {treasure.redeemed_by}.")

        treasure.redeemed_by = author
        await data.session_commit()
        await FiorygiTransaction.spawn_fiorygi(data,
                                               author,
                                               treasure.value,
                                               f'aver trovato il tesoro "{treasure.code}"')
        await data.reply("🤑 Tesoro riscattato!")
