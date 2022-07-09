const fs = require("fs");
let rarity ={};
rarity.skin = ["black", "blue", "pink", "white"];
rarity.skinprob = [40,10,20,30];
rarity.eye = ["bdmn", "Hchromia","gold","lightning","default"];
rarity.eyeprob = [10,10,20,20,40];
rarity.hair = ["bun","curl","long","short"];
rarity.hairprob = [10,20,35,35];
rarity.clothes = ["knight", "maid", "tech", "yakuza"];
rarity.clothesprob = [10,20,30,40];
rarity.head = ["flowercrown", "halo", "maid", "tiara"];
rarity.headprob = [10,20,30,40];
rarity.accessory = ["flower", "mask", "nvg", "secglasses"];
rarity.accessoryprob = [10,20,30,40];
fs.writeFile('rarity.json', JSON.stringify(rarity), (error) => {
    if (error) throw error;
  });