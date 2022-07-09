const { createCanvas, loadImage } = require("canvas");
const fs = require("fs");
const console = require("console");
const canvas = createCanvas(3000, 3000);
const ctx = canvas.getContext("2d");
const rarity = require("./rarity.json");
let dnas = [];

const saveImage = (_editionCount) => {
	let path = `./output/${_editionCount}.png`;
	loadImage("./assets/10 finisher/nothing.png").then((image) => {
		ctx.drawImage(image, 0, 0, 3000, 3000);
		const buffer = canvas.toBuffer("image/png");
		fs.writeFileSync(path, buffer);
		fs.writeFileSync(path, canvas.toBuffer("image/png"));
	});
	return path;
};

const clearCanvas = () => {
	loadImage("./assets/10 finisher/nothing.png").then((image) => {
		ctx.clearRect(0, 0, 3000, 3000);
	});
};

const checkDupe = (dna) => {
	for (let i = 0; i < dnas.length; i++) {
		if (dna == dnas[i]) {
			return true;
			console.log("dupe found");
		} else {
			return false;
		}
	}
};
const buildDNA = () => {
	const chooseSkin = () => {
		let prob = rarity.skinprob;
		let skin = rarity.skin;
		let chosen = Math.floor(Math.random() * (100 - 1 + 1)) + 1;
		let sum = 0;
		for (let i = 0; i < prob.length; i++) {
			sum += prob[i];
			if (chosen <= sum) {
				return i;
			}
		}
	};
	const chooseEye = () => {
		let prob = rarity.eyeprob;
		let eye = rarity.eye;
		let chosen = Math.floor(Math.random() * (100 - 1 + 1)) + 1;
		let sum = 0;
		for (let i = 0; i < prob.length; i++) {
			sum += prob[i];
			if (chosen <= sum) {
				return i;
			}
		}
	};
	const chooseHair = () => {
		let prob = rarity.hairprob;
		let hair = rarity.hair;
		let chosen = Math.floor(Math.random() * (100 - 1 + 1)) + 1;
		let sum = 0;
		for (let i = 0; i < prob.length; i++) {
			sum += prob[i];
			if (chosen <= sum) {
				return i;
			}
		}
	};
	const chooseHead = () => {
		let prob = rarity.headprob;
		let head = rarity.head;
		let chosen = Math.floor(Math.random() * (100 - 1 + 1)) + 1;
		let sum = 0;
		for (let i = 0; i < prob.length; i++) {
			sum += prob[i];
			if (chosen <= sum) {
				return i;
			}
		}
	};
	const chooseClothes = () => {
		let prob = rarity.clothesprob;
		let clothes = rarity.clothes;
		let chosen = Math.floor(Math.random() * (100 - 1 + 1)) + 1;
		let sum = 0;
		for (let i = 0; i < prob.length; i++) {
			sum += prob[i];
			if (chosen <= sum) {
				return i;
			}
		}
	};
	const chooseAccessory = () => {
		let prob = rarity.accessoryprob;
		let accessory = rarity.accessory;
		let chosen = Math.floor(Math.random() * (100 - 1 + 1)) + 1;
		let sum = 0;
		for (let i = 0; i < prob.length; i++) {
			sum += prob[i];
			if (chosen <= sum) {
				return i;
			}
		}
	};
	let dupe = true;
	let dna = [];
	while (dupe == true) {
		dna.length = 0;
		dna.push(chooseSkin());
		dna.push(chooseEye());
		dna.push(chooseHair());
		dna.push(chooseClothes());
		dna.push(chooseHead());
		dna.push(chooseAccessory());
		dupe = checkDupe(dna);
	}
	return dna;
};

const buildImage = (DNA) => {
	const drawSkin = (dna) => {
		switch (dna) {
			case 0:
				loadImage("./assets/1 skin colour/black.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 1:
				loadImage("./assets/1 skin colour/blue.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 2:
				loadImage("./assets/1 skin colour/pink.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 3:
				loadImage("./assets/1 skin colour/white.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
		}
	};

	const drawEyeDefault = (dna) => {
		switch (dna) {
			case 0:
				loadImage("./assets/2 eye default/bdmn.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 1:
				loadImage("./assets/2 eye default/heterochromia.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
		}
	};

	const drawDefault = () => {
		loadImage("./assets/3 default/DEFAULT.png").then((image) => {
			ctx.drawImage(image, 0, 0, 3000, 3000);
		});
	};

	const drawHairBack = (dna) => {
		switch (dna) {
			case 0:
				loadImage("./assets/4 hair BACK/bun.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 1:
				loadImage("./assets/4 hair BACK/curl.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 2:
				loadImage("./assets/4 hair BACK/long.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
		}
	};

	const drawClothes = (dna) => {
		switch (dna) {
			case 0:
				loadImage("./assets/5 clothes/knight.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 1:
				loadImage("./assets/5 clothes/maid.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 2:
				loadImage("./assets/5 clothes/tech.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 3:
				loadImage("./assets/5 clothes/yakuza.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
		}
	};

	const drawHairFront = (dna) => {
		switch (dna) {
			case 0:
				loadImage("./assets/6 hair FRONT/bun.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 1:
				loadImage("./assets/6 hair FRONT/curl.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 2:
				loadImage("./assets/6 hair FRONT/long.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 3:
				loadImage("./assets/6 hair FRONT/short.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
		}
	};

	const drawHeadwear = (dna) => {
		switch (dna) {
			case 0:
				loadImage("./assets/7 headwear/flowercrown.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 1:
				loadImage("./assets/7 headwear/halo.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 2:
				loadImage("./assets/7 headwear/maid.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 3:
				loadImage("./assets/7 headwear/tiara.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
		}
	};

	const drawEyeSpecial = (dna) => {
		switch (dna) {
			case 2:
				loadImage("./assets/8 eye special/gold.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 3:
				loadImage("./assets/8 eye special/lightning.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
		}
	};

	const drawAccessory = (dna) => {
		switch (dna) {
			case 0:
				loadImage("./assets/9 accessory/flower.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 1:
				loadImage("./assets/9 accessory/mask.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 2:
				loadImage("./assets/9 accessory/nvg.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
			case 3:
				loadImage("./assets/9 accessory/secglasses.png").then((image) => {
					ctx.drawImage(image, 0, 0, 3000, 3000);
				});
				break;
		}
	};
	dna = buildDNA();
	drawSkin(dna[0]);
	drawEyeDefault(dna[1]);
	drawDefault();
	drawHairBack(dna[2]);
	drawClothes(dna[3]);
	drawHairFront(dna[2]);
	drawHeadwear(dna[4]);
	drawEyeSpecial(dna[1]);
	drawAccessory(dna[5]);
	return dna;
};
const get_random_name = () => {
	const full_names_json = require("./full_names.json");
	let full_names = full_names_json["full_names"];
	return full_names[Math.floor(Math.random() * full_names.length)];
};

let gen = {
	items: [],
};
for (i = 0; i < 3; i++) {
	let dna = buildImage();
	let name = get_random_name();
	let path = saveImage(name);
	clearCanvas();
	gen.items.push({
		dna: dna,
		name: name,
		path: path,
	});
}
fs.writeFile(`items.json`, JSON.stringify(gen), (error) => {
	if (error) throw error;
});
