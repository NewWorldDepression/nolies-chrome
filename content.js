async function getOwnershipData() {
    const response = await fetch(chrome.runtime.getURL("ownership.json"));
    return response.json();
}

async function displayBanner() {
    const hostname = window.location.hostname.replace("www.", ""); // Ex: www.nytimes.com -> nytimes.com
    const ownershipData = await getOwnershipData();

    if (ownershipData[hostname]) {
        const owner = ownershipData[hostname];

        // Create banner
        const banner = document.createElement("div");
        banner.innerText = `Ce média appartient à : ${owner}.`;
        banner.style.position = "fixed";
        banner.style.top = "0";
        banner.style.left = "0";
        banner.style.width = "100%";
        banner.style.backgroundColor = "black";
        banner.style.color = "white";
        banner.style.padding = "10px";
        banner.style.fontSize = "16px";
        banner.style.zIndex = "10000";
        document.body.appendChild(banner);

        // Remove banner after 60 seconds
        setTimeout(() => {
            banner.remove();
        }, 60000);
    }
}

displayBanner();