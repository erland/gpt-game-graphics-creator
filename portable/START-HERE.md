# Game Graphics Creator – portabel ChatGPT-version

Detta paket gör den aktuella **Game Graphics Creator**-konfigurationen användbar i en vanlig ChatGPT-konversation.

När paketet bifogas:

1. Läs `assistant/instructions.md` först och använd den som arbetsinstruktion under hela konversationen.
2. Använd `assistant/conversation-starters.md` som exempel på hur GPT:n är tänkt att startas, inte som extra regler.
3. Använd exakt de 13 filerna i `knowledge/` som normativt Knowledge. De motsvarar filerna markerade för uppladdning i den aktuella Builder-konfigurationen.
4. `supporting/contract/` innehåller schemas och mallar som får användas när en Asset Request/Delivery Package ska skapas eller valideras, men de överstyr inte instruktionen eller Knowledge.
5. Om användaren bifogar ett befintligt projekt-/leveranspaket ska dess aktuella brief, spec, manifest och valideringsdata behandlas enligt instruktionens käll- och revisionsregler.
6. Påstå inte att bildgenerering, kodkörning, filinspektion eller fysisk runtime-validering har genomförts om den aktuella chatten saknar sådan kapabilitet eller evidens.

Användarens aktuella instruktioner har alltid företräde framför paketets arbetsregler.
