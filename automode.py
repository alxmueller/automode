#!/usr/bin/env python3

import asyncio

# noinspection PyUnresolvedReferences
import iterm2


def profile_name(os_theme):
    return {
        "light": "Light Profile",
        "dark": "Dark Profile",
    }[os_theme]


async def set_profile(connection, name, session_id=None):
    app = await iterm2.async_get_app(connection)

    partial_profiles = await iterm2.PartialProfile.async_query(connection)
    for partial_profile in partial_profiles:
        if partial_profile.name == name:
            profile = await partial_profile.async_get_full_profile()
            await profile.async_make_default()
            if session_id is not None:
                session = app.get_session_by_id(session_id)
                await session.async_set_profile(profile)
            else:
                for window in app.terminal_windows:
                    for tab in window.tabs:
                        for session in tab.sessions:
                            await session.async_set_profile(profile)
            break


async def monitor_sessions(connection):
    app = await iterm2.async_get_app(connection)

    async with iterm2.EachSessionOnceMonitor(app) as monitor:
        while True:
            session_id = await monitor.async_get()
            os_theme = (await app.async_get_theme())[0]
            await set_profile(connection, profile_name(os_theme), session_id)


async def monitor_os_theme(connection):
    async with iterm2.VariableMonitor(
        connection, iterm2.VariableScopes.APP, "effectiveTheme", None
    ) as monitor:
        while True:
            os_theme = (await monitor.async_get()).split(" ")[0]
            await set_profile(connection, profile_name(os_theme))


async def main(connection):
    asyncio.create_task(monitor_sessions(connection))
    asyncio.create_task(monitor_os_theme(connection))


iterm2.run_forever(main)
