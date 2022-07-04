This is a patch that allows new FMVs to be added to the game!

FMVs use the BGM naming scheme.
The extension is .pmsf.
Before the extension is the numeric ID.

All IDs below 100 must use 2 digits eg. 00.pmsf or 10.pmsf

IDs above 99 are 3 digits 100.pmsf or 200.pmsf

There are a total 256 available slots ranging from 00.pmsf to 255.pmsf.


For a guide on creating new PMSF files you can follow this guide please be aware as of now I'm only aware how to create FMVs at native psp res.
For all intents and purposes PMSF, PMF and PSMF are all the same thing.
https://projectdiva.net/community/threads/2020-create-pmf-videos-for-psp-games.2348/

Your new PMSF files must be placed on your memory stick in PSP\P3P\FMV\

To call your FMVs in game you use the Call_BGM function with an ID of 512 + the ID of the PMSF file.
For example if I want to call 10.PMSF I'd call a BGM with an id 522
