This patch allows new BGM tracks to be added to the game.

Plase note you will not be able to add a 02.ADX becase the game actually uses that to call Mass Destruction but any other ID is pretty much usable.

I'm not 100% sure but there's probbaly a total 65535 (0xffff) BGM slots.
Plase don't use BGM slots 512 to 768 becase those slots are used the FMV patch so if someone had the FMV patch enabaled the game would just attempt to play an FMV insted.

An intresting note:
-  If you call a BGM ID below 128 but the game can't load an ADX file it will fall back and make another BGM call for 02.ADX and thus play  Mass Destruction
