//내가 만든 파일
const hre = require("hardhat");

async function main() {
    const HelloWorld = await hre.ethers.getContractFactory("HelloWorld");
    const helloWorld = await HelloWorld.deploy("Hello, Blockchain!");

    await helloWorld.deployed();

    console.log("HelloWorld deployed to:", helloWorld.address);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
