import asyncio
from typing import Dict, Optional, Union
from warnings import warn

from discord import Emoji, PartialEmoji
from discord.abc import GuildChannel
from discord.ext.commands import Context

from dpymenus import ButtonMenu
from dpymenus.exceptions import ButtonsError, CallbackError


class PaginatedMenu(ButtonMenu):
    """
    Represents a button-based response menu.

    :param ctx: A reference to the command context.
    :param timeout: How long (in seconds) to wait before timing out.
    :param data: A dictionary containing variables to pass around menu functions.
    """

    def __init__(self, ctx: Context, timeout: int = 300, data: Optional[Dict] = None):
        super().__init__(ctx, timeout)
        self.data = data if data else {}

    def __repr__(self):
        return f'<Menu pages={[p.__str__() for p in self.pages]}, timeout={self.timeout}, ' \
               f'active={self.active} page={self.page_index}, data={self.data}>'

    async def open(self):
        """The entry point to a new TextMenu instance; starts the main menu loop.
        Manages gathering user input, basic validation, sending messages, and cancellation requests."""
        await super()._validate_pages()
        await self._validate_buttons()

        self.output = await self.ctx.send(embed=self.page)

        await self._add_buttons()

        while self.active:
            self.input = await self._get_reaction()
            await self.output.remove_reaction(self.input, self.ctx.author)

            await self.page.on_next(self)

        await self._cleanup_reactions()

    # Internal Methods
    async def _validate_buttons(self):
        """Ensures that a button menu was passed the appropriate amount of buttons."""
        _cb_count = 0
        for page in self.pages:
            if page.buttons is None:
                break

            if page.on_next:
                _cb_count += 1

            if len(page.buttons) <= 1:
                raise ButtonsError('Any page with an `on_next` callback must have at least one button.')

            if len(page.buttons) > 5:
                warn('Adding more than 5 buttons to a page at once may result in discord.py throttling the bot client.')

        if self.page.on_fail:
            raise CallbackError('A ButtonMenu can not have an `on_fail` callback.')

        if _cb_count < len(self.pages) - 1:
            raise CallbackError(f'ButtonMenu missing `on_next` callbacks. Expected {len(self.pages) - 1}, found {_cb_count}.')
