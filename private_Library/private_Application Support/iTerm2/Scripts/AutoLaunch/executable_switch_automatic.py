#!/usr/bin/env python3

import asyncio
import os
import iterm2


async def main(connection):
    async with iterm2.VariableMonitor(connection, iterm2.VariableScopes.APP, "effectiveTheme", None) as mon:
        while True:
            # Block until theme changes
            theme = await mon.async_get()

            # Themes have space-delimited attributes, one of which will be light or dark.
            parts = theme.split(" ")
            if "dark" in parts:
                preset = await iterm2.ColorPreset.async_get(connection, "Dark Background")
                os.system(
                    "bash -c 'rm -rf $HOME/.vimrc-theme; ln -s $HOME/.vimrc-theme-dark $HOME/.vimrc-theme'")
                os.system(
                    "bash -c 'rm -rf $HOME/.tmux-theme; ln -s $HOME/.tmux-sol-dark.conf $HOME/.tmux-theme'")
            else:
                preset = await iterm2.ColorPreset.async_get(connection, "Light Background")
                os.system(
                    "bash -c 'rm -rf $HOME/.vimrc-theme; ln -s $HOME/.vimrc-theme-light $HOME/.vimrc-theme'")
                os.system(
                    "bash -c 'rm -rf $HOME/.tmux-theme; ln -s $HOME/.tmux-sol-light.conf $HOME/.tmux-theme'")

            # Update the list of all profiles and iterate over them.
            profiles = await iterm2.PartialProfile.async_query(connection)
            for partial in profiles:
                # Fetch the full profile and then set the color preset in it.
                profile = await partial.async_get_full_profile()
                await profile.async_set_color_preset(preset)

iterm2.run_forever(main)
