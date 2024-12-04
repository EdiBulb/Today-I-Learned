const hre = require("hardhat"); // Hardhat Runtime Environment

async function main() {

    //1. 배포할 컨트랙트 가져오기
    const ContractName = await hre.ethers.getContractFactory("ContractName");

    //2. 컨트랙트 배포(필요한 매개변수 전달)
    const contract = await ContractName.deploy(/* constructor arguments */);

    //3. 배포 완료 대기
    await contract.deployed();

    //4. 배포된 컨트랙트 주소 출력
    console.log("ContractName deployed to:", contract.address);
}

// 오류 처리
main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
