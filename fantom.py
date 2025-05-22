import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=['--start-maximized'])
    page = await browser.newPage()
    await page.goto('https://faucets.chain.link/', {'waitUntil': 'networkidle2'})

    # Wait for the wallet input field to appear
    await page.waitForSelector('input[type="text"]', timeout=20000)

    # Enter your Fantom Testnet wallet address
    wallet_address = '0xYourFantomTestnetWalletAddress'  # <-- Replace with your address
    await page.type('input[type="text"]', wallet_address)

    # Select Fantom Testnet faucet (update selector if needed)
    # The label's "for" attribute might be like "fantomTestnet"
    await page.click('label[for="fantomTestnet"]')

    # Click the "Send Request" button (update selector if needed)
    await page.click('button[type="submit"]')

    # Wait to observe result
    await page.waitFor(5000)

    print("Faucet request sent (if all went well).")
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
