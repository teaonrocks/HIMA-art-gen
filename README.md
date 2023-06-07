# NFT Art Generator

This repository contains a Python script that allows you to generate NFT art based on the rarity of different layers. The script utilizes the PIL library for image manipulation and automates the process of pinning the generated art to Pinata IPFS. Additionally, it generates the necessary metadata for minting on the Cardano blockchain.

## How it works

- Use config.js to generate a rarity.json
- Script uses PIL to generate images
- Uploads it to Pinata IPFS and gets an IPFS hash
- Generates metadata with valid IPFS hash ready to be minted
