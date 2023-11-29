from playwright.sync_api import expect

def test_get_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    expect(page.locator(".t-title")).to_have_text("Check Password")

def test_valid_password(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.fill("input[name='password']", "9George77g9&^9lIoN77)When9n77")
    print(page.locator("input[value='Check Password']"))
    page.click("input[value='Check Password']")
    expect(page.locator(".t-result")).to_contain_text("passes the validity test!")

def test_invalid_password(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.fill("input[name='password']", "dddd")
    page.click("input[value='Check Password']")
    expect(page.locator(".t-result")).to_contain_text("failed!")

def test_back_to_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.fill("input[name='password']", "9George77g9&^9lIoN77)When9n77")
    page.click("input[value='Check Password']")
    page.click("text=Try Again")
    expect(page.locator(".t-title")).to_have_text("Check Password")
